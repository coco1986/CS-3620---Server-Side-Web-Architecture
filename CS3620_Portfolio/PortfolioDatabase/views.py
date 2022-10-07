from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies
from django.template import loader


# Create your views here.
def home(request):
    return render(request, 'PortfolioDatabase/home.html')


def hobbies(request):
    hobby_list = Hobbies.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'PortfolioDatabase/hobbies.html', context)


def portfolio(request):
    p_list = Portfolio.objects.all()
    context = {
        'p_list': p_list
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)


def contact(request):
    return render(request, 'PortfolioDatabase/contact.html')


def hobby_detail(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'PortfolioDatabase/hobby_details.html', context)


def portfolio_detail(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'PortfolioDatabase/portfolio_details.html', context)
