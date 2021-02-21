class yemek():

  def __init__(self, yemekadı, malzemeler, kap):
    self.yemekadı = yemekadı
    self.malzemeler = malzemeler
    self.kap = kap
    print(f'{self.yemekadı} Tarifi')
    

  def miktarlar(self, miktar):
    self.miktar  = miktar
    self.malzeme = list(zip(self.malzemeler,self.miktar))
    print(f'{self.yemekadı} için gerekli malzemeler: {self.malzeme} ')

  def yapılış(self):
    print(f'{self.yemekadı} nasıl yapılır? ')

  def pisirme(self,dakika):
    self.dakika = dakika
    print("Daha sonra {} içinde yaklaşık {} dakika boyunca pişirin.".format(self.kap, self.dakika))

  def yagekle(self):
    print(f'{self.kap} içine zeytinyağı ekleyin.'.capitalize())

  def tuzekleme(self):
    print("Tuzu ekleyin.")

  def afiyetolsun(self):
    print("Afiyet olsun!")



class havuc_tarator(yemek):
  def __init__(self,yemekadı,malzemeler, kap):
    super().__init__(yemekadı, malzemeler,kap)

  def rendele(self):
    print(f'{self.malzemeler[0]}ları rendeleyin.'.capitalize())

  def soğut(self):
    print(f'Pişen {self.malzemeler[0]}ların soğumasını bekleyin. ')

  def yoğurtekle(self):
    print(f'Soğuyan {self.malzemeler[0]}lara yoğurt ekleyin. ')

class tavukSote(yemek):
    def __init__(self,yemekadı,malzemeler, kap):
       super().__init__(yemekadı, malzemeler,kap)


    def eti_dogra(self):
      print(f'{self.malzemeler[0]}nü kuşbaşı doğrayın.'.capitalize())

    def sogan_dogra(self):
      print(f'{self.malzemeler[1]}ı küp küp doğrayın.'.capitalize())

    def sogan_ekle(self):
      print("Tavuklar suyunu çektikten sonra {}ı ekleyin.".format(self.malzemeler[1]))

    def baharat_ekle(self):
      print("Ardından {}, {} ve {} ekleyin. ".format(self.malzemeler[2],self.malzemeler[3],self.malzemeler[4]))

class pilav(yemek):
  def __init__(self,yemekadı,malzemeler, kap):
    super().__init__(yemekadı, malzemeler,kap)

  def yıka(self):
    print("{}leri tuzlu suda 15 dakika bekletin.".format(self.malzemeler[0]).capitalize())

  def erit(self):
    print(f'{self.malzemeler[1]}ını {self.kap}de eritin.'.capitalize())

  def pirinç_ekle(self):
    print(f'{self.malzemeler[0]}leri ekleyin.'.capitalize())

  def su_ekle(self):
    print(f'{self.malzemeler[2]}yu ekleyin.'.capitalize())
  


     



yemek1 = havuc_tarator("Tarator", ["havuç", "yağ","tuz","yoğurt"], "tava")
yemek1.miktarlar(["7 adet", "3 yemek kaşığı", "1 çay kaşığı", "1 su bardağı"])
yemek1.rendele()
yemek1.yagekle()
yemek1.pisirme(10)
yemek1.soğut()
yemek1.yoğurtekle()
yemek1.tuzekleme()
yemek1.afiyetolsun()

print("  ")

yemek2 = tavukSote("Tavuk Sote",["tavuk göğsü","soğan","karabiber","kekik","kırmızı pul biber","tuz"],"tava")
yemek2.miktarlar(["500 gram","1 adet","1 tutam", "1 tutam","1 tutam","1 tutam"])
yemek2.eti_dogra()
yemek2.pisirme(5)
yemek2.sogan_dogra()
yemek2.sogan_ekle()
yemek2.baharat_ekle()
yemek2.tuzekleme()
yemek2.pisirme(15)
yemek2.afiyetolsun()

print("  ")

yemek3 = pilav("Pilav",["pirinç","tereyağ","sıcak su","tuz"],"tencere")
yemek3.miktarlar(["2 su bardağı","3 yemek kaşığı","2s su bardağı", "1 tatlı kaşığı"])
yemek3.yıka()
yemek3.erit()
yemek3.pirinç_ekle()
yemek3.su_ekle()
yemek3.tuzekleme()
yemek3.pisirme(15)
yemek3.afiyetolsun()