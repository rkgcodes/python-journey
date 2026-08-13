#demonstrates defining a function with parameter

def hello(to):
        print("hello, "+ to)

name= input("What's your name? ").strip() .title()
user_name=name.split()
hello(user_name[0])
