from django import forms
from users.models import User

class UserForm(forms.ModelForm):

    class Meta:
        model=User
        fields=['first_name','phone_number','password']
        widgets={
            'phone_number':forms.NumberInput(attrs={"class": "form-control","placeholder":"Enter your phone number"}),
            'first_name':forms.TextInput(attrs={"class": "form-control","placeholder":"Enter your name"}),
            'password':forms.PasswordInput(attrs={"class": "form-control","placeholder":"Enter your password"})
        }

    def clean(self):
        cleaned_data=super().clean()
        phone_number=cleaned_data.get("phone_number")
        password=cleaned_data.get("password")

        if len(password)<=4:
                self.add_error("password","password must be at least 4 characters")
        if len(str(phone_number))<10:
                self.add_error("phone_number","Invalid phone number")
        if User.objects.filter(phone_number=phone_number).exists():
                self.add_error("phone_number","Phone number already exists")

                

        


    




