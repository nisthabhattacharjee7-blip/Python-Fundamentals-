i = 1                                            #1

while(i<51):
    print(i)
    i+= 1    # i = i+1



for i in range (100):                            #2
    if (i == 34):
        break #Exit the loop right now 
    print(i) 

for i in range (100):                            
    if(i == 34):
        continue   #skip this iteration 
    print(i)
   





for i in range(1, 101, 1):                       #4
    print(i, end=" ")
    if (i == 50):
        break
    else:
        print("Mississippi")
print("Thank you")