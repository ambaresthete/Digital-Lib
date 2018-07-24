from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from pro2.forms import DocumentForm
from .models import Contact
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

def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feed = request.POST.get('feed')
        inlineRadioOptions = request.POST.get('inlineRadioOptions')
        Contact.objects.create(name=name,email=email,feed=feed,radio=inlineRadioOptions)
    return render(request,"contact.html",{})