test1=float(input("enter the marks in first test"))
test2=float(input("enter the marks in second test"))
test3=float(input("enter the marks in third test"))

if(test1<=test2 and test1<=test3):
    avg=(test2+test3)
if(test2<=test1 and test2<=test3):
   
    avg=(test1+test3)
if(test3<=test1 and test3<=test2):
    
    avg=(test2+test1)

print("the average of best two is ")
print(avg)
