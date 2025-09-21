# WRITE MODE
# for more go stackoverflow.com
# 'w' is used to open the file in write mode,truncating the file first

# f = open("demo.txt", "a")
# f.write("This is a new line.\n")
# f.write("This is another new line.\n")
# f.close()   # go and check the demo.txt(ex = other file name) file


# f = open("demo.txt", "r")
# data = f.read()
# print(data)



#      other method to write a file

with open("demo.txt", "a") as f:
    f.write("This is a new line.\n")
    f.write("This is another new line.\n")
    # f.close()  # no need to close the file explicitly when using 'with' statement


with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    # f.close()  # no need to close the file explicitly when using 'with' statement