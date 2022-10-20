import random
from django.shortcuts import render, redirect
from.forms import MadlibForm
from.models import Madlibs


# Create your views here.
def index(request):
    form = MadlibForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('madlibs:madlib')

    return render(request, 'madlibs/index.html', {'form': form})


def madlib(request):
    input_list = Madlibs.objects.all().last()
    context = {
        'input_list': input_list,
    }
    randomStory = [
        'madlibs/madlib.html',
        'madlibs/madlib2.html',
        'madlibs/madlib3.html',
        'madlibs/madlib4.html',
        'madlibs/madlib5.html',
        'madlibs/madlib6.html',
        'madlibs/madlib7.html',
        'madlibs/madlib8.html',
        'madlibs/madlib9.html',
        'madlibs/madlib10.html',
        'madlibs/madlib11.html',
        'madlibs/madlib12.html',
        'madlibs/madlib13.html',
        'madlibs/madlib14.html',
        'madlibs/madlib15.html',
    ]
    pickRandom = random.choice(randomStory)
    return render(request, pickRandom, context)
