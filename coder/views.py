from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseBadRequest, FileResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .forms import UploadFileForm, MyForm
from .processfunc import *

def index(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			fileName = request.FILES['file']
			if isMsWordFile(fileName.name):
				downloadedFile = downloadFileOnServer(fileName)
				pocessedFile = processDonloadedFile(downloadedFile)
				return render(request, 'coder/download.html', {'fp' : pocessedFile})
			else:
				return render(request, 'coder/error.html', {})
		else:
			return 	HttpResponse('<h2>{0}</h2>'.format(form.errors))	
	else:
		form = UploadFileForm()
	return render(request, 'coder/index.html', {'form': form})
	
@login_required
def download(request, file):
	response = FileResponse(open(file, 'rb'))
	fileName = getFileName(file)
	response['Content-Disposition'] = 'attachment; filename="{0}"'.format(fileName)
	return response
	
class MyRegisterFormView(FormView):
    form_class = MyForm

    success_url = '/'

    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)
        
