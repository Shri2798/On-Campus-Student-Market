/* create the employee table */
CREATE TABLE Fall22_S003_5_EMPLOYEE(
E_ID VARCHAR(15) NOT NULL PRIMARY kEY, 
EName VARCHAR(20) NOT NULL,
SSN integer  NOT NULL UNIQUE,
Date_of_birth DATE,
Date_of_joining DATE,
Gender CHAR CHECK(Gender='F'OR Gender='M')
);
commit;

/* creating employee phone number table */
CREATE TABLE Fall22_S003_5_Emp_ph(
E_ID VARCHAR(15) NOT NULL, 
Ph_Type VARCHAR(15) NOT NULL,
Ph_Number VARCHAR(12) UNIQUE,
primary key(E_ID,Ph_Type,Ph_Number),
foreign key(E_ID)
 references Fall22_S003_5_EMPLOYEE(E_ID)
 ON DELETE CASCADE
);
commit;

/* created the customer table*/
CREATE TABLE Fall22_S003_5_CUSTOMER(
Customer_ID VARCHAR(15) NOT NULL PRIMARY KEY, 
Customer_Name VARCHAR(40) NOT NULL,
Gender CHAR CHECK(Gender='F'OR Gender='M'),
Date_of_joining DATE,
Customer_type VARCHAR(10),
media VARCHAR(20),
Phone_number VARCHAR (12) UNIQUE,
rating FLOAT default '5',
Date_of_birth DATE
);
commit;

/* creating the vendor table*/
CREATE table  Fall22_S003_5_VENDOR(
V_ID VARCHAR(8) NOT NULL PRIMARY KEY, 
V_Name VARCHAR(40) NOT NULL, 
V_email VARCHAR(50) NOT NULL,
V_Ph_no VARCHAR(12) UNIQUE
);
commit;

/* creating the product details*/
CREATE TABLE Fall22_S003_5_PRODUCTS(
P_ID VARCHAR(8) NOT NULL PRIMARY KEY,  
P_Name varchar(40) NOT NULL,
P_Type VARCHAR(20) NOT NULL,
Category VARCHAR(30),
Price FLOAT default '20',
V_ID VARCHAR(8) NOT NULL,
Date_supp DATE,
Qty_supp integer default '0',
foreign key(V_ID)
 references Fall22_S003_5_VENDOR(V_ID)
 ON DELETE CASCADE
);
commit;

/*creating the Transactions table*/

CREATE table Fall22_S003_5_TRANSACTIONS(
T_ID VARCHAR(20) NOT NULL PRIMARY KEY, 
T_date DATE,
Customer_ID VARCHAR(15) NOT NULL,
P_ID VARCHAR(8) NOT NULL,
qty_purchased INTEGER NOT NULL,
E_ID VARCHAR(15) NOT NULL,
foreign key(Customer_ID)
 references Fall22_S003_5_CUSTOMER(Customer_ID)
 ON DELETE CASCADE,
foreign key(P_ID)
 references Fall22_S003_5_PRODUCTS(P_ID)
 ON DELETE CASCADE,
foreign key(E_ID)
 references Fall22_S003_5_EMPLOYEE(E_ID)
 ON DELETE CASCADE
);
commit;

/* created the table payment details*/
CREATE TABLE Fall22_S003_5_PAYMENT_DETAILS
(
Payment_ID VARCHAR(20) NOT NULL PRIMARY KEY, 
T_ID VARCHAR(20) NOT NULL,
Tot_amount FLOAT NOT NULL,
foreign key(T_ID)
 references Fall22_S003_5_TRANSACTIONS(T_ID)
 ON DELETE CASCADE
);
commit;

/*created the payment mode*/
CREATE TABLE Fall22_S003_5_PAYMENT_MODE( 
Payment_ID VARCHAR(20) NOT NULL PRIMARY KEY, 
T_ID VARCHAR(20) NOT NULL,
P_mode VARCHAR(10),
amt FLOAT NOT NULL,
foreign key(Payment_ID)
 references Fall22_S003_5_PAYMENT_DETAILS(Payment_ID)
 ON DELETE CASCADE,
foreign key(T_ID)
 references Fall22_S003_5_TRANSACTIONS(T_ID)
 ON DELETE CASCADE
);
commit;


/* created the table where customer purchases products */
CREATE TABLE Fall22_S003_5_CUST_bought_PRD(
Customer_ID VARCHAR(15) NOT NULL, 
P_ID varchar(8),
primary key(Customer_ID,P_ID),
foreign key(Customer_ID)
 references Fall22_S003_5_CUSTOMER(Customer_ID)
 ON DELETE CASCADE,
foreign key(P_ID)
 references Fall22_S003_5_PRODUCTS(P_ID)
 ON DELETE CASCADE
);
commit;
