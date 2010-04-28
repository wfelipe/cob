from django.forms import ModelForm
from cob.dns.models import *

class DomainForm(ModelForm):
	class Meta:
		model = Domain
