from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DocumentForm
from .models import Document

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            get_all_files(request)
    else:
        form = DocumentForm()
    return render(request, 'index.html', {'form': form})


def clear_all_images(request):
    Document.objects.all().delete()
    return get_all_files(request)


def get_all_files(request):
    documents = Document.objects.all()
    if documents is not None:
        return render(request, 'all_images.html', {'documents': documents})
    else:
        model_form_upload(request)