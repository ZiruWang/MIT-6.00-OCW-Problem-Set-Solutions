###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

#for n in range(1, 150):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar

count = 0;
n = 1;
while(count != 6):
    flag = 0;
    for a in range(0,n/packages[0] + 1):
        for b in range(0,n/packages[1] + 1):
            for c in range(0,n/packages[2] + 1):
                if packages[0]*a + packages[1]*b + packages[2]*c == n:
                    flag = 1;
    count += 1;
    
    if flag == 0:
        bestSoFar = n;
        count = 0;

    # print count, n, bestSoFar # Debug: trace
    n += 1;

print 'Largest number of McNuggets that cannot be bought in exact quantity:',bestSoFar
    
