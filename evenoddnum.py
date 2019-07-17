#Even Odd Program
n = int(input("Enter the number:"))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
             break
        print(n,"is prime")
    else:
        print(n,"is composite")
