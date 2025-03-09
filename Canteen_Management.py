import mysql.connector

welcome=["Welcome","Bonjour","Namaste"]
print("Hi! Welcome to the Canteen")
for i in welcome:
    print("!!!",i,"!!!")
#Functions
#DataBase Connection
def db_connection():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Pradaap@6868",
    database="db3"
    )
    return mydb

#User related functions:
#Forgot password:
def forgot_password(user_type):
    user=user_type
    print("***Change your password here***")
    email_In=input("Email: ")
    New_password=input("New password: ")
    Confirm_new_password=input("Confirm new password: ")
    #Helps user to verify the new password entered by them
    if New_password == Confirm_new_password:
        conn = db_connection()
        mycursor=conn.cursor()
        #End user part:
        if user == 1:
            #Checks the availability of the user:
            mycursor.execute("SELECT password FROM user WHERE email = %s",(email_In,))
            result=mycursor.fetchone()
            if result is None:
                return False
            else:
                #Updates the password for the respective user
                mycursor.execute("UPDATE user SET password = %s WHERE email = %s",(Confirm_new_password,email_In))
                conn.commit()
                conn.close
                return True

        #Admin user part:
        elif user == 2:
            #Checks for the availability of the user
            mycursor.execute("SELECT password FROM admin WHERE email = %s",(email_In,))
            result=mycursor.fetchone()
            if result is None:
                return False
            else:
                #Updates the Password for the respective user
                mycursor.execute("UPDATE admin SET password = %s WHERE email = %s",(Confirm_new_password,email_In))
                conn.commit()
                conn.close
                return True


#User Signin function:
def User_Signin():
    print("Please Enter your email and create a password")
    email_In=input("Email : ")
    password=input("Password : ")
    if password is not None:
        password_In=input("Confirm your password : ")
        if password == password_In:

            #Database connection and data insertion
            try:
                conn=db_connection()
                mycursor=conn.cursor()
                mycursor.execute("INSERT INTO user (email,password) VALUES (%s,%s)",(email_In,password_In))
                conn.commit()
                print("User Signed in")
                conn.close()
            except mysql.connector.Error as err:
                print(f"Error : {err}")
            
            return True
        else:
            print("Alert! Password mismatch")
    else:
        print("Please enter a right password")


#User_Authentication function
def User_Authentication():
    print("Press 1:Login")
    print("Press 2:Signin")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        email_In=input("Enter your Email:")
        password_In=input("Enter yout Password:")
        conn=db_connection()
        mycursor=conn.cursor()
        mycursor.execute("SELECT password FROM user WHERE email= %s",(email_In,))
        result=mycursor.fetchone()
        conn.close()
        #Checks the output is empty or None
        if result is None:
            print("! User not found")
            return False
        else:
            password_Out=result[0]

        #Authentication part:
        if password_In==password_Out:
            print("***User is Authorized***")
            return True
        else:
            print("Username or password is incorrect")
            return False
    
                         
    elif choice==2:
        print("***Sign In***")
        User_Signin()
    
    else:
        print("Please enter a right Choice")

#Admin_Authentication function
def Admin_Authentication():
    email_In=input("Enter your Email:")
    password_In=input("Enter your Password:")

    #Data fetching part:
    conn = db_connection()
    mycursor = conn.cursor()
    mycursor.execute("SELECT password FROM Admin WHERE email= %s",(email_In,))
    result=mycursor.fetchone()

    #Checks the output is empty or None
    if result is None:
        print("! User Not found")
        return False
    else:
        password_Out=result[0]

    #Authentication part:
    if password_In==password_Out:
        print("***Admin is Authorized***")
        conn.close()
        return True
    else:
        print("Username or password is incorrect")
        return False
#User Orders and Invoice related funcitons:

