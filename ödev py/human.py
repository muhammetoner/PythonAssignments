class Human:
      name  ="muhammet"
      #built-in  hazır fonsiyon 
      def __init__(self,name):# nesne üretildigi an bu yapıcı bulok çalışacak 
            self.name=name
            print("bir human instance'i üretildi")
      def __str__(self):
            return f"STR  Fonksiyonundan  dönen değer : {self.name}"
      
      def talk(self,sentence):#python da klasın içindeki fonsiyon bir paramtere almak zorundadır self rezeve parametresi bi nevi gerklilik diyebiliriz
            print(f"{self.name} {sentence}")#self.değişken  bu bi nevi statce gibi 
           # self.walk() fonksiyonlar içerisinde class içindeki diger alanlara erişmek için yardımcı oluyor .self klası 
      def walk(self):
            print("Human is walking..")