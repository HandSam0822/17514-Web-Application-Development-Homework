from multiprocessing import context
from django.shortcuts import render
from .forms import NumberForm

# Create your views here.
def calculator(request):
    context = {}
    context["form"] = NumberForm()
    if request.method == "GET":
        context["x"] = 2
        context["y"] = 5
        context["res"] = 2 / 5
        return render(request, "calculator/calculator.html", context)
    else:
        # A form bound to the POST data
        form = NumberForm(request.POST)
        if not form.is_valid():  # All validation rules pass
            return render(request, "calculator/calculator.html", context)

        # Process the data in form.cleaned_data
        x = int(form["x"].value())
        y = int(form["y"].value())
        res = x / y
        context["x"] = x
        context["y"] = y
        context["res"] = res
        return render(request, "calculator/calculator.html", context)
