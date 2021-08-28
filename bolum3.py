import time,sys,random,os

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')


print("""\033[96m\n Örümceği Yendikten sonra bıçağını zehire batırdın.Artık daha güçlü bir bıçağa sahipsin.İyileşmek için kapıdan çıktın ve orada bayıldın 
uyandığında bi adam seni iyileştiriyordu uyandığını anladığı an hemen kaçtı.Adamın yüzünde siyah bi sargı ve kolunda sarı bir şişe dövmesi vardı sadece bunu hatırlıyordun
adamın masasındaki iyileştiriciyi lazım olursa diye aldın ve 3.kapıya tekrar gittin.Yol gittikçe kararıyordu.Yol bitmişti etraf kapkaranlıktı ne yapacağını şaşırdın ayağın bi cisme takıldı 
aşağı doğru yuvarlandın birden ışıklar açıldı meşaleler yandı ve karşında kuzeninin cesedini buldun! orada kalakaldın ve ziyaretine baltalı bir iskelet geldi... Yaşamak için Savaş! \n""")


print("""
Baltalı İskelet;
Vuruş : 4
Can : 25
Enerji : 90
Ekipman : Balta

******************

Zordiac;
Vuruş : 3
Can : 10
Enerji : 70
Ekipman : Zehirli bıçak,İyileştirici(+2 can,-8 enerji) 

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
    def __init__(self,isim,can=10,power=70,puan=0):
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
            self.puan += 20
            dusman.can -= 3
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 2
            dusman.puan += 20
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSaldırı Başarısız")
    def iyilestirici(self):
        self.can += 2
        self.power -= 8
        print("İyileştirme Başarılı +2 can eklendi! 8 enerji kaybettin")
    def  savun(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            self.power -= 4
            dusman.power -= 8
            self.puan += 20
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSavunma Başarılı")

    
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 4
            dusman.puan += 20
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
oyuncu2 = oyuncu("Baltalı İskelet")




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
        print("\033[92m\nİskeleti Yendin Hikaye devam ediyor...")
        time.sleep(3)
        import bolum4
        break
    if(oyuncu2.puan==100 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        hsec = input("\033[91m\nOyunu Kaybettin,İskelete yenildin! Önceki bölüme Baştan başlamak ister misin? e/h ")
        print("Kaybedersen 1 önceki bölümden başlarsın.")
        if(hsec=="e" or hsec=="E"):
            import bolum2
            break
        elif(hsec=="h" or hsec=="H"):
            sys.exit
            break
        else:
            sys.exit
            break
    if(oyuncu2.can == 10 or oyuncu2.can == 7 or oyuncu2.can == 9):
        oyuncu2.can += 15
        oyuncu2.power += 20
         
