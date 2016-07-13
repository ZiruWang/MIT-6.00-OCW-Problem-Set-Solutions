# Matching Strings

from string import *

target = "atgacatgcacaagtatgcat"
key = "atgc"

def countSubStringMatch(target,key):
    n = 0;
    count = -1;
    start = 0;
    while(n != -1):
        count += 1;
        n = find(target,key,start);
        start = n + 1;
        # print n;

    return count

# print find(target,key,0)
print countSubStringMatch(target,key)


def countSubStringMatchRecursive(target,key):
    start = find(target,key);
    if start == -1:
        count = 0;
    else:
        target = target[(start+1) : -1];
        count = countSubStringMatchRecursive(target,key) + 1;

    return count

print countSubStringMatchRecursive(target,key)
