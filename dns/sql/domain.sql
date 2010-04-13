insert into dns_domain (name) values ('example.com');
insert into dns_serial (domain_id, serial, start_date, end_date) select id, 1, '1970-01-01 00:00:00', NOW() from dns_domain where name = 'example.com';
insert into dns_record (domain_id, name, fullname, type, content, ttl, prio, since_date, out_date) select id, 'test', 'test.example.com', 'A', '127.0.0.1', 3600, 0, '2010-01-01 00:00:00', '9999-12-31 23:59:59' from dns_domain where name = 'example.com';
insert into dns_domainserial (domain_id, serial_id) values (1, 1);
