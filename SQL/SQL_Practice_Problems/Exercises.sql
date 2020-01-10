USE Northwind_SPP

SET 

-- Q1: We have a table called Shippers. Return all the fields from all the shippers

SELECT TOP 3 *
FROM Shippers


-- In the Categories table, selecting all the fields using this SQL:
-- Select * from Categories …will return 4 columns. We only want to see two columns, CategoryName and Description.

SELECT CategoryName, Description
FROM Categories

--3. Sales Representatives
--We’d like to see just the FirstName, LastName, and HireDate of all the employees with the
--Title of Sales Representative. Write a SQL statement that returns only those employees.

SELECT FirstName, LastName, HireDate
FROM Employees
WHERE TITLE LIKE 'Sales Representative'


--4. Sales Representatives in the United States
--Now we’d like to see the same columns as above, but only for those employees that both have
--the title of Sales Representative, and also are in the United States.

SELECT FirstName, LastName, HireDate
FROM Employees
WHERE TITLE LIKE 'Sales Representative' and Country LIKE 'USA'

--5. Orders placed by specific EmployeeID
--Show all the orders placed by a specific employee. The EmployeeID for this Employee (Steven
--Buchanan) is 5.

SELECT *
FROM Orders
WHERE EmployeeID = 5

--6. Suppliers and ContactTitles
--In the Suppliers table, show the SupplierID, ContactName, and ContactTitle for those
--Suppliers whose ContactTitle is not Marketing Manager.

SELECT SupplierID, ContactName, ContactTitle
FROM Suppliers
WHERE ContactTitle NOT LIKE 'Marketing Manager'

--13. OrderDetails amount per line item
--In the OrderDetails table, we have the fields UnitPrice and Quantity. Create a new field,
--TotalPrice, that multiplies these two together. We’ll ignore the Discount field for now.
--In addition, show the OrderID, ProductID, UnitPrice, and Quantity. Order by OrderID and
--ProductID.

SELECT OrderID, ProductID, UnitPrice, Quantity, Discount, (UnitPrice * Quantity) AS TotalPrice
FROM OrderDetails
GO

--14. How many customers?
--How many customers do we have in the Customers table? Show one value only, and don’t rely
--on getting the record count at the end of a resultset.

SELECT COUNT(CustomerID) AS Number_Customers
FROM Customers
GO

--15. When was the first order?
--Show the date of the first order ever made in the Orders table.

SELECT TOP 1 OrderDate
FROM Orders
ORDER BY OrderDate ASC
GO

--17. Contact titles for customers
--Show a list of all the different values in the Customers table for ContactTitles. Also include a
--count for each ContactTitle.
--This is similar in concept to the previous question “Countries where there are customers”,
--except we now want a count for each ContactTitle

SELECT ContactTitle, COUNT(CustomerID) AS TotalContactTitle
FROM Customers
GROUP BY ContactTitle

--18. Products with associated supplier names
--We’d like to show, for each product, the associated Supplier. Show the ProductID,
--ProductName, and the CompanyName of the Supplier.

SELECT ProductID, ProductName, CompanyName
FROM Products AS P INNER JOIN Suppliers AS S ON (
	P.SupplierID = S.SupplierID
)

--20. Categories, and the total products in each category
--For this problem, we’d like to see the total number of products in each category. Sort the
--results by the total number of products, in descending order.

SELECT CategoryName, COUNT(ProductID) AS TotalProducts
FROM Products P JOIN Categories C ON (
	P.CategoryID = C.CategoryID
)
GROUP BY CategoryName
ORDER BY TotalProducts DESC

--21. Total customers per country/city
--In the Customers table, show the total number of customers per Country and City.

SELECT Country, City, COUNT(CustomerID) AS TotalCustomers
FROM Customers
GROUP BY Country, City
ORDER BY TotalCustomers DESC

--23. Products that need reordering, continued
--Now we need to incorporate these fields—UnitsInStock, UnitsOnOrder, ReorderLevel,
--Discontinued—into our calculation. We’ll define “products that need reordering” with the
--following:
--• UnitsInStock plus UnitsOnOrder are less than or equal to ReorderLevel
--• The Discontinued flag is false (0).

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
FROM Products
WHERE UnitsInStock + UnitsOnOrder <= ReorderLevel AND Discontinued = 0
GO

--24. Customer list by region
--A salesperson for Northwind is going on a business trip to visit customers, and would like to
--see a list of all customers, sorted by region, alphabetically.29
--However, he wants the customers with no region (null in the Region field) to be at the end,
--instead of at the top, where you’d normally find the null values. Within the same region,
--companies should be sorted by CustomerID.

SELECT CustomerID, CompanyName, Region
FROM Customers
ORDER BY CASE WHEN Region is NULL THEN 1 ELSE 0 END, Region ASC
GO

--25. High freight charges
--Some of the countries we ship to have very high freight charges. We'd like to investigate some
--more shipping options for our customers, to be able to offer them lower freight charges. Return
--the three ship countries with the highest average freight overall, in descending order by
--average freight.

SELECT TOP 3 ShipCountry, AVG(Freight) AS AverageFreight
FROM Orders
GROUP BY ShipCountry
ORDER BY AverageFreight DESC;

--26. High freight charges—2015
--We're continuing on the question above on high freight charges. Now, instead of using all the
--orders we have, we only want to see orders from the year 2015.

SELECT TOP 3 ShipCountry, AVG(Freight) AS AverageFreight
FROM Orders
WHERE YEAR(OrderDate) = 2015
GROUP BY ShipCountry
ORDER BY AverageFreight DESC;


--27. High freight charges with between
--Another (incorrect) answer to the problem above is this:
--Select Top 3
--ShipCountry
--,AverageFreight = avg(freight)
--From Orders
--Where
--OrderDate between '20150101' and '20151231'
--Group By ShipCountry
--Order By AverageFreight desc
--Notice when you run this, it gives Sweden as the ShipCountry with the third highest freight
--charges. However, this is wrong—it should be France.
--What is the OrderID of the order that the (incorrect) answer above is missing?

--The BETWEEN operator is inclusive.
--From Books Online:
--BETWEEN returns TRUE if the value of test_expression is greater than or equal to the value of begin_expression and less than or equal to the value of end_expression.

