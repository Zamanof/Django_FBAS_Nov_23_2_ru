lst = [2, 89, 78, 28, 97]

# a = lst[1]
# a = 65
# print(lst)
#
# for i in lst:
#     i *= 10
#     print(i, end=' ')
#
# print()
#
# print(lst)

# print()
#
for i in range(len(lst)): # if length lst equal 5 return 0, 1, 2, 3, 4 -> for i in 0, 1, 2, 3, 4:
    lst[i]*=10
    # print(lst[i], end=' ')

print(lst)

print(list(range(len(lst))))