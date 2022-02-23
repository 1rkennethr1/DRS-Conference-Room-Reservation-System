from django.shortcuts import render

def IndexView(request):
    return render(request, 'index.html')
    
def ContactView(request):
    return render(request, 'contact_us.html')

# Create your views here.
