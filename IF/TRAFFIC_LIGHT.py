# WAP to make and show the traffic lights colours 

light = input("Enter the colour of the light : ")
print(light)

# Enter the colour name in capital letters 
if(light == "RED"):
    print("STOP")
elif(light == "YELLOW"):
    print("WAIT AND LOOK")
elif(light == "GREEN"):
    print("GO")
else:
    print("LIGHT IS BROKEN")