--DateTime Caveat
--NB: With DateTimes you have to be careful; if only a date is given the value is taken as of midnight on that day; to avoid missing times within your end date, or repeating the capture of the following day's data at midnight in multiple ranges, 
--your end date should be 3 milliseconds before midnight on of day following your to date. 3 milliseconds because any less than this and the value will be rounded up to midnight the next day.
--e.g. to get all values within June 2016 you'd need to run:
--where myDateTime between '20160601' and DATEADD(millisecond, -3, '20160701')

--i.e.
--where myDateTime between '20160601 00:00:00.000' and '20160630 23:59:59.997'


SELECT *
FROM Orders
WHERE OrderID IN
(
	SELECT OrderID
	FROM Orders
	WHERE YEAR(OrderDate) = 2015
	EXCEPT
	Select OrderID
	From Orders
	Where OrderDate between '20150101' and '20151231'
)


--28. High freight charges—last year
--We're continuing to work on high freight charges. We now want to get the three ship countries
--with the highest average freight charges. But instead of filtering for a particular year, we want
--to use the last 12 months of order data, using as the end date the last OrderDate in Orders.

SELECT TOP 3 ShipCountry, AVG(Freight) AS AverageFreight
FROM Orders
WHERE DATEDIFF(month, OrderDate, (SELECT MAX(OrderDate) FROM Orders)) <= 12
GROUP BY ShipCountry
ORDER BY AverageFreight DESC


--30. Customers with no orders
--There are some customers who have never actually placed an order. Show these customers.33
--Expected Results
--Customers_CustomerID Orders_CustomerID
--FISSA NULL
--PARIS NULL

SELECT CustomerID 
FROM Customers
EXCEPT
SELECT CustomerID
FROM Orders

--31. Customers with no orders for EmployeeID 4
--One employee (Margaret Peacock, EmployeeID 4) has placed the most orders. However, there
--are some customers who've never placed an order with her. Show only those customers who
--have never placed an order with her.

SELECT CustomerID 
FROM Customers
EXCEPT
SELECT CustomerID
FROM Orders
WHERE EmployeeID = 4

--32. High-value customers
--We want to send all of our high-value customers a special VIP gift. We're defining high-value
--customers as those who've made at least 1 order with a total value (not including the discount)
--equal to $10,000 or more. We only want to consider orders made in the year 2016.

SELECT C.CustomerID, CompanyName, O.OrderID, TotalOrderAmount
FROM Customers AS C JOIN Orders AS O ON (
	C.CustomerID = O.CustomerID
) JOIN 
(
	SELECT O.OrderID, SUM(UnitPrice * Quantity) AS TotalOrderAmount
	FROM Orders AS O JOIN OrderDetails AS D ON (
		O.OrderID = D.OrderID
	)
	WHERE YEAR(OrderDate) = 2016
	GROUP BY O.OrderID
	HAVING SUM(UnitPrice * Quantity) > 10000
) temp ON O.OrderID = temp.OrderID
ORDER BY TotalOrderAmount DESC;

--33. High-value customers—total orders
--The manager has changed his mind. Instead of requiring that customers have at least one
--individual orders totaling $10,000 or more, he wants to define high-value customers as those
--who have orders totaling $15,000 or more in 2016. How would you change the answer to the
--problem above?

SELECT C.CustomerID, CompanyName, TotalOrderAmount
FROM Customers AS C JOIN 
(
	SELECT CustomerID, SUM(UnitPrice * Quantity) AS TotalOrderAmount
	FROM Orders AS O JOIN OrderDetails AS D ON (
		O.OrderID = D.OrderID
	)
	WHERE YEAR(OrderDate) = 2016
	GROUP BY CustomerID
	HAVING SUM(UnitPrice * Quantity) > 15000
) temp ON C.CustomerID = temp.CustomerID
ORDER BY TotalOrderAmount DESC;

--34. High-value customers—with discount
--Change the above query to use the discount when calculating high-value customers. Order by
--the total amount which includes the discount

SELECT C.CustomerID, CompanyName, TotalOrderAmount
FROM Customers AS C JOIN 
(
	SELECT CustomerID, SUM(UnitPrice * Quantity * (1-Discount)) AS TotalOrderAmount
	FROM Orders AS O JOIN OrderDetails AS D ON (
		O.OrderID = D.OrderID
	)
	WHERE YEAR(OrderDate) = 2016
	GROUP BY CustomerID
	HAVING SUM(UnitPrice * Quantity * (1-Discount)) > 10000
) temp ON C.CustomerID = temp.CustomerID
ORDER BY TotalOrderAmount DESC;

--35. Month-end orders
--At the end of the month, salespeople are likely to try much harder to get orders, to meet their
--month-end quotas. Show all orders made on the last day of the month. Order by EmployeeID
--and OrderID

SELECT DISTINCT O2.EmployeeID, O2.OrderID, O2.OrderDate
FROM Orders O1 JOIN Orders O2 ON (
	MONTH(DATEADD(day, 1, O2.OrderDate)) - MONTH(O1.OrderDate) = 1 OR
	MONTH(DATEADD(day, 1, O2.OrderDate)) - MONTH(O1.OrderDate) < 0
)
WHERE DATEDIFF(day, O1.OrderDate, DATEADD(day, 1, O2.OrderDate)) = 1
ORDER BY O2.EmployeeID, O2.OrderID;

SELECT EmployeeID, OrderID, OrderDate
FROM Orders 
WHERE DATEDIFF(day, OrderDate, EOMONTH(OrderDate)) = 0
ORDER BY EmployeeID, OrderID;


--36. Orders with many line items
--The Northwind mobile app developers are testing an app that customers will use to show
--orders. In order to make sure that even the largest orders will show up correctly on the app,
--they'd like some samples of orders that have lots of individual line items.
--Show the 10 orders with the most line items, in order of total line items.

SELECT TOP 10 OrderID, Count(DISTINCT ProductID) AS TotalOrderDetails
FROM OrderDetails
GROUP BY OrderID
ORDER BY TotalOrderDetails DESC


--37. Orders—random assortment
--The Northwind mobile app developers would now like to just get a random assortment of
--orders for beta testing on their app. Show a random set of 2% of all orders.

select  * 
from Orders 
where OrderID in 
(select top 2 percent OrderID from Orders order by newid())

--38. Orders—accidental double-entry
--Janet Leverling, one of the salespeople, has come to you with a request. She thinks that she
--accidentally entered a line item twice on an order, each time with a different ProductID, but the
--same quantity. She remembers that the quantity was 60 or more. Show all the OrderIDs with
--line items that match this, in order of OrderID.

