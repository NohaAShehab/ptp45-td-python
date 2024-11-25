

# any variable defined inside the python module ===> global variable

stdname= 'moaz' # this is a global variable


### any variable defined inside a function --> local variable

def beststudent():
    student='Moaz Salem' # student is local variable
    print(student)


####################################################################3

# 1- I need access global variable from inside the function

# 1.1-I need to read the variable ??

country = "Egypt"

def printCountryInfo():
    print(country)  # read value of the global variable

# printCountryInfo()

##### 1.2 I need to modify the global variable

def modifyCountry():
    global country # use parent the .py file or the script
    country="USA"
    print(f"From inside the function {country}")

# modifyCountry()
# print(f"After calling the modifyCountry function :country= {country}")

print("****************************** function inside a function *****************")

# 2.1 --> read local variable from  inner function
def lunch_info():
    main_dish = 'Ads'  # local

    def printMainDish():
        # read the local variable from inner function
        print(f"Our maindish is {main_dish}")

    printMainDish()

# lunch_info()
################################################################
def lunch_info():
    main_dish = 'Ads'  # local

    def modifmaindish():
        nonlocal main_dish # use when parent is a function
        main_dish = "penna white sauce"
        print(f"My dish is {main_dish}")

    print(f"the default is {main_dish}")
    modifmaindish()
    print(f"Main dish is {main_dish}")
lunch_info()















