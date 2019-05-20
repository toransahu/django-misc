from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def foo(request):
    context = {
        "a": 1,
        "b": 2
    }
    # return render(request, template_name='template_misc/hello.html', context=context)
    return render(request, 'template_misc/hello.html', context)
