#used to open a file or set DB connections and close them even if there are syntax errors
# it is similar to try and finally block

file=open("notes.txt",'a')
try:
    file.write('python-selenium')
finally:
    file.close()

# the above code can be achieved by context manager
with open("notes.txt",'w') as file:
    file.write("selenium")

class MyContextManager:
    def __enter__(self):
        print("Initializing resources")
        # Initialize resources and return them
        return "Resource"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cleaning up resources")
        # Clean up resources if needed

# Using the context manager with the with statement
with MyContextManager() as resource:
    print("Working with resource:", resource)
