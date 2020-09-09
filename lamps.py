from array import *
lamp_array = array('i',[1] )
temp = 2
count = 0
flag = 1

# make array
while temp < 101:
    lamp_array.append(temp)
    temp += 1

# lamp off
lamp_array.reverse()
while True:
    lamp_array.reverse()
    for i in lamp_array:
        count += 1
        if count == 10: 
            lamp_array.remove(i)
            count = 1
            flag += 1
    if flag == 100:
        break

# show result          
for i in lamp_array:
    print(i)      
    
                
            

