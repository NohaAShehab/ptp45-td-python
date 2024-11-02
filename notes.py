

name = 'Ahmed'
print(type(name))

# types differs in size, ---> representation

# runtime --> change type ---> type casting ?

age = 22
print(type(age))

# convert it to string ?
age = str(age)  # convert int to string --> age
print(type(age))


############# convert int to bool
year = 2024
print(type(year), year)
year = bool(year)
print(type(year), year)


val = 0
print(type(val), val)
val = bool(val)
print(type(val), val)

#### convert int to bool --> int==0 --> False otherwise --> True


### 2- convert str to bool

# msg = "hi"
# msg = bool(msg)
# print(type(msg), msg)
print("iti")
msg = "                     "
msg = bool(msg)
print(type(msg), msg) # true

print("------------- hiiii ------------------")

#
# name = "Ahmed"
# name = int(name)  #run time error
# print(type(name), name)
#

message = "e"
import sys
print(sys.getsizeof(message))


###################

updated_message =" "
updated_message= updated_message.replace("$", "e", 1) #return new string
print(updated_message)




firstname=input("please enter yourname")  # always save userinput as string #
print(firstname, type(firstname))


















