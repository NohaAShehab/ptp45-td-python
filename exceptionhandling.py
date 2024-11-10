# try:
#     num = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     summm = num + num2
#     diff = num - num2
#     divv = num / num2
#     print(summm, diff, divv)
# except Exception as abbass:
#     print(f'error happened {abbass}')
#
#
#
# print("0000000000000000000000000000")
# print("0-----------------------------------")

######################3 prepare error
#
# message = input("Enter a message: ")
# if message =="break":
#     raise Exception("break word is not allowed")
#
# print("------------ this after the message ---------------")
#########################3

class BreakException(Exception):
    pass
message = input("Enter a message: ")
if message =="break":
    raise BreakException('Break is allowed 00000')












