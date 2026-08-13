#demonstrates defining a functio with a return value

def main():
   
   x=int(input("What's x? "))
   print("Square of x =",xsquared(x))
   

 
def xsquared(n):
   return(n*n)
      
main()