# def do_something(numb1: int, numb2: int, numb3 = 0, *args):
#     return numb1 + numb2 + numb3
#
#
# print(do_something(35, 58))
# print(do_something(35, 58, 68))
# print(do_something(35, numb3=58, numb2=68))
# print(do_something('35', '58'))
# print(do_something('35', '58'))
# print(print())

# Closure - замыкание

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


clicks = make_counter()

print(clicks())
print(clicks())
print(clicks())

