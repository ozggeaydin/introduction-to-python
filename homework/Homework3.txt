print("Name/Surname: Özge Nur Aydın", "Email: ozgeaydiin@gmail.com", "Homework3", sep= "\n")

def prime_first(): 
  asal1 = []
  for i in range(0,501):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
          asal1.append(i)
  
  print(asal1)

print("0'dan 500'e kadar olan asal sayılar: ")

prime_first()

def prime_second():
  asal2 = [] 
  for i in range(501,1001):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
          asal2.append(i)
  print(asal2)

print("501'den 1000'e kadar olan asal sayılar: ")
prime_second()
