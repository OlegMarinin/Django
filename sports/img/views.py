# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import ImageForm
# def img_home(request):
#     return render(request, 'img/image.html')
#
#
# def upload_images(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/")
#     else:
#         form = ImageForm
#
#     return render(request, 'files/images.html', {'form':form})

from django.shortcuts import render
from .models import Img


def upload_images(request):
    if request.method == 'GET':
        images = Img.objects.order_by('title')
        return render(request, "img/image.html", {"images": images })