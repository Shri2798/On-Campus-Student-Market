import cx_Oracle
from tabulate import tabulate

#Connecting to the database
db_Connect = cx_Oracle.connect('sxt4029', 'Archana123456', 'acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')
if db_Connect:
        cursor = db_Connect.cursor()
        print("Database version:", db_Connect.version)    
        print("Wohoo!!!Connected to Database")
else:
        print("Database Connection failed!!!")


def menu():
    print('Choose an option from the menu below')
    print('----------- Menu ----------')
    print('1. Get the Customer or Employee Data\n')
    print('2. Modify the Data\n')
    print('3. Generate a Report\n')
    print('4. Exit\n')


def getData():
    print('Enter 1 to view Customer details and 2 to view Employee Details\n')
    viewTable =  int(input('Enter input:\n'))
    cursor = db_Connect.cursor()
    if viewTable == 1:
        cursor.execute('select * from Fall22_S003_5_CUSTOMER')
        uList = cursor.fetchall()
        print ("{:<7} {:<18} {:<3} {:<9} {:<13} {:<19} {:<14} {:<4} {:<10}".format("C_ID", "C_Name", "Gender", "DOJ", "C_type", "Media", "Phone_no", "Rating", "DOB")) 
        for i in uList:
            dob = i[3].strftime("%d-%m-%Y")
            doj = i[8].strftime("%d-%m-%Y") 
            print ("{:<7} {:<18} {:<4} {:<9} {:<13} {:<19} {:<14} {:<6} {:<10}".format(i[0],i[1],i[2],dob,i[4],i[5],i[6],i[7],doj))
    elif viewTable == 2:
        cursor = db_Connect.cursor()
        cursor.execute("select E_ID, EName, SSN, Date_of_birth, Date_of_joining, Gender from Fall22_S003_5_EMPLOYEE")
        uTuple = cursor.fetchall()
        for i in range(0,len(uTuple)):
            uList = list(uTuple[i])
            uList[3] = uList[3].strftime("%d-%m-%Y")
            uList[4] = uList[4].strftime("%d-%m-%Y")
            uTuple[i] = tuple(uList)
        print (tabulate(uTuple, headers=["E_ID", "EName", "SSN", "Date_of_birth", "Date_of_joining", "Gender"]))
    else:
        print("Wrong input!")
        actionMenu()


