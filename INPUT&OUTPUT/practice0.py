#  READING MODE
# 'w' is used to open the file in write mode,truncating the file first


f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# 'r' is used to open the file in read mode (default)
# 'w' is used to open the file in write mode,truncating the file first
# 'a' is used to open for writing, appending to the end of the file if it exists
# 'x' is used to create a new file and open it for writing
# 'b' is used to open the file in binary mode
# 't' is used to open the file in text mode (default)
# '+' is used to open a disk file for updatinig (reading and writing)


# if is am read n numbers of lines 
# line1 = f.readline()  # read first line from the file
# print(line1)


# line2 = f.readline()  # read first line from the file
# print(line2)
# f.close()


# if i want to read only n numbers of word from the file
# data = f.read(5)
# print(data)
# f.close()