

                           #Flavyne Tsongwain
                                  #ANS2

import random
import numpy as np

# A and B from part 1 (let's learn numpy).
A = np.random.rand(3, 3) * 255
B = np.random.rand(3, 3) * 255

print(f" {np.matmul(A, B)}")

# ((A^T)(BA)
print("1c: \nA^T * BA^-1 yeilds:")
a_trans = A. transpose()
AB_trans = np.matmul(a_trans, B)
inverted_A = np.linalg.inv(A)
print(np.matmul(AB_trans, inverted_A))


print("1d:")
Av = np.reshape(A, (9, 1))
Bv = np.reshape(B, (9, 1))
print(f"Av:\n{Av}\n")


Cv = np.concatenate((Av, Bv), axis=1)
print("Cv:")
print(Cv)
cv_norm = np.sum(np.power((np.linalg.norm(Av)-np.linalg.norm(Bv)),2))
print ("Cv")





import random
import numpy as np


def new_line():
    print("\n")


# Step 1
A = np.random.rand(3, 3) * 255
B = np.random.rand(3, 3) * 255

print(f"1a: \nMatrix multiplication yields: \n{np.matmul(A, B)}")
new_line()

print(f"1b: \nElement-wise multiplication yields: \n{np.multiply(A, B)}")
new_line()

print("1c: \nA^T * BA^-1 yields:")
a_trans = A.transpose()
AB_trans = np.matmul(a_trans, B)
inverted_A = np.linalg.inv(A)
print(np.matmul(AB_trans, inverted_A))
new_line()

print("1d:")
Av = np.reshape(A, (9, 1))
print(f"Av:\n {Av}\n")

Bv = np.reshape(B, (9, 1))
print(f"Bv:\n {Bv}\n")

Cv = np.concatenate((Av, Bv), axis=1)
print("Cv:")
print(Cv)
cv_norm = np.concatenate((Av,Bv), axis = 1)
print("Cv Norm:")
print(cv_norm)
new_line()

print("2:")
I = np.random.rand(256, 256) * 255
M = np.random.rand(256, 256) * 255

for row in range(len(M)):
    for col in range(len(M)):
        M[row][col] = random.randint(0, 1)

for row in range(len(M)):
    for col in range(len(M)):
        if M[row][col] == 0:
            I[row][col] = M[row][col]
M = np.array(M)
print(I)


