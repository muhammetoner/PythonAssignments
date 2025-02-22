from human import Human


faiz=1.59
vade ="36" 
krediAdi="ihityiac kredisi"

print(int(vade)+12)
#değişkenleririn tipinin konsola yazdıra biliyoruz 
print(type(faiz))
print(type(vade))
 #değişken türünü  değiştirmek isitedegimiz vakit
 # değiştirdimek istedğimiz  değişkenin başına dönüştürmek istedeğimiz
 #  veri türünü yazmamız gerek
print(int(vade)+12 )
faiz=str(faiz)
print(type(faiz))

vade =34#int(input("lütfen istediğiniz vade sayısını giriniz : "))
print(type(vade))
print(vade + 12)
vade =vade+12

# string interpolation
# seçtiğiniz vade sonucu ortaya çıkan vade:
print("seçtiğiniz  vade sonucu  ortaya çıkan vade : " +str(vade))
print("seçtiğiniz  vade sonucu  ortaya çıkan vade :  {vadesayisi} ".format(vadesayisi=vade))

isim="halit"
metin= "merhaba{name}".format(name="samet")
print(metin)
# süsülü parantez için de kullandıgımız  değişken ismi bize ait istediğimiz adı ekleyebiliriz
#f- string 
metin =f"hoşgeldiniz  {1+1}"
print(metin) 
#listeler 
# döngüler
#fonksiyon 

krediler= ["ihtiyac Kredisi", "taşıt kredisi", "konut Kredisi"]
print(type(krediler[0])) 
#eleman sayısına 1 den indeks sayısına 0 dan başlıyacagız
print(len(krediler))#length uzunluk için 
#print(krediler[3])=> hata veriri
dizi=["ihitiyac kredisi",10,5.2,True]
print(dizi)
# .append listenin  son son indeksine eleman eklemek için kullanılır 
krediler.append("x kredisi")
print(krediler)

#.pop  liste den eleman silmek için kullanılır  eger .pop( )yazarsan herzaman son indeksi siler
krediler.pop()
print(krediler)
krediler.pop(0)
print(krediler) 
#remove index ile değil de deger bazlı çalışıyor indekx sırasına göre buldugu ilk değeri siler

krediler.remove("taşıt kredisi")
print(krediler)

# extend metodu bir den fazla degeri tek satrıda eklemeize yarar 
krediler.extend(["Y Kredisi ", "Z kredisi"])
print(krediler)
#for
#i=0  i<10
for i in range(10):
      print(i)
print("**************")
# range birinci eleman başlangıç elmanım dır 
#  ikinci elaman varış elemanımdır  üçüncü elamanım ise ilgili i elamanın kaçar kaçar artacagını belirler
for i in range(0,11):
      print(i)
print("****************")
for i in range( 0,51,5):
      print(i)
print("**************")

krediler= ["ihtiyac Kredisi", "taşıt kredisi", "konut Kredisi"]
for kredi in krediler:
      print(kredi)
print("**************") 
for  i in range(len(krediler)):
      print(krediler[i])
print("************")
i=0
while i<10:
      print("x")
      i+=1
print("*******")
i=0
while i<10:
      print("x")
      break
print("*********")
krediler= ["ihtiyac Kredisi", "taşıt kredisi", "konut Kredisi"]
i=0 
while i<len(krediler):
      i+=1
      print(i)
      print(krediler[i])
      if krediler [i]== "konut Kredisi":
            break
#fonksiyonlar
# fonksiyon çagırmak için def komutu kullanılır
def calculate ():
      print(100*2)
def calculateWithparamas( fiyat,indirim):
      print(fiyat-indirim)
def sayhello(name):
    print(f"Merhaaba{name}")
calculate()
calculateWithparamas(50,10)
calculateWithparamas(100,30)
sayhello("halit")
sayhello("mehmet")
sayhello("muhammet")
def calculateAndReturn(fiyat,indirim):
      return fiyat-indirim
yenifiyat= calculateAndReturn(200,50)
print(yenifiyat)
print("******************")

#sınıflar => classslar 
#modules
# paket yönetimi

# intance=> örnek
human1=Human("mert")
human1.talk("merhaba")
human1.walk()
print(human1)

human2=Human("hakan")
human2.talk("merhaba")
human2.walk()
print(human2)
human3=Human("can")
human3.talk("sellamunaleyküm")
human3.walk()


