from django import forms
from .models import StudentModel

class StudentsForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels ={
            'name': 'Student Name',
            'roll': 'Student Roll'
            
        }
        widgets ={
        'name': forms.TextInput()
        
        } 
        
        help_texts = {
            'name':'Full naeme'
        }
        
        
    