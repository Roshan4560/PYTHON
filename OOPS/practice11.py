# class method = a class method is a bound to the 
# class and receives the class as an implicit first argument

# note = static method can't access or modify class state and generally for  utility 
# class student 
# @classmethod # decorator
# def college(cls):
#     pass


class Person:
    name = "Anonymous"

    # def ChangeName(self, name):
    #     # Person.name = name  #  this is a type to change their name withput creating an instance
    #     self.__class__.name = "Roshan"  # this is a type to change their name withput creating an instance

    @classmethod
    def ChangeName(cls, name):
        cls.name = name  # this is a type to change their name withput creating an instance

p1 = Person()
p1.ChangeName("Roshan")
print(p1.name)
print(Person.name) # class variable