SELECT OrderID
FROM OrderDetails 
WHERE Quantity >= 60
GROUP BY OrderID, Quantity
HAVING COUNT(*) = 2

--39. Orders—accidental double-entry details
--Based on the previous question, we now want to show details of the order, for orders that
--match the above criteria.

SELECT OrderID, ProductID, UnitPrice, Quantity, Discount
FROM OrderDetails
WHERE OrderID IN
(
	SELECT OrderID
	FROM OrderDetails 
	WHERE Quantity >= 60
	GROUP BY OrderID, Quantity
	HAVING COUNT(*) = 2
)


--40. Orders—accidental double-entry details, derived table
--Here's another way of getting the same results as in the previous problem, using a derived table instead of a CTE. However, there's a bug in this SQL. It returns 20 rows instead of 16. Correct the SQL.
--Problem SQL: 
Select OrderDetails.OrderID ,ProductID ,UnitPrice ,Quantity ,Discount 
From OrderDetails Join 
( 
	Select OrderID 
	From OrderDetails 
	Where Quantity >= 60 
	Group By OrderID, Quantity 
	Having Count(*) = 2 
) PotentialProblemOrders on PotentialProblemOrders.OrderID = OrderDetails.OrderID 
Order by OrderID, ProductID

-- Correct
Select OrderDetails.OrderID ,ProductID ,UnitPrice ,Quantity ,Discount 
From OrderDetails Join 
( 
	Select DISTINCT OrderID 
	From OrderDetails 
	Where Quantity >= 60 
	Group By OrderID, Quantity 
	Having Count(*) = 2 
) PotentialProblemOrders on PotentialProblemOrders.OrderID = OrderDetails.OrderID 
Order by OrderID, ProductID


--41. Late orders
--Some customers are complaining about their orders arriving late. Which orders are late? Sort the results by OrderID.

SELECT OrderID, OrderDate, RequiredDate, ShippedDate
FROM Orders
WHERE RequiredDate <= ShippedDate
ORDER BY OrderID

--42. Late orders—which employees?
--Some salespeople have more orders arriving late than others. Maybe they're not following up on the order process, and need more training. 
-- Which salespeople have the most orders arriving late?


SELECT E.EmployeeID,LastName, TotalLateOrders
FROM Employees E JOIN ( 
	SELECT EmployeeID, COUNT(OrderID) AS TotalLateOrders
	FROM Orders
	WHERE RequiredDate <= ShippedDate
	GROUP BY EmployeeID
) temp
ON (
	temp.EmployeeID = E.EmployeeID
)
ORDER BY TotalLateOrders DESC

--43. Late orders vs. total orders
--Andrew, the VP of sales, has been doing some more thinking some more about the problem of late orders. 
--He realizes that just looking at the number of orders arriving late for each salesperson isn't a good idea. 
--It needs to be compared against the total number of orders per salesperson.

With AllOrders AS (
	SELECT EmployeeID, COUNT(OrderID) AS TotalOrders
	FROM Orders
	GROUP BY EmployeeID

), LateOrders AS (
	SELECT EmployeeID, COUNT(OrderID) AS TotalLateOrders
	FROM Orders
	WHERE RequiredDate <= ShippedDate
	GROUP BY EmployeeID
)
SELECT E.EmployeeID, LastName, TotalOrders, TotalLateOrders
FROM Employees E JOIN AllOrders A ON (
	E.EmployeeID = A.EmployeeID
) JOIN LateOrders L ON (
	E.EmployeeID = L.EmployeeID
)
ORDER BY E.EmployeeID

--44/45/46/47. Late orders vs. total orders—missing employee
--There's an employee missing in the answer from the problem above. 
--Fix the SQL to show all employees who have taken orders.

With AllOrders AS (
	SELECT EmployeeID, COUNT(OrderID) AS TotalOrders
	FROM Orders
	GROUP BY EmployeeID

), LateOrders AS (
	SELECT EmployeeID, COUNT(OrderID) AS TotalLateOrders
	FROM Orders
	WHERE RequiredDate <= ShippedDate
	GROUP BY EmployeeID
)
SELECT E.EmployeeID, LastName, TotalOrders, 
CASE WHEN TotalLateOrders IS NULL THEN 0 ELSE TotalLateOrders END AS TotalLateOrders,
CONVERT(DECIMAL(10,2),ROUND(CASE WHEN TotalLateOrders IS NULL THEN 0 ELSE TotalLateOrders * 1.0 / TotalOrders END, 2)) AS PercentLateOrders
FROM Employees E LEFT JOIN AllOrders A ON (
	E.EmployeeID = A.EmployeeID
) LEFT JOIN LateOrders L ON (
	E.EmployeeID = L.EmployeeID
)
ORDER BY E.EmployeeID

--48. Customer grouping
--Andrew Fuller, the VP of sales at Northwind, would like to do a sales campaign for existing customers. 
--He'd like to categorize customers into groups, based on how much they ordered in 2016. 
--Then, depending on which group the customer is in, he will target the customer with different sales materials.
--The customer grouping categories are 0 to 1,000, 1,000 to 5,000, 5,000 to 10,000, and over 10,000. 
--So, if the total dollar amount of the customer’s purchases in that year were between 0 to 1,000, they would be in the “Low” group. 
--A customer with purchase from 1,000 to 5,000 would be in the “Medium” group, and so on.
--A good starting point for this query is the answer from the problem “High-value customers—total orders”. 
--Also, we only want to show customers who have ordered in 2016.
--Order the results by CustomerID.

WITH OrderTotal AS (
	SELECT CustomerID, SUM(UnitPrice*Quantity) AS TotalAmount
	FROM Orders O JOIN OrderDetails D ON (
		O.OrderID = D.OrderID
	)
	WHERE YEAR(OrderDate) = 2016
	GROUP BY CustomerID
)
SELECT O.CustomerID, CompanyName, O.TotalAmount, CustomerGroupName
FROM OrderTotal O LEFT JOIN CustomerGroupThresholds ON (
	TotalAmount >= RangeBottom AND TotalAmount <= RangeTop
) JOIN Customers C ON (
	O.CustomerID = C.CustomerID
)
ORDER BY CustomerID;

--50/51. Customer grouping with percentage
--Based on the above query, show all the defined CustomerGroups, 
--and the percentage in each. Sort by the total in each group, in descending order.

