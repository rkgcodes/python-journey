# demonstrate a function to cehck even and odd

def main():
    x=int(input("What's x? "))
    print(odd_even(x))



def odd_even(num):
    if (num%2==0):
        return("Even")

    else:
        return("Odd")

    
main()