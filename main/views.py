from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import datetime
from .models import *
from .forms import RecordForm


def test_view(request):
    return HttpResponse(
        """
        <h1 style="color:teal;">Bosh sahifa</h1>
        <hr>
        <p>Bugun djangoda MVT prinsiplarini qollash orqali website yaratamiz!</p>
        
        
        """
    )

def index_view(request):
    context = {
        'now':datetime.datetime.now()
    }
    return render(request, 'index.html',context)

def kitoblar_view(request):
    if request.method == 'POST':
        muallif = get_object_or_404(Muallif,id=request.POST.get('muallif_id'))
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=get_object_or_404(Muallif, id=request.POST.get('muallif_id')),
)
        return redirect('/kitoblar/')
    kitoblar = Kitob.objects.all()
    mualliflar = Muallif.objects.all()
    context = {
        'kitoblar':kitoblar,
        'mualliflar':mualliflar,
    }
    return render(request,'kitoblar.html',context)


def kitob_retrieve_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob': kitob
    }
    return render(request, 'kitob_detail.html', context)
def kitob_delete_confirm_view(request,kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob':kitob,
    }
    return render(request, 'kitob-delete-confirm.html',context)

def kitob_delete_view(request,kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    kitob.delete()
    return redirect('/kitoblar/')

def talabalar_view(request):
    talabalar = Talaba.objects.all()

    search = request.GET.get('search')

    if request.method == 'POST':
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else 0
        )
        return redirect('/talabalar/')
    if search:
        talabalar = talabalar.filter(ism__contains=search)
    order = request.GET.get('order')
    if order:
        talabalar = talabalar.order_by(order )
    kurs = request.GET.get('kurs')
    if kurs:
        talabalar = talabalar.filter(kurs=kurs)
    context = {
        'talabalar':talabalar,
        'search':search,
        'order':order,
        'kurs':kurs,
    }
    return render(request,'talabalar.html',context)

def talaba_retrieve_view(request, talaba_id):
     talaba = Talaba.objects.get(id = talaba_id)
     context = {
         'talaba': talaba,
     }
     return render(request,'talaba_retrieve.html',context)

def talaba_delete_confirm_view(request,talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba':talaba,
    }
    return render(request, 'talaba-delete-confirm.html',context)

def talaba_update_view(request,talaba_id):
    talaba = get_object_or_404(Talaba, id=talaba_id)
    if request.method == "POST":
        Talaba.objects.filter(id=talaba_id).update(
            ism=request.POST.get('ism'),
            # guruh=request.POST.get('guruh'),
            # kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni'),
        )
        return redirect('talabalar')
    context = {
        'talaba':talaba,
    }
    return render(request,'talaba-update.html',context)

def talaba_delete_view(request,talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect('/talabalar/')


def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    if request.method == 'POST':
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            jins=request.POST.get('jins'),
            t_sana=request.POST.get('t_sana') or None,
            kitob_soni=request.POST.get('kitob_soni') if request.POST.get('kitob_soni') else 0,
            tirik=(request.POST.get('tirik') == 'True')
        )
        return redirect('/talabalar/')
    search = request.GET.get('search')
    if search:
        mualliflar = mualliflar.filter(ism__contains=search)
    order = request.GET.get('order')
    if order:
        mualliflar = mualliflar.order_by(order)
    kurs = request.GET.get('kurs')
    if kurs:
        mualliflar = mualliflar.filter(kurs=kurs)
    context = {
        'mualliflar': mualliflar,
        'search': search,
        'order': order,
        'kurs':mualliflar,
    }

    return render(request, 'mualliflar.html', context)

def muallif_retrieve_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_retrieve.html', context)
def muallif_delete_confirm_view(request,muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif':muallif,
    }
    return render(request, 'muallif-delete-confirm.html',context)


def muallif_delete_view(request,muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    muallif.delete()
    return redirect('/mualliflar/')

