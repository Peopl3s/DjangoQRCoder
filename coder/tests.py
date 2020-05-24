from django.test import TestCase
from django.urls import reverse
from django.test import Client
from .processfunc import *

class IndexViewTests(TestCase):
	def test_index_view_with_no_login_user(self):
		"""
		If no login user, an appropriate message should be displayed.
		"""
		client = Client()
		response = client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Нет досутпа. Необходимо войти на сайт".encode('utf-8'))
	
	def test_index_view_with_no_docx_doc_input_file(self):
		"""
		If input file is't .docx/doc extentions, an appropriate message should be displayed.
		"""
		client = Client()
		response = client.post('/accounts/login/', {'username': 'peoples', 'password': 'GGdd98611'})
		self.assertEqual(response.status_code, 200)
		response = client.post('/', {'file': 'hello.php'})
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "Назад".encode('utf-8'))
	
		
class UtilityFunctionTests(TestCase):
	def test_is_ms_word_file_checker_func_correct(self):
		"""
		True if input file has docx/doc ext
		"""
		self.assertEqual(isMsWordFile('hello.docx'), True)
	