WITH OrderTotal AS (
	SELECT CustomerID, SUM(UnitPrice*Quantity) AS TotalAmount
	FROM Orders O JOIN OrderDetails D ON (
		O.OrderID = D.OrderID
	)
	WHERE YEAR(OrderDate) = 2016
	GROUP BY CustomerID
)
SELECT CustomerGroupName, COUNT(C.CustomerID) AS TotalInGroup, COUNT(C.CustomerID) * 1.0/(SELECT COUNT(*) FROM OrderTotal) AS PercentageInGroup
FROM OrderTotal O LEFT JOIN CustomerGroupThresholds ON (
	TotalAmount >= RangeBottom AND TotalAmount <= RangeTop
) JOIN Customers C ON (
	O.CustomerID = C.CustomerID
)
GROUP BY CustomerGroupName

--52. Countries with suppliers or customers
--Some Northwind employees are planning a business trip, and would like to visit as many suppliers and customers as possible. 
--For their planning, they’d like to see a list of all countries where suppliers and/or customers are based.

SELECT DISTINCT Country
FROM Customers
UNION
SELECT DISTINCT Country
FROM Suppliers
ORDER BY Country

--53. Countries with suppliers or customers, version 2
--The employees going on the business trip don’t want just a raw list of countries, they want more details. 
--We’d like to see output like the below, in the Expected Results.

SELECT SupplierCountry, CustomerCountry
FROM 
(
	SELECT DISTINCT Country AS CustomerCountry
	FROM Customers
) C FULL OUTER JOIN (
	SELECT DISTINCT Country AS SupplierCountry
	FROM Suppliers
) S ON (
	SupplierCountry = CustomerCountry
)

--54. Countries with suppliers or customers, version 3
--The output in the above practice problem is improved, but it’s still not ideal
--What we’d really like to see is the country name, the total suppliers, and the total customers.

SELECT CASE 
WHEN SupplierCountry IS NULL AND CustomerCountry IS NOT NULL THEN CustomerCountry 
WHEN CustomerCountry IS NULL AND SupplierCountry IS NOT NULL THEN SupplierCountry 
WHEN CustomerCountry IS NOT NULL AND SupplierCountry IS NOT NULL THEN CustomerCountry
END AS Country, 
ISNULL(TotalSuppliers, 0) AS TotalSuppliers, ISNULL(TotalCustomers, 0) AS TotalCustomers
FROM 
(
	SELECT Country AS CustomerCountry, COUNT(CustomerID) AS TotalCustomers
	FROM Customers
	GROUP BY Country
) C FULL OUTER JOIN (
	SELECT Country AS SupplierCountry, COUNT(SupplierID) AS TotalSuppliers
	FROM Suppliers
	GROUP BY Country
) S ON (
	SupplierCountry = CustomerCountry
)

--55. First order in each country
--Looking at the Orders table—we’d like to show details for each order that was the first in that
--particular country, ordered by OrderID.
--So, for each country, we want one row. That row should contain the earliest order for that
--country, with the associated ShipCountry, CustomerID, OrderID, and OrderDate.

WITH OrderRankbyDate AS (
	SELECT OrderID, CustomerID, ShipCountry, OrderDate, 
	RANK() OVER (PARTITION BY ShipCountry ORDER BY OrderDate, OrderID ASC) AS OrderRank
	FROM Orders 
)
SELECT OrderID, CustomerID, ShipCountry, OrderDate
FROM OrderRankbyDate
WHERE OrderRank = 1


--56. Customers with multiple orders in 5 day period
--There are some customers for whom freight is a major expense when ordering from
--Northwind.
--However, by batching up their orders, and making one larger order instead of multiple smaller
--orders in a short period of time, they could reduce their freight costs significantly.
--Show those customers who have made more than 1 order in a 5 day period. The sales people
--will use this to help customers reduce their freight costs.
--Note: There are more than one way of solving this kind of problem. For this problem, we will
--not be using Window functions.

WITH OrderIn5Days AS (
	SELECT O1.CustomerID, O1.OrderID AS InitialOrderID, O1.OrderDate AS InitialOrderDate,
	O2.OrderID AS NextOrderID, O2.OrderDate AS NextOrderDate, DATEDIFF(DAY, O1.OrderDate, O2.OrderDate) AS DaysBetweenOrders 
	FROM Orders O1 JOIN Orders O2 ON (
		O1.CustomerID = O2.CustomerID AND
		DATEDIFF(DAY, O1.OrderDate, O2.OrderDate) <= 5 AND
		O1.OrderDate <= O2.OrderDate AND 
		O1.OrderID <> O2.OrderID
	)
), FirstOrder AS (
	SELECT CustomerID, InitialOrderDate, MIN(NextOrderDate) AS ClosestOrderDate
	FROM OrderIn5Days
	GROUP BY CustomerID, InitialOrderDate
)
SELECT O.CustomerID, InitialOrderID, O.InitialOrderDate, NextOrderID, NextOrderDate, DaysBetweenOrders
FROM OrderIn5Days O JOIN FirstOrder F ON
(
	O.CustomerID = F.CustomerID AND
	O.InitialOrderDate = F.InitialOrderDate AND
	NextOrderDate = ClosestOrderDate
)
ORDER BY O.CustomerID, O.InitialOrderDate;

--57. Customers with multiple orders in 5 day period, version 2
--There’s another way of solving the problem above, using Window functions. We would like to
--see the following results.

WITH NextOrderDate AS (
	SELECT CustomerID, OrderID AS InitialOrderID, OrderDate AS InitialOrderDate, 
	(LEAD(OrderID, 1) OVER (PARTITION BY CustomerID ORDER BY OrderDate)) AS NextOrderID,
	(LEAD(OrderDate, 1) OVER (PARTITION BY CustomerID ORDER BY OrderDate)) AS NextOrderDate
	FROM Orders
)
SELECT *
FROM NextOrderDate
Where DateDiff (dd, InitialOrderDate, NextOrderDate) <= 5


------------------ More Problems --------------------------

--1. Cost changes for each product
--There's a table called ProductCostHistory which contains the history of the cost of the product.
--Using that table, get the total number of times the product cost has changed.
--Sort the results by ProductID

SELECT ProductID, COUNT(DISTINCT StandardCost) AS TotalPriceChanges
FROM ProductCostHistory
GROUP BY ProductID

--2. Customers with total orders placed
--We want to see a list of all the customers that have made orders, and the total number of orders
--the customer has made.
--Sort by the total number of orders, in descending order

