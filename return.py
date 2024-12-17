#return 
s_username="john"
s_password="123"
Username=input("username:")
password=input("Enter the password:")
def validate_user():
    if(s_username == Username and s_password == password):
            return True
    else:
        return False

a=validate_user()
print(a)
