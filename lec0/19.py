#demonstrates defining a main function

def main():
    name= input("What's your name? ").strip() .title()
    user_name=name.split()
    hello(user_name[0])

        

def hello(to):
        print("hello, "+ to)


main()