USE Northwind_SPP


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

