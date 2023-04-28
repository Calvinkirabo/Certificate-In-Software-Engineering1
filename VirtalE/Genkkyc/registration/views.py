from django.shortcuts import render, redirect
from .models import info
from django.contrib import messages


# Create your views here.

def reg(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        state = request.POST.get('state')
        town = request.POST.get('town')
        z_code = request.POST.get('zip_code')
        number_1 = request.POST.get('p_num1')
        number_2 = request.POST.get('p_num2')
        email = request.POST.get('email')

        form = info(
        f_name=f_name,
        l_name=l_name,
        dob=dob,
        gender=gender,
        country=country,
        state=state,
        town=town,
        z_code=z_code,
        number_1=number_1,
        number_2=number_2,
        email= email
    )

        form.save()
        messages.success(request, 'data saved succesfully')
        return redirect('registration')
    else:
        messages.error(request, 'data not saved')
        return render(request, 'form.html', {})
