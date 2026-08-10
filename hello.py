def main():
    num = int(input("What's the number to square? "))
    y= square(num)
    print("square of the number" , num, "is" , y)
    
def square(n):
    return (n*n)


main()