from django.shortcuts import render
import json
from requests import Response
from django.http import HttpResponse
from .models import Sample


# Create your views here.


def foo(request):
    context = {
            # "a": {"x": 3, "y": 4},
            "a": json.dumps({"x": 3, "y": 4}),
            "c": {"x": 5, "y": 6},
            "b": 2
    }

    context = {}

    context["jd"] = json.dumps({"x": 1, "y": 2})
    context["dd"] = {"a": 1}
    # return render(request, template_name='template_misc/hello.html', context=context)
    # return render(request, 'template_misc/hello.html', context)
    return render(request, 'template_misc/hello.html', context)


def bar(request):
    sample_model = Sample(name="toran")
    sample_model2 = Sample(name="toran", age=25)
    return HttpResponse(json.dumps({
        "name2": bool(sample_model2.name),
        "comp2bool": bool(sample_model2.company),
        "comp1": sample_model2.company,
        "age2": bool(sample_model2.age),
        "age1": sample_model.age
        }))
