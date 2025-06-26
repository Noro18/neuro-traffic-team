from django.shortcuts import render
from django.http import StreamingHttpResponse
from monitorApp.inference import run_inference  # Import your generator
# Create your views here.

def monitorApp(request):
    return render(request, 'inference.html')
def gen(): # function ida ne'e hanesan function tambahan ne'ebe loop kada frame husi inference ne'ebe halao iha inference.py
    for frame in run_inference():
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(), content_type='multipart/x-mixed-replace; boundary=frame')