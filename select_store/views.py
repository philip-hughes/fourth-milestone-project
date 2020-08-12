from django.shortcuts import render

# Create your views here.


def select_store(request):
    if request.POST:
        print("working..................")
        print("request data", request.POST)
    else:
        print('not form request')
            
    return render(request, 'select_store/select-store.html')
