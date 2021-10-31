def fizzBuzz(n):
    for i in range(1,n+1):
        op = ""
        if (i % 3 == 0):
            op += "Fizz"
        if(i % 5 == 0):
            op += "Buzz"

        if(op == "" ) : print(str(i))
        else: print(op)

def fizzBuzzRecursive(n,count = 1):
    if count > n :
        return
    op = ""
    if (count % 3 == 0):
        op += "Fizz"
    if(count % 5 == 0):
        op += "Buzz"
    if(op == "" ) : print(str(count))
    else: print(op)

    fizzBuzzRecursive(n,count+1)

# One line solution
# for i in range(1, 16): print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i))

# Calling funtion and using if else

# Fizz Buzz Recursive
fizzBuzzRecursive(15)