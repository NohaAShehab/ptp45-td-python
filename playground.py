newl = ["iti", 324,"iti", 234, 'fdsgdfg', 'esfsdfsdf', 'iti', 2424,42424,2 ]
# count = 0
# for item in newl:
#     if item=='iti':
#         newl.remove(item)
#     count += 1
#
# print(newl )
# print(f'------------------- {count}')

## while
count= 0
no_of_items = newl.count("iti")
while no_of_items > 0:
    newl.remove("iti")
    count += 1
    no_of_items = newl.count("iti")

print(count)