def modifyData():
    print('1. Employee\n')
    print('2. Customer\n')
    opt = int(input("Choose an option from the above to modify relations:\n"))
    if opt == 1:
        modify = int(input("Choose 1 to Insert and 2 to Update"))
        if modify == 1:
            print("Performing Insert operation on Employee\n")
            e_id =  input('Enter E_ID: ')
            EName = input('Enter EName: ')
            ssn =  int(input('Enter SSN: '))
            Date_of_birth =  input('Enter Date_of_birth: ')
            Date_of_joining =  input('Enter Date_of_joining: ')
            Gender =  input('Enter Gender: ')
            cursor = db_Connect.cursor()
            insert_query = "INSERT INTO Fall22_S003_5_EMPLOYEE VALUES(:1, :2, :3, to_date(:4,'dd-mm-yyyy'), to_date(:5,'dd-mm-yyyy'), :6)"
            row = (e_id, EName, ssn, Date_of_birth, Date_of_joining, Gender)
            cursor.execute(insert_query, tuple(row))
            print("Inserted data into Fall22_S003_5_EMPLOYEE")
            db_Connect.commit()
            print("Inserted new Employee record successfully!")
            
            cursor = db_Connect.cursor()
            show_query = "select E_ID, EName, SSN, Date_of_birth, Date_of_joining, Gender from Fall22_S003_5_EMPLOYEE where E_ID ='{}'"
            cursor.execute(show_query.format(e_id))
            uTuple = cursor.fetchall()
            for i in range(0,len(uTuple)):
                uList = list(uTuple[i])
                uList[3] = uList[3].strftime("%d-%m-%Y")
                uList[4] = uList[4].strftime("%d-%m-%Y")
                uTuple[i] = tuple(uList)
            print (tabulate(uTuple, headers=["E_ID", "EName", "SSN", "Date_of_birth", "Date_of_joining", "Gender"]))
                       
        elif modify == 2:
            cursor = db_Connect.cursor()
            print("Performing Update operation on Employee\n")
            e_id = input("Enter employee id for whom you want to modify the data:\n")
            print("1. Ename\n")
            print("2. Date_of_birth\n")
            print("3. Date_of_Joining\n")
            print("4. Gender\n")
            attribute = int(input("Choose an attribute to update\n"))
            if attribute == 1:   
                ename = input("Enter new name to be modified:\n")
                update_query = "update Fall22_S003_5_EMPLOYEE set EName = '{}' where E_ID = '{}'"
                cursor.execute(update_query.format(ename, e_id))
                db_Connect.commit()
                print("Updated name attribute for Employee successfully!")
                
                cursor = db_Connect.cursor()
                show_query = "select E_ID, EName, SSN, Date_of_birth, Date_of_joining, Gender from Fall22_S003_5_EMPLOYEE where E_ID ='{}'"
                cursor.execute(show_query.format(e_id))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[4] = uList[4].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["E_ID", "EName", "SSN", "Date_of_birth", "Date_of_joining", "Gender"]))

            elif attribute == 2:
                dob = input("Enter date of birth to be modified in 'dd-mm-yyyy' format:\n")
                update_query = "update Fall22_S003_5_EMPLOYEE set Date_of_birth = to_date('{}','DD-MM-YYYY') where E_ID = '{}'"
                cursor.execute(update_query.format(dob, e_id))
                db_Connect.commit()
                print("Updated DOB attribute for Employee successfully!\n")
                
                cursor = db_Connect.cursor()
                show_query = "select E_ID, EName, SSN, Date_of_birth, Date_of_joining, Gender from Fall22_S003_5_EMPLOYEE where E_ID ='{}'"
                cursor.execute(show_query.format(e_id))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[4] = uList[4].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["E_ID", "EName", "SSN", "Date_of_birth", "Date_of_joining", "Gender"]))

            elif attribute == 3:
                doj = input("Enter date of joining to be modified in 'dd-mm-yyyy' format:\n")
                update_query2 = "update Fall22_S003_5_EMPLOYEE set Date_of_joining = to_date('{}','DD-MM-YYYY') where E_ID = '{}'"
                cursor.execute(update_query2.format(doj, e_id))
                db_Connect.commit()
                print("Updated DOJ attribute for Employee successfully!\n")
                
                cursor = db_Connect.cursor()
                show_query = "select E_ID, EName, SSN, Date_of_birth, Date_of_joining, Gender from Fall22_S003_5_EMPLOYEE where E_ID ='{}'"
                cursor.execute(show_query.format(e_id))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[4] = uList[4].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["E_ID", "EName", "SSN", "Date_of_birth", "Date_of_joining", "Gender"]))

                
            elif attribute == 4:
                gender = input("Enter Gender to be modified:\n")
                update_query = "update Fall22_S003_5_EMPLOYEE set Gender = '{}' where E_ID = '{}'"
                cursor.execute(update_query.format(gender, e_id))
                db_Connect.commit()
                print("Updated Gender attribute for Employee successfully!\n")
                
                cursor = db_Connect.cursor()
                show_query = "select E_ID, EName, SSN, Date_of_birth, Date_of_joining, Gender from Fall22_S003_5_EMPLOYEE where E_ID ='{}'"
                cursor.execute(show_query.format(e_id))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[4] = uList[4].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["E_ID", "EName", "SSN", "Date_of_birth", "Date_of_joining", "Gender"]))

            else:
                print("Wrong input!")
                actionMenu()
        else:
            print("Wrong input!")
            actionMenu()
                
    elif opt == 2:
        modify = int(input("Choose 1 to Insert and 2 to Update : \n"))
        if modify == 1:
            print("Performing Insert operation on Customer\n")
            Customer_ID =  input('Enter Customer ID: ')
            Customer_Name = input('Customer Name: ')
            Gender =  input('Enter Gender: ')
            Date_of_joining =  input('Enter Date_of_joining: ')
            Customer_type =  input('Enter Customer type: ')
            media =  input('Enter media: ')
            Phone_number =  input('Enter Phone number: ')
            rating =  float(input('Enter rating: '))
            Date_of_birth =  input('Enter Date_of_birth: ')
            cursor = db_Connect.cursor()
            insert_query1 = "INSERT INTO Fall22_S003_5_CUSTOMER VALUES(:1, :2, :3, to_date(:4,'dd-mm-yyyy'), :5, :6, :7, :8, to_date(:5,'dd-mm-yyyy'))"
            row1 = (Customer_ID, Customer_Name, Gender, Date_of_joining, Customer_type, media, Phone_number, rating, Date_of_birth)
            cursor.execute(insert_query1, tuple(row1))
            print("\nInserted data into Fall22_S003_5_CUSTOMER\n")
            db_Connect.commit()
            cursor = db_Connect.cursor()
            show_query = "select Customer_ID, Customer_Name, Gender, Date_of_joining, Customer_type, media, Phone_number, rating, Date_of_birth from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
            cursor.execute(show_query.format(Customer_ID))
            uTuple = cursor.fetchall()
            for i in range(0,len(uTuple)):
                uList = list(uTuple[i])
                uList[3] = uList[3].strftime("%d-%m-%Y")
                uList[8] = uList[8].strftime("%d-%m-%Y")
                uTuple[i] = tuple(uList)
            print (tabulate(uTuple, headers=["Customer_ID", "Customer_Name", "Gender", "Date_of_joining", "Customer_type", "media", "Phone_number", "rating", "Date_of_birth"]))
            
            
            
