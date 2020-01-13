-- SELECT basics
-- 1.
SELECT world.population FROM world
  WHERE world.name = 'Germany';
-- 2.
SELECT world.name, world.population FROM world
  WHERE world.name IN ('Sweden', 'Norway', 'Denmark');
-- 3.
SELECT world.name, world.area FROM world
  WHERE world.area BETWEEN 200000 AND 250000;

-- SELECT from WORLD
-- 1.
SELECT world.name, world.continent, world.population FROM world;
-- 2.
SELECT world.name FROM world
WHERE world.population >= 200000000;
-- 3.
SELECT world.name, world.gdp/world.population AS 'capita GDP' FROM world
WHERE world.population >= 200000000;
-- 4.
SELECT world.name, world.population/1000000 AS 'population in millions' FROM world
WHERE world.continent = 'South America';
-- 5.
SELECT world.name, world.population FROM world
WHERE world.name IN ('France', 'Germany', 'Italy');
-- 6.
SELECT world.name FROM world
WHERE world.name LIKE 'United%';
-- 7.
SELECT world.name, world.population, world.area FROM world
WHERE world.population > 250000000 OR world.area > 3000000;
-- 8.
SELECT world.name, world.population, world.area FROM world
WHERE world.population > 250000000 XOR world.area > 3000000;
-- 9.
SELECT world.name, ROUND(world.population/1000000, 2) AS 'Population in Millions', 
ROUND(world.gdp/1000000000, 2) AS 'GDP in Billions' FROM world
WHERE world.continent = 'South America';
-- 10.
SELECT world.name, ROUND(world.gdp/world.population, -3) AS 'per-capita GDP' FROM world
WHERE world.gdp > 1000000000000;
-- 11.
SELECT world.name, world.capital FROM world
WHERE LENGTH(world.name) = LENGTH(world.capital);
-- 12.
SELECT world.name, world.capital FROM world
WHERE LEFT(world.name, 1) = LEFT(world.capital, 1) AND world.name <> world.capital;
-- 13.
SELECT world.name FROM world
WHERE world.name LIKE '%a%' 
AND world.name LIKE '%e%'
AND world.name LIKE '%i%'
AND world.name LIKE '%o%'
AND world.name LIKE '%u%'
AND world.name NOT LIKE '% %';

-- SELECT from NOBEL
-- 1.
SELECT nobel.yr, nobel.subject, nobel.winner
  FROM nobel
 WHERE nobel.yr = 1950;
-- 2.
SELECT nobel.winner
  FROM nobel
 WHERE nobel.yr = 1962
   AND nobel.subject = 'Literature';
-- 3.
SELECT nobel.yr, nobel.subject FROM nobel
WHERE nobel.winner = 'Albert Einstein';
-- 4.
SELECT nobel.winner FROM nobel
WHERE nobel.yr >= 2000 AND nobel.subject = 'Peace';
-- 5.
SELECT * FROM nobel
WHERE nobel.subject = 'Literature'
AND nobel.yr IN (1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989);
-- 6.
SELECT * FROM nobel
WHERE nobel.winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter', 'Barack Obama');
-- 7.
SELECT nobel.winner FROM nobel
WHERE nobel.winner LIKE 'John%';
-- 8.
SELECT nobel.yr, nobel.subject, nobel.winner FROM nobel
WHERE nobel.yr = 1980 AND nobel.subject = 'Physics' XOR nobel.yr = 1984 AND nobel.subject = 'Chemistry';
-- 9.
SELECT nobel.yr, nobel.subject, nobel.winner FROM nobel
WHERE nobel.yr = 1980 AND nobel.subject NOT IN ('Chemistry', 'Medicine');
-- 10.
SELECT nobel.yr, nobel.subject, nobel.winner FROM nobel
WHERE nobel.subject = 'Medicine' AND nobel.yr < 1910 XOR nobel.subject = 'Literature' AND nobel.yr >= 2004; 
-- 11.
SELECT * FROM nobel
WHERE nobel.winner = 'PETER GRÜNBERG';
-- 12.
SELECT * FROM nobel
WHERE nobel.winner = 'EUGENE O''NEILL';
-- 13.
SELECT nobel.winner, nobel.yr, nobel.subject FROM nobel
WHERE nobel.winner LIKE 'Sir%'
ORDER BY nobel.yr DESC;
-- 14.
SELECT nobel.winner, nobel.subject FROM nobel
WHERE nobel.yr = 1984
ORDER BY nobel.subject IN ('Chemistry', 'Physics'), nobel.subject, nobel.winner;

-- SELECT within SELECT Tutorial
-- 1.
SELECT world.name FROM world
  WHERE world.population >
     (SELECT world.population FROM world
      WHERE world.name='Russia');
-- 2.
SELECT world.name FROM world
WHERE world.continent = 'Europe' AND world.gdp/world.population >(SELECT world.gdp/world.population FROM world
WHERE world.name = 'United Kingdom');
-- 3.
SELECT world.name, world.continent FROM world
WHERE world.continent IN (SELECT world.continent FROM world
WHERE world.name IN ('Argentina', 'Australia')) ORDER BY world.name;
-- 4.
SELECT world.name, world.population FROM world
WHERE world.population > (SELECT world.population FROM world
WHERE world.name = 'Canada') AND world.population < (SELECT world.population FROM world
WHERE world.name = 'Poland');
-- 5.
SELECT world.name, CONCAT(ROUND(100*world.population/(SELECT world.population FROM world
WHERE world.name = 'Germany')), '%') FROM world
WHERE world.continent = 'Europe';
-- 6.
