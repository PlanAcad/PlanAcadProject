from django import forms  

class FechaCalendarioAcademicoUpdateForm(forms.ModelForm):
      
    class Meta:  
        year_fecha_desde = forms.IntegerField()
        month_fecha_desde = forms.IntegerField()
        day_fecha_desde = forms.IntegerField()
        year_fecha_hasta = forms.IntegerField()
        month_fecha_hasta = forms.IntegerField()
        day_fecha_hasta = forms.IntegerField()
        