# Write a recursive function to print all the elements in a list
# hint : use list & index as parameters

list = [1, 2, 3, 4, 5, 12.4, 3.4, 5.6, "Ram", "Shyam", "Mohan"]

def print_list_elements(list, index=0):  # to print all the elements in a list
    if index < len(list):  # base case
        print(list[index])  # print the current element
        print_list_elements(list, index + 1)  # recursive case
    else:
        return
    
print("The elements in the list are:")
print_list_elements(list)
# 1 2 3 4 5 12.4 3.4 5.6 Ram Shyam Mohan