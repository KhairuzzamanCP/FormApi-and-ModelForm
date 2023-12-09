from django.shortcuts import render
from first_app.forms import StudentsForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentsForm()
               
    return render(request, 'home.html', {'form':form})