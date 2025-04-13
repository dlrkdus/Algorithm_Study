-- 코드를 입력하세요
SELECT a.author_id, a.author_name, b.category, SUM(PRICE * SALES) AS TOTAL_SALES
FROM Book b 
JOIN AUTHOR a ON b.author_id = a.author_id
JOIN BOOK_SALES s 
ON b.book_id = s.book_id
WHERE YEAR(s.sales_date) = 2022 AND MONTH(s.sales_date) = 1
GROUP BY a.author_id, b.category
ORDER BY a.author_id, b.category DESC;
