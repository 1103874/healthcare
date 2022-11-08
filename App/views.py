from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import DailyHealthCheckForm
from .models import DailyHealthCheck


def index(request):

    qs = DailyHealthCheck.objects.all().order_by('create_date')

    return render(request, 'HealthReasultList.html', {'qs': qs})


def createhealth(request):

    if request.method == 'POST':
        form = DailyHealthCheckForm(request.POST)
        if form.is_valid():
            DailyHealthCheck = form.save(request.POST)
            DailyHealthCheck.create_date = timezone.now()
            DailyHealthCheck.save()
            return redirect('App:index')

    else:
        form = DailyHealthCheckForm

    return render(request, 'HealthCreate.html', {'form': form})