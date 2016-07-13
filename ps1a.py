# 1000th Prime

count = 1;
candidate = 3;

while(count < 1000):
    n = 1;
    flag = 1;
    while(flag != 0 and (2*n + 1) < candidate):
        flag = candidate % (2*n + 1);
        n = n + 1;
    
    if flag != 0:
        count = count + 1
        print ('No.'+ str(count) + ' is ' + str(candidate))
        # print count
    candidate = candidate + 2;
    
    
