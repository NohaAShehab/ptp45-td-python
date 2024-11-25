

course = 'python'
print("*************** local variables **********************************")

def askforEmail():
    email = input("Enter your email: ")
    print(f"from inside the function  email = {email}")

askforEmail()

print(email)
print("-------------------------------------")