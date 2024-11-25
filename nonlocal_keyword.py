
# define function inside  a function ===> yes ?
def salary_info():
    basic_salary = 1000  # local variable


    def print_salary_info():
        # me as inner function can read  the parent function variable
        print(f"the basic salary is {basic_salary}")

    # I need to call the child function
    print_salary_info()


# salary_info()

############3 2nd scenario


def grade_info():
    grade = 0 # local for the grade_info

    def modifygrade():
        grade = 90  # any variable defined inside a function -->new local variable for this function
        print(f'grade ={grade}')

    modifygrade()


    print(f"after modify grade is {grade}")


# grade_info()

###################### I need to modify local variable from inside the child function



def grade_info():
    grade = 0 # local for the grade_info

    def modifygrade():
        # I need to tell the interpreter plz don't create new local variable
        # please use the parents' one
        nonlocal grade
        grade = 90
        print(f'grade ={grade}')

    modifygrade()


    print(f"after modify grade is {grade}")


grade_info()





