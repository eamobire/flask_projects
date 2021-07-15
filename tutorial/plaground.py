"""Understanding Decorators"""


# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#     def authenticator_decorator(function):
#         def wrapper(*args,**kwargs):
#             if args[0].is_logged_in:
#                 function(args[0])
#         return wrapper
#
#
#
#     @ authenticator_decorator
#     def create_blog_post(user):
#         print(f"This is {user.name}'s first blog post")
#
#
# new_user = User("Enoch")
# new_user.is_logged_in=True
# new_user.create_blog_post()

def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(1, 2, 3)

# def bold_decorator(function):
#     def wrapper():
#         print(f"<b>{function}</b>")
#
#     return wrapper
#
# @ bold_decorator
# def tag():
#     return "Hello"
#
# tag()
