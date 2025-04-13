-- 코드를 입력하세요
SELECT c.car_type, COUNT(c.car_type) AS CARS
FROM CAR_RENTAL_COMPANY_CAR c
WHERE c.options LIKE '%통풍시트%'
OR c.options LIKE '%열선시트%'
OR c.options LIKE '%가죽시트%'
GROUP BY c.car_type
ORDER BY c.car_type;