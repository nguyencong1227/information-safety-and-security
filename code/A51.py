import numpy as np
x = np.random.randint(2, size=6)
y = np.random.randint(2, size=8)
z = np.random.randint(2, size=9)
print (x)
print (y)
print (z)

def maj (x, y, z):
    if (x == 0 and y == 0) or (x == 0 and z == 0) or (y == 0 and z == 0):
        return 0
    else : 
        return 1
    
keys = []

for i in range (3):
    m = maj(x[1], y[3], z[3])
#     print (m)
# or x[0] = t, then append x[i] into new X (till n - 1)
    if (x[1] == m):
        t = x[2]^x[4]^x[5]
        for i in range (len(x) - 1, 0, -1):
            if (i == 0):
                x[i] = t  
            else :
                x[i] = x[i - 1]
    if (y[3] == m):
        t = y[6]^y[7]
        for i in range (len(y) - 1, 0, -1):
            if (i == 0):
                y[i] = t  
            else :
                y[i] = y[i - 1]

    if (z[3] == m):
        t = z[2] ^ z[7] ^ z[8]
        for i in range (len(z) - 1, 0, -1):
            if (i == 0):
                z[i] = t  
            else :
                z[i] = z[i - 1]
    key = x[len(x) - 1] ^ y[len(y) - 1]^z[len(z) - 1]
    keys.append(key)
print (keys)