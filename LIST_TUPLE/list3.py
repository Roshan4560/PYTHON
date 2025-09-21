# WAP to check if a list contains a palidrome of elements .

list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", 3, 4, "abc", 1]

list1_copy = list1.copy()
list1_copy.reverse()
if(list1 == list1_copy):
    print("List1 is a palindrome")
else:
    print("List1 is not a palindrome")


list2_copy = list2.copy()
list2_copy.reverse()
if(list2 == list2_copy):
    print("List2 is a palindrome")
else:
    print("List2 is not a palindrome")