SELECT CustomerID, COUNT(DISTINCT [SalesOrderID]) AS TotalOrders
FROM [dbo].[SalesOrderHeader]
GROUP BY CustomerID
ORDER BY TotalOrders DESC

--3. Products with first and last order date
--For each product that was ordered, show the first and last date that it was ordered.
--In the previous problem I gave you the table name to use. For this problem, look at the list of
--tables, and figure out which ones you need to use.
--Sort the results by ProductID.

SELECT ProductID, CONVERT(DATE, MIN(OrderDate)) AS FirstOrder, 
CONVERT(DATE, MAX(OrderDate)) AS FirstOrder
FROM SalesOrderHeader H JOIN SalesOrderDetail D ON (
	H.SalesOrderID = D.SalesOrderID
)
GROUP BY ProductID
ORDER BY ProductID

--6. Product cost on a specific date, part 2
--It turns out that the answer to the above problem has a problem. Change the date to 2014-04-15.
--What are your results?
--If you use the SQL from the answer above, and just change the date, you won't get the results
--you want.
--Fix the SQL so it gives the correct results with the new date. Note that when the EndDate is null,
--that means that price is applicable into the future.

SELECT ProductID, StandardCost
FROM ProductCostHistory
WHERE STARTDATE <= '2014-04-15' AND '2014-04-15' <= ISNULL(ENDDATE, GETDATE())

--7. Product List Price: how many price changes?
--Show the months from the ProductListPriceHistory table, and the total number of changes made
--in that month.

WITH PriceChange AS (
	SELECT StartDate, ListPrice, 
	LEAD(ListPrice, 1) OVER (PARTITION BY ProductID ORDER BY StartDate) AS NextListPrice
	FROM ProductListPriceHistory
)
SELECT Format(StartDate, 'yyyy/MM') AS ProductListPriceMonth, COUNT(ListPrice) AS TotalRows
FROM PriceChange
WHERE ListPrice <> NextListPrice
GROUP BY Format(StartDate, 'yyyy/MM')

--8. Product List Price: months with no price changes?
--After reviewing the results of the previous query, it looks like price changes are made only in
--one month of the year.
--We want a query that makes this pattern very clear. Show all months (within the range of
--StartDate values in ProductListPriceHistory). This includes the months during which no prices
--were changed.

SELECT CalendarMonth, ISNULL(COUNT(ProductID), 0) AS TotalRows
FROM ProductListPriceHistory RIGHT JOIN Calendar ON (
	CalendarDate = StartDate
)
WHERE Calendar.CalendarDate >=
(Select Min(StartDate) from ProductListPriceHistory)
and Calendar.CalendarDate <=
(Select Max(StartDate) from ProductListPriceHistory)
GROUP BY CalendarMonth
ORDER BY CalendarMonth

--9. Current list price of every product
--What is the current list price of every product, using the ProductListPrice history?
--Order by ProductID

SELECT ProductID, ListPrice
FROM ProductListPriceHistory
WHERE EndDate IS NULL
ORDER BY ProductID

--10. Products without a list price history
--Show a list of all products that do not have any entries in the list price history table.
--Sort the results by ProductID

SELECT ProductID, ProductName
FROM Product
WHERE ProductID NOT IN 
(
	SELECT DISTINCT ProductID
	FROM ProductListPriceHistory
)
ORDER BY ProductID

--11. Product cost on a specific date, part 3
--In the earlier problem “Product cost on a specific date, part 2”, this answer was given:
--Select
--ProductID
--,StandardCost
--From ProductCostHistory
--Where
--'2014-04-15' Between StartDate and IsNull(EndDate, getdate())
--Order By ProductID
--However, there are many ProductIDs that exist in the ProductCostHistory table that don’t show
--up in this list
--Show every ProductID in the ProductCostHistory table that does not appear when you run the
--above SQL.


SELECT DISTINCT ProductID
FROM ProductCostHistory
WHERE ProductID NOT IN
(
	Select
	ProductID
	From ProductCostHistory
	Where
	'2014-04-15' Between StartDate and IsNull(EndDate, getdate())
)

--12. Products with multiple current list price records
--There should only be one current price for each product in the ProductListPriceHistory table, but
--unfortunately some products have multiple current records.
--Find all these, and sort by ProductID

SELECT ProductID
FROM ProductListPriceHistory
WHERE EndDate IS NULL
GROUP BY ProductID
HAVING COUNT(ProductID) > 1


--13. Products with their first and last order date, including name
--and subcategory
--In the problem “Products with their first and last order date, including name", we looked only at
--product that have been ordered.
--It turns out that there are many products that have never been ordered.
--This time, show all the products, and the first and last order date. Include the product
--subcategory as well.
--Sort by the ProductName field.

WITH ProductOrders AS (
	SELECT ProductID, CONVERT(DATE, MIN(OrderDate)) AS FirstOrder, 
	CONVERT(DATE, MAX(OrderDate)) AS LastOrder
	FROM SalesOrderHeader JOIN SalesOrderDetail ON (
		SalesOrderHeader.SalesOrderID = SalesOrderDetail.SalesOrderID
	)
	GROUP BY ProductID
)
SELECT Product.ProductID, ProductName, ProductSubCategoryName, FirstOrder, LastOrder
FROM Product LEFT JOIN ProductSubcategory ON (
	Product.ProductSubcategoryID = ProductSubcategory.ProductSubCategoryID
) LEFT JOIN ProductOrders ON (
	Product.ProductID = ProductOrders.ProductID
)
ORDER BY ProductName

--14. Products with list price discrepancies
--It's astonishing how much work with SQL and data is in finding and resolving discrepancies in
--data. Some of the salespeople have told us that the current price in the price list history doesn't
--seem to match the actual list price in the Product table.
--Find all these discrepancies. Sort the results by ProductID.

SELECT P.ProductID, ProductName, P.ListPrice, L.ListPrice AS LatestListPrice, 
		(P.ListPrice - L.ListPrice) AS Diff
FROM Product P JOIN ProductListPriceHistory L ON (
	P.ProductID = L.ProductID
)
WHERE EndDate IS NULL AND P.ListPrice <> L.ListPrice
ORDER BY P.ProductID

--15. Orders for products that were unavailable
--It looks like some products were sold before or after they were supposed to be sold, based on the
--SellStartDate and SellEndDate in the Product table. Show a list of these orders, with details.
--Sort the results by ProductID, then OrderDate.

