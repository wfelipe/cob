from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from cob.dns.models import Domain
from django.contrib.auth.decorators import login_required

def domain_list(request):
	domains = Domain.objects.all ()
	return render_to_response('dns/domain_list.html', { 'domains': domains, })

def domain_detail(request, domain_id):
	domain = get_object_or_404(Domain, pk=domain_id)
	return render_to_response('dns/domain_detail.html', { 'domain': domain })
