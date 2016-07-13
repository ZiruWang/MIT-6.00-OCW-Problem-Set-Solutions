from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

target = 'ATGACATGCA';
key = 'A';


# Recursion may not work in this case because tuple is immutable. 

##def subStringMatchExact(target,key):
##    start = find(target,key);
##    if start == -1:
##        index1 = ();
##        return index1;
##    else:
##        index1 = (start,) + subStringMatchExact(target[(start+1):],key);
##        return index1


def subStringMatchExact(target,key):
    '''It returns a tuple of the starting points of matches of the key string
    in the target string, when indexing starts at 0'''
    index1 = ();
    start = 0;
    while(find(target,key,start) != -1):
        index1 = index1 + (find(target,key,start),);
        start = find(target,key,start) + 1;

    return index1



print subStringMatchExact(target,key)




    







            


