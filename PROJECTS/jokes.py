# # AUTOMATIC JOKES IMPLEMENTATION

# import pyjokes

# joke = pyjokes.get_joke() 
# print(joke) 

# text to speech in audio 
# import pyttsx3
# engine = pyttsx3.init() 

# engine.say("Hello, Hello Roshan kumar")
# engine.runAndWait()



import os

# Specify the directory path (you can change it to any directory you want)
directory_path = "/coder/roshan"

# List the contents of the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of the directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access the directory '{directory_path}'.")