SELECT P.ProductID, OrderDate, ProductName, OrderQty, SellStartDate, SellEndDate 
FROM SalesOrderHeader H LEFT JOIN SalesOrderDetail D ON (
	H.SalesOrderID = D.SalesOrderID

) JOIN Product P ON (
	D.ProductID = P.ProductID
)
WHERE H.OrderDate < P.SellStartDate OR H.OrderDate > P.SellEndDate
ORDER BY P.ProductID


--16. Orders for products that were unavailable: details
--We'd like to get more details on when products that were supposed to be unavailable were ordered.
--Create a new column that shows whether the product was ordered before the sell start date, or after the sell end date.
--Sort the results by ProductID and OrderDate.

SELECT P.ProductID, OrderDate, ProductName, OrderQty, SellStartDate, SellEndDate, 
CASE WHEN OrderDate < SellStartDate THEN 'BEFORE' WHEN OrderDate > SellStartDate THEN 'AFTER' END AS Reason
FROM SalesOrderHeader H LEFT JOIN SalesOrderDetail D ON (
	H.SalesOrderID = D.SalesOrderID

) JOIN Product P ON (
	D.ProductID = P.ProductID
)
WHERE H.OrderDate < P.SellStartDate OR H.OrderDate > P.SellEndDate
ORDER BY P.ProductID, OrderDate

--17. OrderDate with time component
--How many OrderDate values in SalesOrderHeader have a time component to them?
--Show the results as below.

SELECT TotalOrdersWithTime, TotalOrders, TotalOrdersWithTime * 1.0 / TotalOrders AS PercentOrderWithTime
FROM (
	SELECT COUNT(*) AS TotalOrdersWithTime
	FROM SalesOrderHeader
	WHERE CONVERT(TIME, OrderDate) <> CONVERT(TIME, '00:00:00.000')
) temp1 JOIN 
(
	SELECT COUNT(SalesOrderID) AS TotalOrders
	FROM SalesOrderHeader
) temp2 ON TotalOrdersWithTime <> TotalOrders

-- 18. Fix this SQL! Number 1

Select
Product.ProductID
,ProductName
,ProductSubCategoryName
,FirstOrder = Convert(date, Min(OrderDate))
,LastOrder = Convert(date, Max(OrderDate))
From Product
Left Join SalesOrderDetail Detail
on Product.ProductID = Detail.ProductID
Left Join SalesOrderHeader Header
on Header.SalesOrderID = Detail .SalesOrderID
Left Join ProductSubCategory
on ProductSubCategory.ProductSubCategoryID = Product.ProductSubCategoryID
Where
'Color' = 'Silver'    ---- ERROR IS HERE ----
Group by Product.ProductID
,ProductName
,ProductSubCategoryName
Order by LastOrder desc

--19. Raw margin quartile for products
--The product manager would like to show information for all products about the raw margin – 
--that is, the price minus the cost. Create a query that will show this information, as well as the raw margin quartile.
--For this problem, the quartile should be 1 if the raw margin of the product is in the top 25%, 2 if the product is in the second 25%, etc.
--Sort the rows by the product name.

SELECT ProductID, ProductName, StandardCost, ListPrice, (ListPrice - StandardCost) AS Margin, 
NTILE(4) OVER (ORDER BY (ListPrice - StandardCost) DESC) AS Quantile 
FROM Product
WHERE (ListPrice - StandardCost) > 0
ORDER BY ProductName


--20. Customers with purchases from multiple sales people
--Show all the customers that have made purchases from multiple sales people.
--Sort the results by the customer name (first name plus last name).

SELECT C.CustomerID, FirstName + '_' + LastName AS CustomerName, TotalDifferentSalesPeople
FROM Customer C JOIN 
(
	SELECT CustomerID, COUNT(DISTINCT SalesPersonEmployeeID) AS TotalDifferentSalesPeople
	FROM SalesOrderHeader 
	GROUP BY CustomerID
	HAVING COUNT(DISTINCT SalesPersonEmployeeID) > 1
) temp ON (
	C.CustomerID = temp.CustomerID
)
ORDER BY FirstName + '_' + LastName

--22. Duplicate product
--It looks like the Product table may have duplicate records. 
--Find the names of the products that have duplicate records (based on having the same ProductName).

SELECT ProductName
FROM Product
GROUP BY ProductName
HAVING COUNT(*) > 1

