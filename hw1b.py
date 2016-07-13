#The product of the Primes

from math import *

count = 1;
candidate = 3;

lgsum = log(2);
number = 10000;

while(candidate < number):
    n = 1;
    flag = 1;
    while(flag != 0 and (2*n + 1) < candidate):
        flag = candidate % (2*n + 1);
        n = n + 1;
    
    if flag != 0:
        count = count + 1
        # print ('No.'+ str(count) + ' is ' + str(candidate))
        # print count
        lgsum = lgsum + log(candidate);
        #print str(count) + ' ' + str(lgsum) + ' ' + str(lgsum/count)  
        
    candidate = candidate + 2;

print str(number) + ' ' + str(lgsum) + ' ' + str(lgsum/number)  
    
