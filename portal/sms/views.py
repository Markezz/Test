from django.shortcuts import render, render_to_response


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html', {})