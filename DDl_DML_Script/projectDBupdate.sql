/*updating the employee name in the Employee table where the Emp_Id=E1025;*/
update Fall22_S003_5_Employee set EName='Virat Kohli' where E_ID='E1025';

/*updating the employee date of birth in the Employee table using the SSN field; */
update Fall22_S003_5_Employee set Date_of_birth='27/08/1998' where SSN='128111234';
select * from Fall22_S003_5_Employee;

/*updating the media preference by customer in the Fall22_S003_5_Customer */
update Fall22_S003_5_Customer set media='Newspaper' where Customer_Name = 'Alen Robert' and Phone_number='772-121-3292';

/*updating the customer_name in the Fall22_S003_5_CUSTOMER table */
update Fall22_S003_5_CUSTOMER set customer_name ='Monica Geller' where Customer_ID='C1016';

update Fall22_S003_5_Customer set media='Social Media' where Customer_ID='C1044';
select * from Fall22_S003_5_CUSTOMER;
 
/*updating the email address of the vendor with vendor_id='10000' in the Fall22_S003_5_Vendor table; */
update Fall22_S003_5_Vendor set V_email='vistarfoods@gmail.com' where V_ID='V1003';
select * from Fall22_S003_5_VENDOR;

/*updating the quantity supplied of the Fall22_S003_5_PRODUCTS table where the PId='P1024';*/
update Fall22_S003_5_PRODUCTS set Qty_supp=30 where P_ID='P1024';

/* updating the supply date in the Fall22_S003_5_PRODUCTS table using vendorId and order_date */
update Fall22_S003_5_PRODUCTS set Date_supp='18/10/22' where P_ID='P1010';
select * from Fall22_S003_5_PRODUCTS;


/*updating the employee id who managed the transaction using the T_ID*/
update Fall22_S003_5_TRANSACTIONS set E_ID='1034' where T_ID='T1075';
select * from Fall22_S003_5_TRANSACTIONS;


/* deleting a customer record and inserting the record again in to the table.*/
select count(*) from  Fall22_S003_5_CUSTOMER;
delete  from Fall22_S003_5_CUSTOMER where Customer_Name='Alan Ross' and Customer_ID='C1015';
select count(*) from  Fall22_S003_5_CUSTOMER;
insert into Fall22_S003_5_CUSTOMER(Customer_ID, Customer_Name, Gender, Date_of_joining, Customer_type, media, Phone_number, rating, Date_of_birth) values ('C1015','Alan Ross','M','29/12/2020','faculty','Social Media','576-469-9903','5.7','04/06/1980');
select * from Fall22_S003_5_CUSTOMER;

