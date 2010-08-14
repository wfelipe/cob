from django.forms import ModelForm
from dns.models import *

class DomainForm(ModelForm):
	class Meta:
		model = Domain
