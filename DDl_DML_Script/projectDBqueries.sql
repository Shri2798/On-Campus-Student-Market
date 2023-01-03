/*No of customers who purchased products more than once*/

SELECT Customer_Name,Customer_ID 
    FROM Fall22_S003_5_CUSTOMER 
        WHERE Customer_ID IN(
            SELECT S.Customer_ID 
                FROM Fall22_S003_5_TRANSACTIONS S 
                    GROUP BY S.Customer_ID 
                        HAVING COUNT(S.Customer_ID)>1);

/*Used 'CUBE', 'Group by'
  -- Here the CUBE will return more rows and the sum of the quantity of the products by grouping Product_Name,Selling_Price,Category
  -- we have done this using 2 tables contains and product as intially products will be grouped with selling price and then it will be 
  -- grouped to category resulting quantity*/

select P.P_Name, P.Price, P.Category, sum (t.qty_purchased) 
from Fall22_S003_5_PRODUCTS P, Fall22_S003_5_TRANSACTIONS t 
where P.P_ID=t.P_ID 
Group by CUBE (P.P_Name, P.Price, P.Category);

/*Grouping category models by Health and Beauty' and getting their respective suppliers and qty counts */
SELECT p1.P_Type, p1.Qty_supp, v1.V_ID, v1.V_name ,count(Qty_supp) 
    FROM Fall22_S003_5_PRODUCTS p1, Fall22_S003_5_VENDOR v1 
        WHERE p1.V_ID = v1.V_ID and p1.Category='Health and Beauty' 
            GROUP BY p1.P_Type, p1.Qty_supp, v1.V_ID, v1.V_name;

/*QUERY for selecting products having price greater than 20 using ROLLUP*/
select P_Name, Price 
from Fall22_S003_5_PRODUCTS 
GROUP BY ROLLUP (P_Name, Price) 
HAVING Price>'20';


/*Quarterly Revenue Model*/
/* Monthly Sold items */
SELECT P_ID, SUM(qty_purchased) as sold
FROM Fall22_S003_5_TRANSACTIONS
WHERE T_date BETWEEN TO_DATE('01/07/2022','DD/MM/YYYY') AND TO_DATE('01/09/2022','DD/MM/YYYY')
GROUP BY P_ID
ORDER BY sold DESC;


/*Media that is promoting our business widely using FETCH we are showing the top 2 results*/
SELECT media, COUNT(media) as count 
FROM Fall22_S003_5_CUSTOMER
GROUP BY media
ORDER BY count DESC
FETCH NEXT 2 ROWS ONLY;

/*Average rating of the business based on the customer rating given at the time of transaction*/

SELECT AVG(rating) as Rating 
FROM Fall22_S003_5_CUSTOMER;

/*Query Using OVER()
We are obtaining the Product ID,Name its overall average price and the average price at which it is being sold against the other products*/
SELECT P_ID, P_Name, Price,
    AVG(Price) OVER() AS "overall_average_price",
    AVG(Price) OVER (PARTITION BY P_type) AS "product_average_price"
FROM Fall22_S003_5_PRODUCTS;


