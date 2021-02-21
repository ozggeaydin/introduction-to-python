import random

class Hangman():
  

  def __init__(self, kelimeler):
    self.kelimeler =  kelimeler

  def kelimesec(self):
    self.kelime = random.choice(self.kelimeler)
    self.sayac = len(self.kelime)+1
    print("Tahmin hakkınız:", self.sayac)

  def display(self):
    self.son_kelime = "-"*len(self.kelime)
    self.son_kelime = list(self.son_kelime)
    print("Kelime: ", " ".join(self.son_kelime), end = "\n")

  def play(self):
    while self.sayac > 0:
      tahmin = input("Bir harf giriniz: ")
      tahmin = tahmin.lower()

      if tahmin not in self.kelime:
        self.sayac -= 1
        print(f'Kelime bu harfi içermiyor! Kalan hakkınız {self.sayac} ')

      else:
        for i in range(len(self.kelime)):
          if tahmin == self.kelime[i]:
            self.son_kelime[i] = tahmin
        print(' '.join(self.son_kelime), end='\n')

  def kaybettin(self):
    if self.sayac ==0:
      print("Tüm haklarınız bitti!!")


game = Hangman(["silgi","kitap","defter","sıra","makas","kalem","kalemtıraş","öğrenci","öğretmen"])

game.kelimesec()
game.display()
game.play()
game.kaybettin()



  
