from django.shortcuts import render
from .models import Build
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
import io


# Create your views here.

def home(request):
    return render(request, 'project/home.html')


def build_accept(request):
    if request.method == 'POST':
        # form = Build(request.POST, request.FILES)
        battle_name = request.POST.get('battle_name', '')
        monster_build = request.POST.get('monster_build', '')
        skill_1 = request.POST.get('skill_1', '')
        equip_1 = request.POST.get('equip_1', '')
        skill_2 = request.POST.get('skill_2', '')
        equip_2 = request.POST.get('equip_2', '')
        skill_3 = request.POST.get('skill_3', '')
        equip_3 = request.POST.get('equip_3', '')
        strategy = request.POST.get('strategy', '')
        build = Build(battle_name=battle_name, monster_build=monster_build, skill_1=skill_1, equip_1=equip_1, skill_2=skill_2, equip_2=equip_2, skill_3=skill_3, equip_3=equip_3, strategy=strategy)

        build.save()
    return render(request, 'project/build_accept.html') #{'form': form}


def build_printout(request, id):
    user_build = Build.objects.get(pk=id)
    template = loader.get_template('project/build_printout.html')
    html = template.render({'user_build': user_build})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        # had to enter the below code to resolve error "wkhtmltopdf reported an error: Exit with code 1 due to network error: ProtocolUnknownError" when attempting to download the pdf
        'enable-local-file-access': "",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "monster_build.pdf"

    return response


def build_list(request):
    builds = Build.objects.all()
    fight_name = request.GET.get('fight_name')
    if fight_name != '' and fight_name is not None:
        builds = builds.filter(battle_name__icontains=fight_name)
    paginator = Paginator(builds, 5)
    page = request.GET.get('page')
    builds = paginator.get_page(page)
    return render(request, 'project/build_list.html', {'builds': builds})


def image_test(request):
    return render(request, 'project/image_test.html')
