from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import forms
from .models import Shift

# from django.db.models import Sum, Count


def initial_page(request):
    return render(request, 'hoursCalc/initial_page.html')

#aqui tem um login requirido

def index(request):

    users = User.objects.all()
    form = forms.ClockInOutForm()
    shift = Shift.objects.all()

    context = {
        'shift': shift,
        'users': users,
        'form': form,
        'title': 'Home'
    }

    return render(request, 'hoursCalc/index.html', context)


@login_required
def submitForm(request):  # mudar para

    if request.method == 'POST':
        form = forms.ClockInOutForm(request.POST)

        if form.is_valid():

            name = request.user

            new_clock_in = str(
                form.cleaned_data['date']) + ' ' + str(form.cleaned_data['clock_in'])
            new_clock_out = str(
                form.cleaned_data['date']) + ' ' + str(form.cleaned_data['clock_out'])

            clock_in_new = datetime.strptime(new_clock_in, '%Y-%m-%d %H:%M:%S')
            clock_out_new = datetime.strptime(
                new_clock_out, '%Y-%m-%d %H:%M:%S')

            Shift.objects.create(name=name,
                                 clock_in=clock_in_new,
                                 clock_out=clock_out_new,
                                 date=form.cleaned_data['date'],
                                 description=form.cleaned_data['description'])

    return redirect(index)


@login_required
def remove(request, pk):  # mudar remover
    post = get_object_or_404(Shift, pk=pk)

    user_post_id = post.name.id
    request_user_id = request.user.id

    if(user_post_id != request_user_id):
        messages.warning(request, f'você não poder deletar, porque não foi voce que o fez')
        return redirect(index)

    post.delete()
    messages.success(request, f'você removeu')
    return redirect(index)

#aqui tem um login requirido

# juntar selectDate com select_periods
def selectDate(request, dt="2000-01-01", df="2000-01-01"):

    users = User.objects.all()
    select_date_form = forms.SelectDateForm()
    shifts = Shift.objects.select_related('name').order_by('name')

    if request.method == 'POST':
        select_date_form = forms.SelectDateForm(request.POST)

        if select_date_form.is_valid():

            print("VALIDATION SUCCESS!")
            print("date_from: ", select_date_form.cleaned_data['date_from'])
            print("date_to: ", select_date_form.cleaned_data['date_to'])

            df = select_date_form.cleaned_data['date_from']
            dt = select_date_form.cleaned_data['date_to']

            shifts = Shift.objects.select_related('name').filter(
                date__gte=df, date__lte=dt).order_by('name')

    context = {
        'select_date_form': select_date_form,
        'users': users,
        'shifts': shifts,
        'title': 'Select Dates'
    }

    return render(request, 'hoursCalc/select.html', context)


#aqui tem um login requirido

def select_periods(request, date_from, date_to):  # filtrar as datas dos turnos 
    users = User.objects.all()
    objects = Shift.objects.filter(
        date__gte=date_from).filter(date__lte=date_to)

    context = {
        'users': users,
        'objects': objects,
        'title': 'Select Period'
    }

    return render(request, 'hoursCalc/select.html', context)


@login_required
def update_shift(request, pk):  # Atualiza o shift o turno

    shift_to_update = get_object_or_404(Shift, pk=pk)

    if request.method == 'POST':
        shift_form = forms.ShiftUpdateForm(request.POST)

        if shift_form.is_valid():

            new_clock_in = str(
                shift_form.cleaned_data['date']) + ' ' + str(shift_form.cleaned_data['clock_in'])
            new_clock_out = str(
                shift_form.cleaned_data['date']) + ' ' + str(shift_form.cleaned_data['clock_out'])

            clock_in_new = datetime.strptime(new_clock_in, '%Y-%m-%d %H:%M:%S')
            clock_out_new = datetime.strptime(
                new_clock_out, '%Y-%m-%d %H:%M:%S')

            shift_to_update.clock_in = clock_in_new
            shift_to_update.clock_out = clock_out_new
            shift_to_update.date = shift_form.cleaned_data['date']

            shift_to_update.save()

            messages.success(request, f'Turno atualizado')

            return redirect(index)

    else:
        shift_form = forms.ShiftUpdateForm(initial={'clock_in': shift_to_update.clock_in,
                                                    'clock_out': shift_to_update.clock_out,
                                                    'date': shift_to_update.date,
                                                
                                                    
                                                    'description': shift_to_update.description,
                                                    })

    context = {
        'shift_form': shift_form,
        'title': 'Update Shift'
    }

    return render(request, 'hoursCalc/update_shift.html', context)


def shift_detail(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    return render(request, 'hoursCalc/shift_detail.html', {'shift': shift})