--23. Duplicate product: details
--We'd like to get some details on the duplicate product issue. 
--For each product that has duplicates, show the product name and the specific ProductID that we believe to be the duplicate 
--(the one that's not the first ProductID for the product name).

WITH FirstProductID AS (
	SELECT ProductName, MIN(ProductID) AS FirstProductID
	FROM Product
	WHERE ProductName IN (
		SELECT ProductName
		FROM Product
		GROUP BY ProductName
		HAVING COUNT(*) > 1
	)
	GROUP BY ProductName
)
SELECT P.ProductName, ProductID
FROM Product P JOIN FirstProductID F ON (
	P.ProductName = F.ProductName AND
	P.ProductID <> F.FirstProductID
)



WITH ProductCount AS (
	SELECT ProductName, ProductID, ROW_NUMBER() OVER (PARTITION BY ProductName ORDER BY ProductID) AS ProductCount
	FROM Product
)
SELECT ProductName, ProductID
FROM ProductCount
WHERE ProductCount > 1


--24/27. How many cost changes do products generally have?
--We've worked on many problems based on the ProductCostHistory table. 
--We know that the cost for some products has changed more than for other products. 
--Write a query that shows how many cost changes that products have, in general.
--For this query, you can ignore the fact that in ProductCostHistory, 
--sometimes there's an additional record for a product where the cost didn't actually change.

-- Consider identical prices
WITH LastPrice AS (
	SELECT ProductID, StartDate, StandardCost, 
	LAG(StandardCost) OVER (PARTITION BY ProductID ORDER BY StartDate) AS LastCost
	FROM ProductCostHistory
), PriceChanges AS (
	SELECT ProductID, COUNT(ProductID) AS NumberPriceChanges
	FROM LastPrice
	WHERE StandardCost <> LastCost OR LastCost IS NULL
	GROUP BY ProductID
)
SELECT *
FROM PriceChanges
ORDER BY ProductID

-- Ignore identical prices records
SELECT NumberPriceChanges, COUNT(ProductID) AS NumberofProducts
FROM (
	SELECT ProductID, COUNT(StandardCost) AS NumberPriceChanges
	FROM ProductCostHistory
	GROUP BY ProductID
) temp
GROUP BY NumberPriceChanges
ORDER BY NumberPriceChanges

--25. Size and base ProductNumber for products
--The ProductNumber field in the Product table comes from the vendor of the product. The size is sometimes a part of this field.
--We need to get the base ProductNumber (without the size), and then the size separately. 
--Some products do not have a size. For those products, the base ProductNumber will be the same as the ProductNumber, and the size field will be null.
--Limit the results to those ProductIDs that are greater than 533. Sort by ProductID. 
-- The size follows a hyphen

SELECT ProductID, ProductNumber, CHARINDEX('-', ProductNumber) AS HyphenLocation, 
CASE CHARINDEX('-', ProductNumber) WHEN 0 THEN NULL ELSE SUBSTRING(ProductNumber, CHARINDEX('-', ProductNumber)+1, LEN(ProductNumber)-CHARINDEX('-', ProductNumber)) END AS Size
FROM Product
WHERE ProductID > 533
ORDER BY ProductID


--26. Number of sizes for each base product number
--Now we'd like to get all the base ProductNumbers, and the number of sizes that they have.
--Use the output of the previous problem to get the results. However, do not use the filter from the previous problem (ProductIDs that are greater than 533). 
--Instead of that filter, select only those products that are clothing (ProductCategory = 3).
--Order by the base ProductNumber.

SELECT BaseProductNumber, COUNT(DISTINCT Size) AS TotalSizes
FROM (
	SELECT ProductID, ProductNumber, ProductSubcategoryID, CHARINDEX('-', ProductNumber) AS HyphenLocation, 
	CASE CHARINDEX('-', ProductNumber) WHEN 0 THEN ProductNumber ELSE SUBSTRING(ProductNumber, 0, CHARINDEX('-', ProductNumber)) END AS BaseProductNumber,
	CASE CHARINDEX('-', ProductNumber) WHEN 0 THEN '1' ELSE SUBSTRING(ProductNumber, CHARINDEX('-', ProductNumber)+1, LEN(ProductNumber)-CHARINDEX('-', ProductNumber)) END AS Size
	FROM Product
) temp LEFT JOIN ProductSubcategory S ON temp.ProductSubcategoryID = S.ProductSubcategoryID
WHERE ProductCategoryID = 3
GROUP BY BaseProductNumber
ORDER BY BaseProductNumber


--28. Which products had the largest increase in cost?
--We'd like to show which products have had the largest, one time increases in cost. 
--Show all of the price increases (and decreases), in decreasing order of difference.
--Don't show any records for which there is no price difference.

WITH LastPrice AS (
	SELECT ProductID, StartDate, StandardCost, 
	LAG(StandardCost, 1) OVER (PARTITION BY ProductID ORDER BY StartDate) AS LastCost 
	FROM ProductCostHistory
), PriceChange AS (
	SELECT StartDate, ProductID, StandardCost, LastCost, (StandardCost - LastCost) AS CostChange
	FROM LastPrice
	WHERE LastCost IS NOT NULL
)
SELECT *
FROM PriceChange
Order by CostChange desc


--30/31. History table with start/end date overlap
--There is a product that has an overlapping date ranges in the ProductListPriceHistory table.
--Find the products with overlapping records, and show the dates that overlap.

--Expected Results
--CalendarDate	ProductID	TotalRows
--2013-05-15	746			2
--2013-05-16	746			2
--2013-05-17	746			2
--2013-05-18	746			2



;WITH e1(n) AS
(
    SELECT 1 UNION ALL SELECT 1 UNION ALL SELECT 1 UNION ALL 
    SELECT 1 UNION ALL SELECT 1 UNION ALL SELECT 1 UNION ALL 
    SELECT 1 UNION ALL SELECT 1 UNION ALL SELECT 1 UNION ALL SELECT 1
), -- 10
e2(n) AS (SELECT 1 FROM e1 CROSS JOIN e1 AS b)
SELECT *
FROM e2


SELECT CalendarDate, ProductID, COUNT(StartDate) AS TotalRows
FROM Calendar AS c JOIN 
(
	SELECT DISTINCT *
	FROM ProductListPriceHistory
) AS p ON (
	c.CalendarDate >= p.StartDate AND c.CalendarDate <= COALESCE(p.EndDate, GETDATE())
)
GROUP BY CalendarDate, ProductID
HAVING COUNT(StartDate) >= 2
ORDER BY CalendarDate, ProductID


--32. Running total of orders in last year
--For the company dashboard we'd like to calculate the total number of orders, by month, as well
--as the running total of orders.
--Limit the rows to within one year of the last order. Sort by calendar month.


--Expected Results
--CalendarMonth			TotalOrders		RunningTotal
--2013/06 - Jun			13				13
--2013/07 - Jul			86				99
--2013/08 - Aug			88				187
--2013/09 - Sep			89				276
--2013/10 - Oct			99				375
--2013/11 - Nov			105				480


WITH TotalOrders AS (
	SELECT CalendarMonth, COUNT(SalesOrderID) As TotalOrders
	FROM [dbo].[SalesOrderHeader] JOIN Calendar ON (CONVERT(DATE, OrderDate) = CalendarDate)
	WHERE OrderDate >= DATEADD(YEAR, -1, (SELECT MAX(OrderDate) FROM SalesOrderHeader))
	GROUP BY CalendarMonth
)
SELECT CalendarMonth, TotalOrders, SUM(TotalOrders) OVER (ORDER BY CalendarMonth ROWS UNBOUNDED PRECEDING) AS RunningTotal
FROM TotalOrders
ORDER BY CalendarMonth

--33. Total late orders by territory
--Show the number of total orders, and the number of orders that are late.
--For this problem, an order is late when the DueDate is before the ShipDate.
--Group and sort the rows by Territory.
--Expected Results
--TerritoryID		TerritoryName	CountryCode		TotalOrders		TotalLateOrders
--1					Northwest		US				233				78
--2					Northeast		US				14				7
--3					Central			US				20				11

WITH OrderbyTerritory AS (
	SELECT t.TerritoryID, TerritoryName, CountryCode, SalesOrderID, DueDate, ShipDate
	FROM SalesOrderHeader s JOIN SalesTerritory t ON (s.TerritoryID = t.TerritoryID)

), TotalOrders AS (
	SELECT TerritoryID, TerritoryName, CountryCode, COUNT(SalesOrderID) AS TotalOrders
	FROM OrderbyTerritory
	GROUP BY TerritoryID, TerritoryName, CountryCode
), LateOrders AS (
	SELECT TerritoryID, TerritoryName, CountryCode, COUNT(SalesOrderID) AS TotalLateOrders
	FROM OrderbyTerritory
	WHERE DueDate < ShipDate
	GROUP BY TerritoryID, TerritoryName, CountryCode
)
SELECT s.TerritoryID, s.TerritoryName, s.CountryCode, TotalOrders, TotalLateOrders
FROM TotalOrders s JOIN LateOrders l ON (s.TerritoryID = l.TerritoryID)
ORDER BY s.TerritoryID

--36. Order processing: time in each stage
--When an order is placed, it goes through different stages, such as processed, readied for pick up,
--in transit, delivered, etc.
--How much time does each order spend in the different stages?
--To figure out which tables to use, take a look at the list of tables in the database. You should be
--able to figure out the tables to use from the table names.
--Limit the orders to these SalesOrderIDs:
--68857
--70531
--70421
--Sort by the SalesOrderID, and then the date/time.

WITH TrackingHistory AS (
	SELECT SalesOrderID, EventDateTime AS CurrentEvent, TrackingEventID AS CurrentEventID,
	LAG(EventDateTime) OVER (PARTITION BY SalesOrderID ORDER BY EventDateTime) AS PrevEvent
	FROM OrderTracking 
	WHERE SalesOrderID IN (68857, 70531, 70421) 
)
SELECT SalesOrderID, EventName, DATEDIFF(HOUR, PrevEvent, CurrentEvent) AS HoursTaken 
FROM TrackingHistory T JOIN [TrackingEvent] E ON (
	T.CurrentEventID = E.TrackingEventID
)
WHERE PrevEvent IS NOT NULL


--37. Order processing: time in each stage, part 2
--Now we want to show the time spent in each stage of order processing. But instead of showing
--information for specific orders, we want to show aggregate data, by online vs offline orders.
--Sort first by OnlineOfflineStatus, and then TrackingEventID.

WITH TrackingHistory AS (
	SELECT SalesOrderID, EventDateTime AS CurrentEvent, TrackingEventID AS CurrentEventID,
	LEAD(EventDateTime, 1) OVER (PARTITION BY SalesOrderID ORDER BY EventDateTime) AS NextEvent
	FROM OrderTracking 
), EventHistory AS (
SELECT T.SalesOrderID, EventName, (
	CASE WHEN OnlineOrderFlag = 0 THEN 'Offline'
	ELSE 'Online'
	END
) AS OrderCategory, 

DATEDIFF(HOUR, CurrentEvent, NextEvent)*1.0 AS HoursTaken 
	FROM TrackingHistory T JOIN [TrackingEvent] E ON (
		T.CurrentEventID = E.TrackingEventID
	) JOIN SalesOrderHeader H ON (
		T.SalesOrderID = H.SalesOrderID
	)
)
SELECT OrderCategory, EventName, AVG(HoursTaken) AS HoursTaken
FROM EventHistory
GROUP BY EventName, OrderCategory
ORDER BY OrderCategory, EventName

--38. Order processing: time in each stage, part 3
--The previous query was very helpful to the operations manager, to help her get an overview of
--differences in order processing between online and offline orders.
--Now she has another request, which is to have the averages for online/offline status on the same
--line, to make it easier to compare.


--39. Top three product subcategories per customer
--The marketing department would like to have a listing of customers, with the top 3 product
--subcategories that they've purchased.
--To define “top 3 product subcategories”, we'll order by the total amount purchased for those
--subcategories (i.e. the line total).
--Normally we'd run the query for all customers, but to make it easier to view the results, please
--limit to just the following customers:
	--13763
	--13836
	--20331
	--21113
	--26313
--Sort the results by CustomerID


WITH CustomerOrderDetail AS (
	SELECT CustomerID, ProductSubCategoryName, LineTotal
	FROM SalesOrderDetail AS S JOIN SalesOrderHeader H ON (
		S.SalesOrderID = H.SalesOrderID
	) JOIN Product AS P ON (
		S.ProductID = P.ProductID
	) JOIN ProductSubcategory AS C ON (
		P.ProductSubcategoryID = C.ProductSubcategoryID
	)
), CustomerOrderCategory AS (
	SELECT CustomerID, ProductSubCategoryName, SUM(LineTotal) AS Total
	FROM CustomerOrderDetail
	GROUP BY CustomerID, ProductSubCategoryName
), CustomerOrderCategoryRank AS (
	SELECT CustomerID, Total, ProductSubCategoryName, ROW_NUMBER() OVER (PARTITION BY CustomerID ORDER BY Total DESC) AS Rn
	FROM CustomerOrderCategory
)
SELECT CustomerID, ProductSubcategoryName, Total
FROM CustomerOrderCategoryRank
WHERE Rn <= 3 AND CustomerID IN (
	13763,
	13836,
	20331,
	21113,
	26313
)


--40. History table with date gaps
--It turns out that, in addition to overlaps, there are also some gaps in the ProductListPriceHistory
--table. That is, there are some date ranges for which there are no list prices. We need to find the
--products and the dates for which there are no list prices.
--This is one of the most challenging and fun problems in this book, so take your time and enjoy it!
--Try doing it first without any hints, because even if you don't manage to solve the problem, you
--will have learned much more.

--ProductID		DateWithMissingPrice
--742				2013-05-21
--742				2013-05-22
--742				2013-05-23
--742				2013-05-24

-- Idea: Find missing on two columns (ProductID and CalendarDate). So first step is to create the cartesian product of the two

WITH ProductAvailablePeriod AS (
	SELECT ProductID, MIN(StartDate) AS MinStartDate, MAX(ISNULL(EndDate, '2014-05-29')) AS MaxEndDate
	FROM ProductListPriceHistory
	GROUP BY ProductID
), ProductDates AS (
	SELECT ProductID, CalendarDate
	FROM ProductAvailablePeriod AS P LEFT JOIN Calendar AS C ON (
		CalendarDate >= MinStartDate AND CalendarDate < MaxEndDate 
	) 
)
SELECT D.ProductID, CalendarDate
FROM ProductDates D LEFT JOIN ProductListPriceHistory P ON (
	D.ProductID = P.ProductID AND
	D.CalendarDate BETWEEN P.StartDate AND ISNULL(P.EndDate, '2014-05-29')
)
WHERE P.ProductID IS NULL

