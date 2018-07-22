from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from pro2.forms import DocumentForm
# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, "model_form_upload.html", {
        'form': form
        }
        )
