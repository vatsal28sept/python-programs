# Functions With **kwargs 
# Create A Function That Accepts Any Number Of Keyword Arguments And Prints Them In the Formet Key:Value 

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_kwargs(name="vatsal",lname="patel")
print_kwargs(bro="utsav",sis="patel")

