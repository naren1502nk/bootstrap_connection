from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'mdb_bootstrap.html')