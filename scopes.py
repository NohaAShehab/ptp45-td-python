# any variable defined in the python script --> global variable (can be accessed anywhere in the script)
course = 'python'

print("----------------------")

print(course)  # read value

print("---------------------------")

course = "Python"  # modify the value

print(f"--  at the end course = {course}")
################################################################################

# what will happen when I try to read the global variable from inside the function

def printCourse():
    print(f"from inside the function  course = {course}")


printCourse()

##################################### local variables
print("*************** local variables **********************************")
# any variable defined inside a function === local variable ?
# can be accessed only inside the function
def askforEmail():
    email = input("Enter your email: ")
    print(f"from inside the function  email = {email}")

# askforEmail()

# print(email)

###############################################
def sumnum(num1, num2): # num1, num2 are local
    res = num1 + num2  # num1, num2 are local variables can be accessed only inside the function
    print(f"from inside the function  sumnum = {res}")
    return res


res = sumnum(4,4) # this is new global variable
print(res)







#########################
# i need to modify the global variable from inside the function

print(f"before calling the function --> course= {course}")
def modifyCourse():
    course = "Houidini"
    print(f"course = {course}")


# modifyCourse()
# print(f"after calling the function course = {course}")


# I need to tell the interpreter please update the global variable
# please don't create new local one ??

course = "python"
def updateCourse():
    ### please don't create new local variable --> use the global
    global course  # use the global variable don't create new variable
    course = "Houidini"
    print(f"course = {course}")

updateCourse()
print(f"course after update = {course}")
















