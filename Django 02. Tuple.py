# tpl = (2, 89, 78, 28, 97)

# for i in range(len(tpl)):
#     print(tpl[i], end=' ')

# for i in tpl:
#     print(i, end=' ')

# numb1, numb2 = 25, 98
#
# print(f"numb1 = {numb1}, numb2 = {numb2}")
# temp = numb1
# numb1 = numb2
# numb2 = temp

# numb1 = numb1 + numb2
# numb2 = numb1 -  numb2
# numb1 = numb1 - numb2

# numb1, numb2 = numb2, numb1
#
# print(f"numb1 = {numb1}, numb2 = {numb2}")

# return multiple values
# def foo():
#     return 45, 89, 891
#
# print(type(foo()))
# a, b, c = foo()
#
# print(f"{a} {b} {c}")


# def bar(*args):
#     print(type(args))
#     for i in args:
#         print(i)
#
#
# def bar2(**kwargs):
#     print(type(kwargs))
#     # for i in args:
#     #     print(i)
#
# bar(15, 87, 98, 77, 771)
#
# bar2(a=5, b="Salam", salam=True)


tpl1 = (2, 89, 78, 28, 97)

tpl1 = tuple(sorted(tpl1))

print(tpl1)
