# Selling McNuggets

x = 6;
y = 9;
z = 20;
a = 0;
b = 0;
c = 0;

for total in range(50,56):
    for a in range(0,total/x + 1):
        for b in range(0,total/y + 1):
            for c in range(0,total/z + 1):
                if (a*x + b*y + c*z == total):
                    print total, ' = 6 x' , a, ' + 9 x', b, ' + 20 x', c


# x, x + 1, x + 2, x + 3, x + 4, x + 5
# 6, 9, 20

# (x + 6 : x + 11) = (x : x + 5) + 6
# (x + 9 : x + 14) = (x : x + 5) + 9
# (x + 12 : x + 17) = (x : x + 5) + 6 + 6
# (x + 15 : x + 20) = (x : x + 5) + 6 + 9
# (x + 20 : x + 25) = (x : x + 5) + 20

# The combination of 1, 2, 3, 4, 5, 6 can cover all the number between 1 to 10
# i.e. Any integer n = a + 2b + 3c + 4d + 5e + 6f

                    
