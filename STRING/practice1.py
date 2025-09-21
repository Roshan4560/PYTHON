#  STRING METHODS IN PYTHON


# 1.  basic operations 
str1 = "hello" + "Roshan"
print(str1)

# 2.   length of string
# In the length all things are counted eg = digits,letters,symbol,space etc 
print(len(str1))
str2 = "Roshan kumar chourasia"
print(str2[0],str2[3],str2[6],str2[9])

# 3.  string slicing
# In the string slicing we can get the specific part of the string
# eg = "ApnaCollege"   str[1:4] we get "pna"
# it also work in negative way eg = str[-5:-1]
str3 = "ApnaCollege"
print(str3[1 : 8])


# 4.  other strings are used in python
#   like
str.endswith("e") # check the string is end with "e" or not
# in this string we can use word or the letter

str.startswith("A") # check the string is start with "A" or not

str.capitalize() # it will convert the first letter of the string into capital letter

str.upper() # it will convert the all letter of the string into capital letter

str.lower() # it will convert the all letter of the string into small letter

str.replace("old","new") # it will replace the old word with new word

str.find("word") # it will find the word in the string and return the index of the first occurrence

str.count("word") # it will count the number of occurrence of the word in the string