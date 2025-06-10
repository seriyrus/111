from django.shortcuts import render
from .forms import Form1

def index(request):
    form = Form1()
    far = 0
    if request.method == 'POST':
        form = Form1(request.POST)
        if form.is_valid():
            far = 9/5*int(form.cleaned_data['celsius']) + 32
        else:
            orm = Form1()
    data = {
        'form': form,
        'far': far
    }
    return render(request, 'main/index.html', data)
