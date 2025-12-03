-- sql/schema.sql
CREATE TABLE Customers (
  CustomerID INT PRIMARY KEY,
  CustomerName VARCHAR(100),
  Region VARCHAR(50)
);

CREATE TABLE Products (
  ProductID INT PRIMARY KEY,
  ProductName VARCHAR(100),
  Category VARCHAR(50),
  Price DECIMAL(10,2)
);

CREATE TABLE Sales (
  SaleID INT PRIMARY KEY,
  Date DATE,
  CustomerID INT,
  ProductID INT,
  Quantity INT,
  SalesAmount DECIMAL(12,2),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Calendar (date dimension)
CREATE TABLE Calendar (
  Date DATE PRIMARY KEY,
  Year INT,
  Month INT,
  Day INT,
  MonthName VARCHAR(20),
  Quarter INT,
  IsHoliday BIT DEFAULT 0
);
