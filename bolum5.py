import time,sys,random,os

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')


print("""\033[96m\n Menajer++yı yendikten sonra bayılacak kadar yorgundun.Baltan da kırılmıştı elinde silah da kalmamıştı.Kendini iyileştirip duruyordun.
Birden kolunda sarı şişe dövmesi olan ve kafasında siyah sargı olan adam yanına geldi.Sırtına hançer saplanmıştı,çok şaşgın bir şekilde bunu neden yaptığını sordun ve anında bayıldın.
Uyandığında bir ormanın içerisindeydin,ne olduğunu anlamadın.Biraz ilerleyince yeni bir ceset buldun,bu ceset yeğenine aitti.Yavaş yavaş aileni katlediyorlardı.
O an ki sinirle bağırmaya başladın.Çalıların arasından bi varlık fırladı ve sana şöyle dedi 'Beni yenersen özel güçler kazanacaksın! yenemezsen hayatını kaybedeceksin.' Yaşamak için Savaş! \n""")


print("""
Saydam;
Vuruş : 1
Can : 10
Enerji : 50
Ekipman : Yumruk,İyileştirici(+3 can -8 enerji)

******************

Zordiac;
Vuruş : 1
Can : 10
Enerji : 50
Ekipman : Yumruk,İyileştirici(+3 can,-8 enerji) 

Saydam,Senin kopyandır.Ona karşı iyi savaş

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
    def __init__(self,isim,can=10,power=50,puan=0):
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
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 1
            dusman.puan += 20
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
            self.power += 4
            dusman.power -= 8
            self.puan += 20
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSavunma Başarılı")

    
        else:
            dusman.power += 4
            self.power -= 8
            self.can -= 1
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
oyuncu2 = oyuncu("Saydam")




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
        print("\033[92m\nSaydamı Yendin Hikaye devam ediyor...")
        time.sleep(3)
        import bolum6
        break
    if(oyuncu2.puan==100 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        hsec = input("\033[91m\nOyunu Kaybettin,Saydam'a yenildin! Şuanki Bölüme Baştan başlamak ister misin? e/h ")

        if(hsec=="e" or hsec=="E"):
            import bolum5
            break
        elif(hsec=="h" or hsec=="H"):
            sys.exit
            break
        else:
            sys.exit
            break
    if(oyuncu2.can == 2):
        oyuncu2.can += 3
        oyuncu2.power -= 8
         