#User Order
def user_orders():
    print("@Orders page")
    order_number=0
    email=input("Enter your email: ")
    print("#Press 1 to choose dosa")
    choice=int(input("Enter you Order:"))
    if choice == 1:
        order_number += 1
        food="dosa"
        order_quantity=int(input("Enter number of Dosa:"))
        phone_no = int(input("Enter your Phone number: "))
        phone=str(phone_no)
        conn=db_connection()
        mycursor=conn.cursor()
        mycursor.execute("SELECT price,quantity FROM Menu WHERE food_item = %s",(food,))
        result=mycursor.fetchmany()
        output=result[0]
        quantity_avail=output[1]
        #print("quantity is ",quantity_avail)
        price_out = int(output[0])
        #print("price is",price_out)
        final_price=order_quantity*price_out
        price=order_quantity*final_price
        quantity=quantity_avail-order_quantity
        mycursor.execute("INSERT INTO orders(email,phone,food_item,order_quantity,price) VALUES (%s,%s,%s,%s,%s)",(email,phone,food,order_quantity,final_price))
        mycursor.execute("UPDATE Menu SET quantity=%s WHERE food_item=%s",(quantity,food))
       
        #Ordered food details:
        my_food = {}
        my_food["phone_no"]=phone_no
        my_food["food"]=food
        my_food["Quantity"]=order_quantity
        my_food["Price"]=price
        print("Food I chose")
        print(my_food)

        #Collects the Orders 
        my_orders={}
        my_orders[order_number]=my_food
        print("My orders:")
        print(my_orders)
        conn.commit()
        conn.close()

        return my_orders
    


#Menu function
def user_menu():
    print("@User Menu")
    conn = db_connection()
    mycursor=conn.cursor()
    print("Press: 1 Breakfast")
    print("Press: 2 Lunch")
    print("Press: 3 Snacks")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("***@Breakfast Section***")
        mycursor.execute("SELECT food_item,availability,price FROM Menu WHERE repasts='breakfast'")
        result=mycursor.fetchall()
        print("[('Food', 'Availability', 'Price')]")
        for row in result:
            print(result)         
    elif choice == 2:
        print("***@Lunch Section***")
        mycursor.execute("SELECT food_item,availability,price FROM Menu WHERE repasts='lunch'")
        result=mycursor.fetchall()
        print("[('Food', 'Availability', 'Price')]")
        for row in result:
            print(result)
    else:
        print("***@Snacks Section***")
        mycursor.execute("SELECT food_item,availability,price FROM Menu WHERE repasts='snacks'")
        result=mycursor.fetchall()
        print("[('Food', 'Availability', 'Price')]")
        for row in result:
            print(result)

    #Orders part:
    def order_invoice(orders):
        print("My Orders :")
        print(orders)

    print("**************")
    print("****Orders****")
    #If you press 1 it will redirect to the User Order page:
    order_now=int(input("Yes means Press 1:"))
    if order_now==1:
        #Redirect to the order page
        orders = user_orders()
        #Redirect to the Invoice generator
        order_invoice(orders)
        
    else:
        print("Thanks for Visiting!")
   

#Admin 
#Add New Item in the list:
def add_new_item(repasts):
    print("@Add New ",repasts)
    food_In = input("Enter the item name: ")
    price_In = input("Enter the Price of the Food: ")
    quantity_In = int(input("Enter the Quantity: "))
    repasts_In = repasts
    if quantity_In > 0:
        availability_In = "Yes"
    else:
        availability_In = "No"

    #Database interaction part:
    conn = db_connection()
    mycursor = conn.cursor()
    try:
        #New item will be inserted
        mycursor.execute("INSERT INTO Menu (food_item,availability,repasts,quantity,price) VALUES (%s,%s,%s,%s,%s)",(food_In,availability_In,repasts_In,quantity_In,price_In))
        conn.commit()
        conn.close()
        print("Item Added successfully!")
        #after insertion redirects to the Admin menu page
        admin_menu()
    except mysql.connector.Error as err:
        print(f"Error while inserting a new item: {err}")
    