#             cursor.execute("select * from Fall22_S003_5_CUSTOMER")
#             print (tabulate(cursor, headers=["C_ID", "C_Name", "Gender", "Doj", "C_type", "media", "P_number", "rating", "Dob"]))
        
        elif modify == 2:
            cursor = db_Connect.cursor()
            print("Performing Update operation on Customer\n")
            Customer_ID = input("Enter customer id for whom you want to modify the data:\n")
            print("1. media\n")
            print("2. Customer_type\n")
            print("3. rating\n")
            attribute = int(input("Choose an attribute to update\n"))
            if attribute == 1:   
                media = input("Enter new media to be updated:\n")
                update_query = "update Fall22_S003_5_CUSTOMER set media = '{}' where Customer_ID = '{}'"
                cursor.execute(update_query.format(media, Customer_ID))
                db_Connect.commit()
                print("Media updated successfully!")
                cursor = db_Connect.cursor()
                show_query = "select Customer_ID, Customer_Name, Gender, Date_of_joining, Customer_type, media, Phone_number, rating, Date_of_birth from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
                cursor.execute(show_query.format(Customer_ID))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[8] = uList[8].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["Customer_ID", "Customer_Name", "Gender", "Date_of_joining", "Customer_type", "media", "Phone_number", "rating", "Date_of_birth"]))
                
                
#                 showquery1 = "select * from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
#                 cursor.execute(showquery1.format(Customer_ID))
#                 print (tabulate(cursor, headers=["C_ID", "C_Name", "Gender", "Doj", "C_type", "media", "P_number", "rating", "Dob"]))   
                
            elif attribute == 2:
                cType = input("Enter the Customer type to be modified:\n")
                update_query = "update Fall22_S003_5_CUSTOMER set Customer_type = '{}' where Customer_ID = '{}'"
                cursor.execute(update_query.format(cType,Customer_ID))
                db_Connect.commit()
                print("Customer type updated successfully!")
                cursor = db_Connect.cursor()
                
                show_query = "select Customer_ID, Customer_Name, Gender, Date_of_joining, Customer_type, media, Phone_number, rating, Date_of_birth from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
                cursor.execute(show_query.format(Customer_ID))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[8] = uList[8].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["Customer_ID", "Customer_Name", "Gender", "Date_of_joining", "Customer_type", "media", "Phone_number", "rating", "Date_of_birth"]))
                
            
