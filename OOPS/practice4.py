#  STATIC METHODS
# Static methods are methods that don't use the self parameter (work as a class level)

# syntax 
# class student:
#     @staticmethod    # decorator
#     def college():
#         print("Welcome to ABC college")


# decorator allow us to wrap another function in order to extend the 
# behavior of the wrapped function, without permanently modifying it.
# eg =

class Student:
    @staticmethod  # decorator
    def college():
        print("Welcome to ABC college")

    s1 = college()