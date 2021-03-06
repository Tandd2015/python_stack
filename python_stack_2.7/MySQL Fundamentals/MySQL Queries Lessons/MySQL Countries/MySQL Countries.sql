-- What query would you run to get all the countries that speak Slovene. Your query should return the name of the country, language and language percentage. You query should arrange the result by language percentage in descending order.
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene' ORDER BY languages.percentage DESC;

-- What query would you run to display the total number of cities for each country. Your query should return the name of the country and the total number of cities. You query should arrange the result by number of cities in descending order.
SELECT countries.name, count(cities.name) AS cities
FROM  countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id ORDER BY cities DESC;

-- What query would you run to get all the cities in Mexico with a population of greater than 500,000. Your query should arrange the result by population in descending order.
SELECT cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' ORDER BY cities.population DESC;

-- What query would you run to get all language in each country with a percentage greater than 89%. Your query should arrange the result by percentage in descending order.
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages on countries.id = languages.country_id
WHERE languages.percentage > 89.0 ORDER BY languages.percentage DESC;

-- What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000.
SELECT countries.name, countries.surface_area, countries.population 
FROM countries
WHERE countries.surface_area < 501.00 AND countries.population > 100000;

-- What query would you run to get all Constitutional Monarchy Countries with a capital greater than 200 and a life expectancy greater than 75 years.
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy > 75.0;

-- What query would you run to get all the cities of Argentina inside the Buenos Aires district and have population greater than 500, 000. The query should return the Country Name, City Name, District and Population.
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

-- What query would you run to summarize the number of countries in each region. The query should display the name of the region and the number of countries. Also, the query should arrange the result by number of countries in descending order.
SELECT countries.region, count(countries.id) AS countries
FROM countries
GROUP BY countries.region ORDER BY countries DESC;