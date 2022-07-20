from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models  import Thetaimage
# Create your views here.

def home(request):
    # return HttpResponse("Hello, world")
    images = Thetaimage.objects
    return render(request,'aTheta_images/home.html', {'images': images})

def details(request, image_id):
    theta_image = get_object_or_404(Thetaimage, pk=image_id)
    return render(request, 'aTheta_images/details.html', {"theta_image": theta_image})