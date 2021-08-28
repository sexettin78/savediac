import time,sys,random

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')


print("""\033[96m\nUzun zaman önce Zordiac adlı bir asker vardı.Bu diyarda vatan görevi uzun sürüyordu o yüzden 3 yıldır ailesini ve memleketini görememişti.
Memleketine geldiğinde birde baktı ki heryer ne olduğu belirsiz canlılar tarafından basılmıştı.Evinde bir not buldu,not içerisinde 'patikanın sonundaki mağaraya gel.' yazıyordu.
Mağaraya gitti ve onu bir goblin elinde bıçakla karşıladı... Yaşamak için Dövüş! \n""")


print("""
Bıçaklı Goblin;
Vuruş : 2
Can : 4
Enerji : 25
Ekipman : Bıçak

******************

Zordiac;
Vuruş : 1
Can : 10
Enerji : 100
Ekipman : Yumruk

Rakibin canı veya enerjisi 0 altına inerse veya puanınız 100 olursa kazanırsınız.Aynısı rakip için de geçerli
""")

def nokta_ekle():
    print(".")
    time.sleep(0.4)
    print("..")
    time.sleep(0.4)
    print("...")
    time.sleep(0.4)


class oyuncu():
    def __init__(self,isim,can=10,power=100,puan=0):
        self.isim = isim
        self.can = can
        self.power = power
        self.puan = puan
        
    def bilgileri_goster(self):
        print("""
        Karakter: {}
        Can: {}
        Enerji: {}
        Puan: {}
        """.format(self.isim,self.can,self.power,self.puan)) 

        
    def saldir(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            dusman.power -= 8 
            self.power -= 4
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 2
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSaldırı Başarısız")

    def  savun(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            self.power -= 4
            dusman.power -= 8
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSavunma Başarılı")
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 2
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSavunma Başarısız")

    def saldir_savun_sayi(self):
        return random.randint(1,2)

    def exit(self):
        print("Oyun Kapatılıyor...")
        nokta_ekle()
        sys.exit()

    


oyuncu1 = oyuncu("Zordiac")
oyuncu2 = oyuncu("Bıçaklı Goblin")




nokta_ekle()

while True:
    hamle = input("""
    1-Saldır
    2-Savun
    3-Çık
    Hamle Seçimi:
    """)
    if(hamle=="1"):
        oyuncu1.saldir(oyuncu2)

    elif(hamle=="2"):
        oyuncu1.savun(oyuncu2)
    elif(hamle=="3"):
        oyuncu1.exit()
    else:
        hatali_eksik()


    if(oyuncu1.puan==100 or oyuncu2.can <= 0 or oyuncu2.power <= 0 ):
        print("\033[92m\nOyunu Kazandın! Hikaye devam ediyor...")
        break
    if(oyuncu2.puan==100 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        print("\033[91m\nOyunu Kaybettin,Bir gobline yenildin! >:( ")
        break

    if(oyuncu2.can == 10 or oyuncu2.can == 9):
        oyuncu2.can -= 7
        oyuncu2.power -= 75
         
