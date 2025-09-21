#  create a new file and add the following data in it
# Hi everyone
# we are learning File I/O
# using java
# I like programming in java

with open("demo1.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using java\n")
    f.write("I like programming in java\n")
    # f.close()  # no need to close the file explicitly when using 'with' statement

with open("demo1.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")  # replace java with python
print(new_data)  # print the modified data

word = "learning"
if word in data:
    print(f"{word} is present in the file")