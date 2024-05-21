from django.shortcuts import render


def chart_view(request):
    return render(request, 'chart.html')
