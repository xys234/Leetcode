-- ANSWERS

USE Northwind_SPP


-------------------- MORE SQL ------------------------

-- 13. 
Select
Product.ProductID
,ProductName
,ProductSubCategoryName
,FirstOrder = Convert(date, Min(OrderDate))
,LastOrder = Convert(date, Max(OrderDate))
From Product
left Join SalesOrderDetail Detail
on Product.ProductID = Detail.ProductID
left join SalesOrderHeader Header
on Header.SalesOrderID = Detail .SalesOrderID
left join ProductSubCategory ProdSubCat
on ProdSubCat.ProductSubCategoryID = Product.ProductSubCategoryID
Group by
Product.ProductID
,ProductName
,ProductSubCategoryName
Order by ProductName