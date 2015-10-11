from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.views import generic
import time
from abox import logger
# Imaginary function to handle an uploaded file.


def handle_uploaded_file(resource):
    original_name = resource.name
    last_dot = original_name.rindex('.')
    params = {
        'filename': original_name[:last_dot],
        'extname': original_name[last_dot:],
        'time': str(time.time()).replace('.', '_'),
        'dest_dir': '/data/python/virtualenv/workspace/af/storage/upload',
    }

    destpath = '%(dest_dir)s/%(filename)s_%(time)s.%(extname)s' % params
    with open(destpath, 'wb+') as destination:
        destination.write(resource.read())


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['resource'])
            raise SyntaxError
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(
        request,
        'storage/upload.html',
        {'form': form},
    )


class ImageView(generic.DetailView):
    pass


# Create your views here.