#                 showquery1 = "select * from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
#                 cursor.execute(showquery1.format(Customer_ID))
#                 print (tabulate(cursor, headers=["C_ID", "C_Name", "Gender", "Doj", "C_type", "media", "P_number", "rating", "Dob"])) 
                               
            elif attribute == 3:
                rating = input("Enter the rating to be modified:\n")
                update_query = "update Fall22_S003_5_CUSTOMER set rating = '{}' where Customer_ID = '{}'"
                cursor.execute(update_query.format(rating, Customer_ID))
                db_Connect.commit()
                print("Rating updated successfully!")
                cursor = db_Connect.cursor()
                
                show_query = "select Customer_ID, Customer_Name, Gender, Date_of_joining, Customer_type, media, Phone_number, rating, Date_of_birth from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
                cursor.execute(show_query.format(Customer_ID))
                uTuple = cursor.fetchall()
                for i in range(0,len(uTuple)):
                    uList = list(uTuple[i])
                    uList[3] = uList[3].strftime("%d-%m-%Y")
                    uList[8] = uList[8].strftime("%d-%m-%Y")
                    uTuple[i] = tuple(uList)
                print (tabulate(uTuple, headers=["Customer_ID", "Customer_Name", "Gender", "Date_of_joining", "Customer_type", "media", "Phone_number", "rating", "Date_of_birth"]))
            
#                 showquery1 = "select * from Fall22_S003_5_CUSTOMER where Customer_ID = '{}'"
#                 cursor.execute(showquery1.format(Customer_ID))
#                 print (tabulate(cursor, headers=["C_ID", "C_Name", "Gender", "Doj", "C_type", "media", "P_number", "rating", "Dob"])) 
            else:
                print("Wrong input!")
                actionMenu()
        else:
            print("Wrong input!")
            actionMenu()
    else:
        print("Wrong input!")
        actionMenu()


def queryData():
    print('1. Get the number of customers who purchased products more than n times\n')
    print('2. Sum of the quantity of the products by grouping Product Name,Selling Price and Category\n')
    print('3. Selecting the products that have price greater than k dollars\n')
    print('4. Check the average rating of the store given by customers\n')
    print('5. Show the top 2 results of Media that are promoting our business widely\n')
    queryIp = int(input("Enter the query number :\n"))
    cursor = db_Connect.cursor()
    if queryIp == 1:
        n = int(input("Enter the n value:\n"))
        query_1 = "SELECT Customer_Name,Customer_ID FROM Fall22_S003_5_CUSTOMER WHERE Customer_ID IN(SELECT S.Customer_ID FROM Fall22_S003_5_TRANSACTIONS S GROUP BY S.Customer_ID HAVING COUNT(S.Customer_ID)> '{}')"
        cursor.execute(query_1.format(n))
        print (tabulate(cursor, headers=["Customer_Name", "Customer_ID"]))
    if queryIp == 2:
        cursor.execute("select P.P_Name, P.Price, P.Category, sum (t.qty_purchased) from Fall22_S003_5_PRODUCTS P, Fall22_S003_5_TRANSACTIONS t where P.P_ID=t.P_ID Group by CUBE (P.P_Name, P.Price, P.Category)")
        res = cursor.fetchall()
        print(type(res))
        res.reverse()
        print (tabulate(res, headers=["P_Name", "Price", "Category", "sum"]))
    if queryIp == 3:
        k = int(input("Enter the k value:\n"))
        query_3 = "select P_Name, Price from Fall22_S003_5_PRODUCTS GROUP BY ROLLUP (P_Name, Price) HAVING Price>'{}' ORDER BY PRICE DESC"
        cursor.execute(query_3.format(k))
        print ("{:<20} {:<18}".format("P_Name", "Price"))
        for P_Name,Price in cursor:
            print ("{:<20} {:<18}".format(P_Name,Price))
    if queryIp == 4:
        cursor.execute("SELECT round(avg(rating),2) as Rating FROM Fall22_S003_5_CUSTOMER")
        print("Average Rating of the store is :")
        res2=cursor.fetchall()
        print(res2)
    if queryIp == 5:
        cursor.execute("SELECT media, COUNT(media) as count FROM Fall22_S003_5_CUSTOMER GROUP BY media ORDER BY count DESC FETCH NEXT 2 ROWS ONLY")
        print ("{:<16} {:<18}".format("Media", "Count"))
        for media,count in cursor:
            print ("{:<16} {:<18}".format(media,count))  

def actionMenu():
    menu()
    userinput = int(input("Enter option : "))
    if userinput == 1:
        getData()
        print("\n")
        actionMenu()
    elif userinput == 2:
        modifyData()
        print("\n")
        actionMenu()
    elif userinput == 3:
        queryData()
        print("\n")
        actionMenu()
    elif userinput == 4: 
        exit()
    else:
        menu()

if __name__ == '__main__':
    actionMenu()