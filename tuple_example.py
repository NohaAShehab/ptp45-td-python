# data = (12, 45, 78, 23, 56, 89, 100, 34, 67, 90, 888)
# sorted_tuple = []
# for item in data:
#     if len(sorted_tuple) == 0:
#         sorted_tuple.append(item)
#     else:
#         if sorted_tuple[0] > item:
#             sorted_tuple.insert(0, item)
#         else:
#             sorted_tuple.append(item)
#
#
# print(sorted_tuple)
##################################33
data = (12, 45, 78, 23, 56, 89, 100, 34, 67, 90, 888)
sorted_tuple = [data[0]]

"""
    12 the min 
    
      12 , 23, 34,   45  , 56,  67,   78, 89, 90, 100


"""

#### each get min of the tuple
data = (12, 45, 78, 23, 56, 89, 100, 34, 67, 90, 888)

# l = []
# get min then --> compare with in the list ??
# minnum = data[0]
# counter = 0
# while counter < len(data):
#     minnum=data[counter]
#     for index in range(counter+1, len(data)):
#         if data[index] < minnum:
#             minnum = data[index]
#
#     l.insert(0, minnum)
#     counter += 1
#     print(minnum)
#
# print(l)
# ## accept next

data = (12, 45, 78, 23, 56, 89, 100, 34, 67, 90)
l=list(data)


for i in range(1, len(l)):
        num = l[i]
        j = i - 1
        while j >= 0 and l[j] > num:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = num

data=tuple(l)
print(data)








