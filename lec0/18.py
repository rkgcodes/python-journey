#demonstrates defining a function with parameter with a default value

def hello(to="World"):
        print("hello, "+ to)


hello()
name= input("What's your name? ").strip() .title()
user_name=name.split()
hello(user_name[0])
