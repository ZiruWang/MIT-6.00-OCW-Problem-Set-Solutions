###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (3,8,11)   # variable that contains package sizes


for n in range(1, 200):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
    flag = 0;
    for a in range(0,n/packages[0] + 1):
        for b in range(0,n/packages[1] + 1):
            for c in range(0,n/packages[2] + 1):
                if packages[0]*a + packages[1]*b + packages[2]*c == n:
                    flag = 1;
    if flag == 0:
        bestSoFar = n;

print 'Given package sizes',packages[0],',',packages[1],', and',packages[2],', the largest number of McNuggets that cannot be bought in exact quantity is:',bestSoFar
    
