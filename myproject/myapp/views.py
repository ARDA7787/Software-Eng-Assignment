from django.shortcuts import render

def cv_views(request):
    return render(request, 'cv.html')
