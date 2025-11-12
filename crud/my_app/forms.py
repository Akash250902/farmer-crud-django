from django import forms
from .models import Farmer_Form

class FarmerForm(forms.ModelForm):
    class Meta:
        model=Farmer_Form
        fields=['farmer_id','farmer_name','f_state','f_district','f_age','f_contact','f_email','f_crop','f_quantity']