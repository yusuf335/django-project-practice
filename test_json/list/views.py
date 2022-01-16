from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect


from .models import ProfileJson
from .forms import  RemarksForm


# Create your views here.


def profile(request):
    if request.method == 'POST':
        form = RemarksForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            json = form.cleaned_data
            ProfileJson.objects.create(profile_json = json)
            return HttpResponseRedirect("/")
    
    form = RemarksForm()

    return render(request, 'list/form.html', {
        'form': form
    })


class ListView(ListView):
    template_name = "list/client.html"
    model = ProfileJson
    context_object_name = "list_view"

    



    
