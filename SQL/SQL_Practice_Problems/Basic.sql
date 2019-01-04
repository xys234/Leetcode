USE Northwind_SPP

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