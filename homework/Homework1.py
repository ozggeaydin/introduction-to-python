
import random as rnd
 
print("Name/Surname: Özge Nur Aydın", "Email: ozgeaydiin@gmail.com", "Subject of Homework1: Generating a 3x3 matrix with 9 random prime number with using for loop.", sep= "\n")

asalsayilar = []

for i in range(2,1000):
  asal = 0
  for j in range(2,i):
    if (i%j==0):
      asal += 1

  if asal==0:
    asalsayilar.append(i)
asalsayilar

matrix = [[[],[],[]], [[],[],[]], [[],[],[]]]


for i in matrix:
  for j in i:
    j.append(rnd.choice(asalsayilar))

print("The result is: ")
for i in matrix:
  print(i)

print("Run the code again to see different matrices!")
  