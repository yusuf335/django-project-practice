from django import forms


from .models import Profile


class RemarksForm(forms.Form):
   def __init__(self, *args, **kwargs):
        CHOICES = (
            ('OK', 'OK'),
            ('NG', 'NG'),
        )
        my_list = []
        label = Profile.objects.all()
        print(label)
        for star in label.iterator():
            my_list.append(star.description)
            print(my_list)

        super(RemarksForm, self).__init__(*args, **kwargs)
        for i in my_list:
            self.fields[str(i)] = forms.ChoiceField(label=False,
                choices=CHOICES, widget=forms.RadioSelect())
