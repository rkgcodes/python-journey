
def main():
    n= get_int("What's x? ")
    print(f"The value of x is {n}")


def get_int(prompt):
    while True:
        try:
           return int(input(prompt))
   

        except ValueError:
            pass

        
        

main()