from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import datetime
from django.db import transaction
from cob.dns.models import *
from cob.dns.utils import *
from cob.dns.forms import *

@login_required
def domain_list(request):
	paginator = Paginator(DomainSerial.objects.all(), 20)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		ds = paginator.page(page)
	except (EmptyPage, InvalidPage):
		ds = paginator.page(paginator.num_pages)
	return render_to_response('dns/domain_list.html', {
		'domainserials': ds,
		'total': paginator.count,
	})

@login_required
def domain_detail(request, domain_id):
	domain = get_object_or_404(Domain, pk=domain_id)
	serials = Serial.objects.filter(domain=domain)
	domainserial = DomainSerial.objects.get(domain=domain)
	records = Record.objects.filter(domain=domain)
	records = records.filter(out_date__gt = domainserial.serial.start_date)
	records = records.filter(since_date__lte = domainserial.serial.end_date)
	paginator = Paginator(records, 20)

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
		  'serials': serials,
		  'records': records,
		})

@login_required
def domain_compare(request):
	if request.method == 'POST':
		post = request.POST
		domain = get_object_or_404(Domain, name=post['domain'])
		# it should return 2 serials
		serials = Serial.objects.filter(domain=domain, serial__in=[post['serial1'], post['serial2']]).order_by('start_date')
		new_records = Record.objects.filter(domain=domain,
			since_date__gt = serials[0].end_date)
		rm_records = Record.objects.filter(domain=domain,
			out_date__lt = serials[1].end_date)
	else:
		print "error"

	return render_to_response('dns/domain_compare.html', {
		'domain': domain,
		'serials': serials,
		'new_records': new_records,
		'rm_records': rm_records,
	})

@login_required
@transaction.commit_on_success
def domain_new(request):
	msg = None
	domain = Domain()
	if request.method == 'POST':
		form = DomainForm(request.POST, instance=domain)
		if form.is_valid():
			form.save()
			msg = 'saved.'
		else:
			msg = 'not saved.'
	else:
		form = DomainForm()

	return render_to_response("dns/domain_new.html", {
		"form": form,
		"msg": msg,
	})
