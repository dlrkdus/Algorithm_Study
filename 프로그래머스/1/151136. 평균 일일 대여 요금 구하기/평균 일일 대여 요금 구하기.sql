-- 코드를 입력하세요
SELECT ROUND(AVG(c.daily_fee)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR c
WHERE c.car_type = 'SUV'