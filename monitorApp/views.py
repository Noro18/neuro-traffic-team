from django.shortcuts import render
from django.http import StreamingHttpResponse
from monitorApp.inference import run_inference  # Import your generator
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Sum
from django.db.models.functions import TruncHour

# Create your views here.

def monitorApp(request):
    return render(request, 'inference.html')
def gen(): # function ida ne'e hanesan function tambahan ne'ebe loop kada frame husi inference ne'ebe halao iha inference.py
    for frame in run_inference():
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@login_required

def dashboard(request):
    return render(request, 'dashboard.html')
@login_required
def video_feed(request):
    return StreamingHttpResponse(gen(), content_type='multipart/x-mixed-replace; boundary=frame')
@login_required







def analysis(request):
    from django.db.models.functions import TruncHour
    from .models import DetailDetail
    # Group by hour and sum quantity
    hour_data = (
        DetailDetail.objects
        .annotate(hour=TruncHour('id_detecta__oras'))
        .values('hour')
        .annotate(total=Sum('quantity'))
        .order_by('hour')
    )
    # Prepare lists for labels and data
    hour_labels = [item['hour'].strftime('%H:00') for item in hour_data]
    hour_totals = [item['total'] for item in hour_data]

    # (Keep your donut chart code here as before)
    class_data = (
        DetailDetail.objects
        .values('id_class__naran_class')
        .annotate(total=Sum('quantity'))
        .order_by('id_class__naran_class')
    )
    labels = [item['id_class__naran_class'] for item in class_data]
    data = [item['total'] for item in class_data]

    context = {
        'donut_labels': json.dumps(labels),
        'donut_data': json.dumps(data),
        'line_labels': json.dumps(hour_labels),
        'line_data': json.dumps(hour_totals),
    }
    return render(request, 'analysis.html', context)


