# Python-letsupgrade

#python program for sum of n natural numbers



num=eval(input("enter numbers"))
if num<0:
    print("enter positive numbers")
else:
    while num>0:
        sum1=0
        sum1=num*(num+1)/2
        print("The sum of number is",sum1)
        break
        

-------------------------------------------------------------------
-------------------------------------------------------------------


#python program for to find intger prime numbers


lower=int(input("enter lower range"))
upper=int(input("enter upper range"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
            else:
                print(num)
