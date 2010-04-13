from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from cob.dns.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def domain_list(request):
	paginator = Paginator(DomainSerial.objects.all(), 20)
	print DomainSerial.objects.all()
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		ds = paginator.page(page)
	except (EmptyPage, InvalidPage):
		ds = paginator.page(paginator.num_pages)
	return render_to_response('dns/domain_list.html', { 'domainserials': ds, })

def domain_detail(request, domain_id):
	domain = get_object_or_404(Domain, pk=domain_id)
	domainserial = DomainSerial.objects.get(domain=domain)
	records = Record.objects.filter(domain=domain)
	records = records.filter(out_date__gt = domainserial.serial.start_date)
	records = records.filter(since_date__lt = domainserial.serial.end_date)
	paginator = Paginator(records, 20)
	print records.query

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
