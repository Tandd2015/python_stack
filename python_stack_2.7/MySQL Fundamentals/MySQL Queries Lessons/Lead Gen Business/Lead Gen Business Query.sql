-- What query would you run to get the total revenue for March of 2012?
SELECT MONTHNAME(billing.charged_datetime) AS 'month', SUM(billing.amount) AS 'revenue'
FROM billing
WHERE MONTHNAME(billing.charged_datetime) = 'March' AND DATE_FORMAT(billing.charged_datetime, '%Y') = 2012
GROUP BY  MONTHNAME(billing.charged_datetime), YEAR(billing.charged_datetime) ORDER BY 'month';

-- What query would you run to get total revenue collected from the client with an id of 2?
SELECT billing.client_id, SUM(billing.amount) AS 'total_revenue'
FROM billing
WHERE billing.client_id = 2
GROUP BY billing.client_id ORDER BY 'total_revenue';

-- What query would you run to get all the sites that client = 10 owns?
SELECT sites.domain_name AS 'website', sites.client_id
FROM sites
WHERE sites.client_id = 10
GROUP BY sites.domain_name ORDER BY sites.client_id;

-- What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?
SELECT sites.client_id, COUNT(sites.site_id) AS 'number_of_websites', MONTHNAME(sites.created_datetime) AS 'month_created', DATE_FORMAT(sites.created_datetime, '%Y') AS 'year_created'
FROM sites
WHERE sites.client_id = 1
GROUP BY month_created, year_created ORDER BY sites.client_id;

SELECT sites.client_id, COUNT(sites.site_id) AS 'number_of_websites', DATE_FORMAT(sites.created_datetime, '%M') AS 'month_created', YEAR(sites.created_datetime) AS 'year_created'
FROM sites
WHERE sites.client_id = 20
GROUP BY month_created, year_created ORDER BY sites.client_id;

-- What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name AS 'website', COUNT(leads.leads_id) AS 'number_of_leads', DATE_FORMAT(ANY_VALUE(leads.registered_datetime), '%M %d, %Y') AS 'date_generated'
FROM sites
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY sites.site_id;

-- What query would you run to get a list of client name and the total # of leads we have generated for each of our client between January 1st 2011 to December 31st 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'client_name', COUNT(leads.leads_id) AS 'number_of_leads'
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id ORDER BY sites.client_id;

-- What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'client_name', COUNT(leads.leads_id) AS 'number_of_leads', DATE_FORMAT(ANY_VALUE(leads.registered_datetime), '%M') AS 'month_generated'
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON leads.site_id = sites.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY clients.client_id, DATE_FORMAT(ANY_VALUE(leads.registered_datetime), '%M') ORDER BY DATE_FORMAT(ANY_VALUE(leads.registered_datetime), '%m');

-- What query would you run to get a list of client name and the total # of leads we have generated for each of our clients site between January 1st 2011 to December 31st 2011? Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time?
SELECT CONCAT(ANY_VALUE(clients.first_name), ' ', ANY_VALUE(clients.last_name)) AS 'client_name', sites.domain_name AS 'website', COUNT(leads.leads_id) AS 'number_of_leads', DATE_FORMAT(ANY_VALUE(leads.registered_datetime), '%M %d, %Y') AS 'date_generated'
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY website ORDER BY clients.client_id;

SELECT CONCAT(ANY_VALUE(clients.first_name), ' ', ANY_VALUE(clients.last_name)) AS 'client_name', sites.domain_name AS 'website', COUNT(leads.leads_id) AS 'number_of_leads'
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
LEFT JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, website ORDER BY clients.client_id;

-- Write a single query that retrieves total revenue collected from each client each month of the year?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'client_name', SUM(billing.amount) AS 'Total_Revenue', DATE_FORMAT(billing.charged_datetime, '%M') AS 'month_charge', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'year_charge'
FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_name, DATE_FORMAT(billing.charged_datetime, '%M'), DATE_FORMAT(billing.charged_datetime, '%Y') ORDER BY clients.client_id;

-- Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client and have a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS 'client_name', GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') AS 'sites'
FROM clients
LEFT JOIN sites ON  clients.client_id = sites.client_id
GROUP BY clients.client_id;



