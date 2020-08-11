from django.shortcuts import render

# Create your views here.


def select_store(request):
    print("working..................")
    return render(request, 'select_store/select-store.html')
