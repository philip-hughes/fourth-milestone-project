from django.http import HttpResponseRedirect


def select_store_decorator(function):
    def _function(request, *args, **kwargs):
        if request.session.get('store') is None:
            return HttpResponseRedirect('/')
        return function(request, *args, **kwargs)
    return _function
