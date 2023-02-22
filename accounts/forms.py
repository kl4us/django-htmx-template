from django import forms
from registration.forms import RegistrationFormTermsOfService, RegistrationFormUniqueEmail

class CustomRegistrationForm(RegistrationFormUniqueEmail):
    pass