import time,sys,random,os

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')


print("""\033[96m\n İyileştirme gücünü tam anlamıyla kazanmıştın.Kendini iyileştirdikten sonra kuzeninin yanına gittin ve orada saatlerce düşündün.Aniden bir ses geldi mağara yıkılacak gibiydi!
Ne olduğunu anlamadan 2 tane varlık bana saldırmaya başladı birisi kovboy şapkası takan maymun diğeri ise üzerinde Menajer++ yazan bir tişört giyen insandı.Maymunu kontrol ediyordu,Bu canlı diğerlerinden daha güçlüydü.Bu bir oyunsa 
bölüm sonu gibiydi sanki.iskeletin baltasını aldım ve salırmaya başladım... Yaşamak için Savaş! \n""")


print("""
Menajer++;
Vuruş : 5
Can : 27
Enerji : 48
Ekipman : kovboymonki,İyileştirici(+12 can -18 enerji)

******************

Zordiac;
Vuruş : 4
Can : 15
Enerji : 70
Ekipman : İskeletin baltası,İyileştirici(+3 can,-8 enerji) 

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
    def __init__(self,isim,can=15,power=70,puan=0):
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
            dusman.can -= 4
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 5
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSaldırı Başarısız")
    def iyilestirici(self):
        self.can += 3
        self.power -= 8
        print("İyileştirme Başarılı +3 can eklendi! 8 enerji kaybettin")
    def  savun(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            self.power -= 4
            dusman.power -= 8
            self.puan += 10
            dusman.can -= 2
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSavunma Başarılı")

    
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 5
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
oyuncu2 = oyuncu("Menajer++")




nokta_ekle()

while True:
    hamle = input("""
    1-Saldır
    2-Savun
    3-İyileştiricini kullan
    4-Çık

    Hamle Seçimi:
    """)
    if(hamle=="1"):
        oyuncu1.saldir(oyuncu2)

    elif(hamle=="2"):
        oyuncu1.savun(oyuncu2)
    elif(hamle=="4"):
        oyuncu1.exit()
    elif(hamle=="3"):
        oyuncu1.iyilestirici()
    else:
        hatali_eksik()


    if(oyuncu1.puan==100 or oyuncu2.can <= 0 or oyuncu2.power <= 0 ):
        print("\033[92m\nMenajer++yı Yendin Hikaye devam ediyor...")
        time.sleep(3)
        #import bolum4
        break
    if(oyuncu2.puan==100 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        hsec = input("\033[91m\nOyunu Kaybettin,Menajer++ya yenildin! Önceki bölüme Baştan başlamak ister misin? e/h ")
        print("Kaybedersen 1 önceki bölümden başlarsın.")
        if(hsec=="e" or hsec=="E"):
            import bolum3
            break
        elif(hsec=="h" or hsec=="H"):
            sys.exit
            break
        else:
            sys.exit
            break
    if(oyuncu2.can == 15 or oyuncu2.can == 14 or oyuncu2.can == 11):
        oyuncu2.can += 12
        oyuncu2.power -= 22
         