#Admin menu page
def admin_menu():
    print("@Admin Menu")
    conn = db_connection()
    mycursor=conn.cursor()
    print("Press: 1 Breakfast")
    print("Press: 2 Lunch")
    print("Press: 3 Snacks")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("***@Breakfast Section***")
        #Retrieves all the Breakfast items:
        mycursor.execute("SELECT food_item,availability,quantity,price FROM Menu WHERE repasts='breakfast'")
        result=mycursor.fetchall()
        print("['Food' ,'availability' ,'Quantity', 'Price' )]")
        for row in result:
            print(result)

        #Add New item:
        print("Press 1: to insert the new item in the menu")
        print("Press 2: to go back to the Home Menu")
        add_item=int(input("Enter your opinion :"))
        if add_item == 1:
            repasts = "breakfast"
            #redirects to the add new item page
            add_new_item(repasts)
        else:
            #redirects to the Home Menu page
            admin_menu()

    elif choice == 2:
        print("***@Lunch Section***")
        #Retrieves all the lunch items:
        mycursor.execute("SELECT food_item,availability,quantity,price FROM Menu WHERE repasts='lunch'")
        result=mycursor.fetchall()
        print("['Food' ,'availability' ,'Quantity', 'Price' )]")
        for row in result:
            print(result)

        #Add New item:
        print("Press 1: to insert the new item in the menu")
        print("Press 2: to go back to the Home Menu")
        add_item=int(input("Enter your opinion :"))
        if add_item == 1:
            repasts = "lunch"
            #redirects to the add new item page
            add_new_item(repasts)
        else:
            #redirects to the Home Menu page
            admin_menu()

    else:
        print("***@Snacks Section***")
        #Retrieves all the Snacks items:
        mycursor.execute("SELECT food_item,availability,quantity,price FROM Menu WHERE repasts='snacks'")
        result=mycursor.fetchall()
        print("['Food' ,'availability' ,'Quantity', 'Price' )]")
        for row in result:
            print(result)
        #Add New item:
        print("Press 1: to insert the new item in the menu")
        print("Press 2: to go back to the Home Menu")
        add_item=int(input("Enter your opinion :"))
        if add_item == 1:
            repasts = "snacks"
            #redirects to the add new item page
            add_new_item(repasts)
        else:
            #redirects to the Home Menu page
            admin_menu()



#Commom menu function:
def menu(user_type):
    print("Menu")
    if user_type == 1:
        #redirects to the user menu
        user_menu()
    else:
        #redirects to the admin menu
        admin_menu()

#UI starts here :    
print("1:Press if you are a User")
print("2:Press if you are a Admin")

User_or_Admin=int(input("Enter your Identity:"))

#User type is globally defined here:
user_type = User_or_Admin
#End User Interface is defined below:
if User_or_Admin == 1:
    print("Welcome User")
    approval=User_Authentication() # type: ignore
    if approval:
        print("User Authorized")
        #redirect to user menu page
        menu(user_type)
    else:
        print("Not Authorized")
        print("Press 1: If forgot password")
        print("Press 2: If you are a new user")
        #Option for changing the password
        change = int(input("Press:"))
        if change == 1:
            #Redirect to the forgot password page
            #where we can reset the password for the available user
            result = forgot_password(user_type)
            if result:
                print("New Password has been updated [:) ")
                print("***Try Login***")
                approval=User_Authentication()
                if approval:
                    menu(user_type)
            else:
                print("User Not found")
        elif change == 2:#Redirects to the signin part
            signin=User_Signin()
            if signin:
                print("Try login again")
                #If signin was successfull then it will redirects to authentication page
                approval=User_Authentication()
                if approval:
                    menu(user_type)
                else:
                    print("Not Authorized")
        else:
            print("Thank you!")



#Admin Interface starts here
elif User_or_Admin == 2:
    print("Welcome Admin")
    approval=Admin_Authentication()
    if approval:
        print("Authorized Admin")
        #call the Admin Menu page
        menu(user_type)
    else:
        print("Not Authorized")
        #Option for changing the password
        print("Forgot Password ?")
        change_password = int(input("Press 1: To change the password:"))
        if change_password == 1:
            #Redirect to the forgot password page
            #where we can reset the password for the available user
            result = forgot_password(user_type)
            if result:
                print("New Password has been updated [:) ")
                print("***Try Login***")
                approval=Admin_Authentication() 
                if approval:
                    menu(user_type)
                else:
                    print("Not Authorized")
                # if the user is not there
                # then need to reachout to the Sercive team 
                # because the user cannot add himself as a admin                 
            else:
                print("User Not found")
                print("Please reachout to the Service Desk")
                print("Contact: +91 9597324119")    
else:
    print("Thanks for Visiting!")

