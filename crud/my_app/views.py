from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Farmer_Form
from .forms import FarmerForm



def farmer_all(request):
    query = request.GET.get('q') 
    if query:
        forms = Farmer_Form.objects.filter(
            Q(farmer_name__icontains=query) |
            Q(f_crop__icontains=query) |
            Q(f_district__icontains=query) |
            Q(f_state__icontains=query)
        )
    else:
        forms = Farmer_Form.objects.all()

    return render(request, "home.html", {"forms": forms})



def add_farmer(request):
    if request.method == "POST":
        form = FarmerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_farmer')
    else:
        form = FarmerForm()

    return render(request, 'add.html', {"form": form})



def update_farmer(request, id):
    up_form = get_object_or_404(Farmer_Form, id=id)

    if request.method == "POST":
        form = FarmerForm(request.POST, instance=up_form)
        if form.is_valid():
            form.save()
            return redirect('all_farmer')
    else:
        form = FarmerForm(instance=up_form)

    return render(request, 'updates.html', {"form": form})



def delete_farmer(request, id):
    farmer = get_object_or_404(Farmer_Form, id=id)
    farmer.delete()
    return redirect('all_farmer')


def about(request):
    return render(request, 'about.html')
