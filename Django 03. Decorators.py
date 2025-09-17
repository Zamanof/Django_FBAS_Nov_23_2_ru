# Decorator syntax

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("Before")
#         print(args)
#         print(kwargs)
#         result = original_function(*args, **kwargs)
#         print(f"Function result: {result}")
#         print("After")
#         return result
#     return  wrapper_function
#
# @decorator_function
# def my_function(numb1, numb2):
#     return numb1 + numb2
#
# @decorator_function
# def other_function(numb1, numb2, numb3):
#     return numb1 * numb2 *numb3
#
#
# print(my_function(25, 69))
# # print(my_function(numb1=25, numb2=69))
# print(other_function(2, 3, 6))


# authenticate example
# def is_authenticate():
#     return False
#
#
# def check_authenticate(func):
#     def wrapper(*args, **kwargs):
#         if is_authenticate():
#             print("User is authenticate")
#             return func(*args, **kwargs)
#         else:
#             raise Exception("User is not authenticate")
#
#     return wrapper
#
#
# @check_authenticate
# def do_something():
#     print("Some operation")
#
#
# do_something()


# validate
def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int):
                raise ValueError(f"{arg} is not int")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def summ(a, b):
    return a + b

print(summ(a=2.5, b=6))

range()