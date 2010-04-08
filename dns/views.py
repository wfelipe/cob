from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from cob.dns.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def domain_list(request):
	paginator = Paginator(Domain.objects.all(), 20)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		domains = paginator.page(page)
	except (EmptyPage, InvalidPage):
		domains = paginator.page(paginator.num_pages)
	return render_to_response('dns/domain_list.html', { 'domains': domains, })

def domain_detail(request, domain_id):
	domain = get_object_or_404(Domain, pk=domain_id)
	paginator = Paginator(Record.objects.filter(domain=domain), 20)

	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		records = paginator.page(page)
	except (EmptyPage, InvalidPage):
		records = paginator.page(paginator.num_pages)

	return render_to_response('dns/domain_detail.html',
		{ 'domain': domain,
		  'records': records,
		})
