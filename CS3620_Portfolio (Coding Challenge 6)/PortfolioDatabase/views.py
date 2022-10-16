from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies
from .models import Contact
from .forms import PortfolioForm, ContactForm
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
    contact = Contact.objects.all()
    context = {
        'contact': contact,
    }
    return render(request, 'PortfolioDatabase/contact.html', context)


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


def create_item(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/form.html', {'form': form})


def update_item(request, id):
    item = Portfolio.objects.get(id=id)
    form = PortfolioForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/form.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('PortfolioDatabase:portfolio')

    return render(request, 'PortfolioDatabase/portfolio-delete.html', {'item': item})


def create_contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('PortfolioDatabase:contact')

    return render(request, 'PortfolioDatabase/form.html', {'form': form})
