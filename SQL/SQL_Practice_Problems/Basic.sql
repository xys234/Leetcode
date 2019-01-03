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