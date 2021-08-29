import time,sys,random,os

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')
ultrahak=1

print("""\033[96m\n Saydam,sana ex-burst adında bir gücü öğretti.Bu güç kumar gibiydi,ortaya tüm enerjini koyuyordun sanki.Ona mağarayı sordum ve bana 'oraya gitmemek daha iyi'
dedi.Mağarayı görüyordum güneşin doğuşuna doğru 2 saatlik yolu vardı.Orada ailemin yattığına ve beni beklediğine emindim.O yüzden oraya gece gizlice gittim.Bu sefer 1.Kapıyı açtım.Elinde kılıçlı ve zırhlı bir varlık bana doğru koşmaya başladı.
Bu varlık sandığımdan daha güçlü görünüyordu.Onu yenmek zor olacaktı.Ona saldıracakken cebimdeki iksir şişesinin değiştirildiğini farkettim iyileştiricim yoktu... Gerçekleri Öğrenmek İçin Savaş! \n""")


print("""
Radiant;
Vuruş : 3
Can : 15
Enerji : 70
Ekipman : İyileştirici(+5 can -15 enerji)

******************

Zordiac;
Vuruş : 1
Can : 15
Enerji : 70
Ekipman :  Yumruk
Özel Yetenekler: Ex-Burst(Gerçekleşirse +7 hasar +10 puan -12 enerji,Gerçekleşmezse -25 enerji) 

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
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 3
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSaldırı Başarısız")
    def iyilestirici(self):
        self.can += 3
        self.power -= 8
        print("İyileştirme Başarılı +3 can eklendi! 8 enerji kaybettin")



    def exproof(self, dusman):

        if(ultrahak==0):
            print("\n Maalesef exburst hakkınız kalmadı.")

        else:
            #ultrahak -= 1
            sonuc = self.saldir_savun_sayi()
            if(sonuc==1): 
                self.power -= 12
                self.puan += 10
                dusman.can -= 7
                dusman.power -= 5
                self.bilgileri_goster()
                dusman.bilgileri_goster()
                print("\033[92mEx-Burst Başarılı")
            
            else:
                self.power -= 25
                self.bilgileri_goster()
                dusman.bilgileri_goster()
                print("\033[91mEx-Burst Başarısız")
        
    def savun(self, dusman):
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
            self.can -= 3
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
oyuncu2 = oyuncu("Radiant")




nokta_ekle()

while True:
    hamle = input("""
    1-Saldır
    2-Savun
    3-ExFlash
    4-ExBurst
    5-Çık

    Hamle Seçimi:
    """)
    if(hamle=="1"):
        oyuncu1.saldir(oyuncu2)

    elif(hamle=="2"):
        oyuncu1.savun(oyuncu2)
    elif(hamle=="5"):
        oyuncu1.exit()
    elif(hamle=="3"):
        print(":) :) :) :) :) :) :) :) :) :)  ")
    elif(hamle=="4"):
 
        oyuncu1.exproof(oyuncu2)
        
    else:
        hatali_eksik()


    if(oyuncu1.puan==100 or oyuncu2.can <= 0 or oyuncu2.power <= 0 ):
        print("\033[92m\nRadiant'ı Yendin Hikaye devam ediyor...")
        time.sleep(3)
        import bolum7
        break
    if(oyuncu2.puan==100 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        hsec = input("\033[91m\nOyunu Kaybettin,Raidant'a yenildin! Önceki bölüme Baştan başlamak ister misin? e/h ")
        print("Kaybedersen 1 önceki bölümden başlarsın.")
        if(hsec=="e" or hsec=="E"):
            import bolum5
            break
        elif(hsec=="h" or hsec=="H"):
            sys.exit
            break
        else:
            import bolum5
            break
    if(oyuncu2.can == 1 or oyuncu2.can == 7):
        oyuncu2.can += 5
        oyuncu2.power -= 15
         
