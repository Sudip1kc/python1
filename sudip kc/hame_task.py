user_data={"sudip":"123pass","fish":"456pass"}
u_balance={"sudip":500,"fish":50000}
daily_withdraw_limit={"sudip":5000,"fish":3000}
user_name=input("enter user name: ")
password=input("enter the password")
if user_name in user_data and user_data[user_name]==password:
    print(f"welcome {user_name}")
    print("The option:\n1.check balance,\n2.withdraw,\n3.deposit")
    option=int(input("enter the choice no:(1,2 or 3)"))
    
