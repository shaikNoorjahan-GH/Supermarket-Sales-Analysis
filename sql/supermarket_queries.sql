-- ============================================
-- Project: Supermarket Sales Analysis
-- SQL Queries
-- ============================================




-- Question 1: What is the total revenue?

SELECT SUM(Sales) AS Total_Revenue FROM supermarket_sales;


-- Question 2: Which branch has the highest sales?

SELECT Branch, SUM(Sales) AS Total_Sales FROM supermarket_sales GROUP BY Branch ORDER BY Total_Sales DESC;


-- Question 3: Which product line is the most profitable?

SELECT `Product line`, SUM(`gross income`) AS Total_Profit FROM supermarket_sales GROUP BY `Product line` ORDER BY Total_Profit DESC;


-- Question 4: Which payment method is the most popular?

SELECT Payment, COUNT(*) AS Number_of_Transactions FROM supermarket_sales GROUP BY Payment ORDER BY Number_of_Transactions DESC;


-- Question 5: Which month has the highest sales?

SELECT Month, SUM(Sales) AS Total_Sales FROM supermarket_sales GROUP BY Month ORDER BY Total_Sales DESC;


-- Question 6: What is the average customer rating?

SELECT AVG(Rating) AS Average_Rating FROM supermarket_sales;


-- Question 7: What are the total sales by city?

SELECT City, SUM(Sales) AS Total_Sales FROM supermarket_sales GROUP BY City ORDER BY Total_Sales DESC;


-- Question 8: How many customer transactions are there?

SELECT COUNT(*) AS Total_Transactions FROM supermarket_sales;


-- Question 9: What is the average sale per transaction?

SELECT AVG(Sales) AS Average_Sale FROM supermarket_sales;


-- Question 10: Which city has the highest average customer rating?

SELECT City, AVG(Rating) AS Average_Rating FROM supermarket_sales GROUP BY City ORDER BY Average_Rating DESC;