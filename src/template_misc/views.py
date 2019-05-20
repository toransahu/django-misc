from django.shortcuts import render
import json
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
