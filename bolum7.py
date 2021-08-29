import time,sys,random,os

def hatali_eksik():
    print('!Eksik ya da Hatalı tuşlama!')
ultrahak=1

print("""\033[96m\n Radiantı yendikten sonra birden ateşler yanmaya başladı bir sürü radiant etrafıma toplandı ve birde baktım ki KARDEŞİM! 
kardeşim karşımdaydı ama sanki bana düşman gözü ile bakıyordu.Radiantın birisi Saldır! dedi ve kardeşim bana saldırmaya başladı.Ne olduğunu tam anlamadım ama anladığım bişey varsa kardeşimi aklını değiştirdiler.
Onunla savaşmak istemiyordum ama üzerine giydirdikleri zırh ve Eline verdikleri silah sayesinde ben onu yenmezsem o beni yenecekti.Onu kurtaramayacağımı bana attığı ilk kesikte anladım.Saldırmak zorundaydım... Yaşamak için Saldır' \n""")


print("""
Kardeşin;
Vuruş : 30
Can : 150
Enerji : 100
Ekipman : Ext(+100 Hasar,-30 enerji),Yenilenme(+150 sağlık -20 enerji)

******************

Zordiac;
Vuruş : 1
Can : 15
Enerji : 70
Ekipman :  Yumruk
Özel Yetenekler: Ex-Burst(Gerçekleşirse +40 hasar +10 puan -7 enerji,Gerçekleşmezse -15 enerji) 

İpucu: 3.kapı

Rakibin canı veya enerjisi 0 altına inerse veya puanınız 50 olursa kazanırsınız.Aynısı rakip için de geçerli
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
            self.puan += 1
            dusman.can -= 5
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSaldırı Başarılı")
            
        else:
            dusman.power -= 4
            self.power -= 8
            self.can -= 30
            dusman.puan += 5
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[91mSaldırı Başarısız")

    def iyilestirici(self):
        self.can += 300
        self.power -= 20




    def exproof(self, dusman):

        if(ultrahak==0):
            print("\n Maalesef exburst hakkınız kalmadı.")

        else:
            #ultrahak -= 1
            sonuc = self.saldir_savun_sayi()
            if(sonuc==1): 
                self.power -= 7
                self.puan += 10
                dusman.can -= 40
                dusman.power -= 5
                self.bilgileri_goster()
                dusman.bilgileri_goster()
                print("\033[92mEx-Burst Başarılı")
            
            else:
                self.power -= 15
                self.puan -= 5
                self.bilgileri_goster()
                dusman.bilgileri_goster()
                print("\033[91mEx-Burst Başarısız")
        
    def savun(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            self.power += 4
            dusman.power -= 8
            self.puan += 5
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
            print("\033[92mSavunma Başarılı")

    
        else:
            dusman.power += 4
            self.power -= 8
            self.can -= 30
            dusman.puan += 5
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
oyuncu2 = oyuncu("Kardeşin")




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
        oyuncu1.iyilestirici()
    elif(hamle=="4"):
 
        oyuncu1.exproof(oyuncu2)
        
    else:
        hatali_eksik()


    if(oyuncu1.puan==50 or oyuncu2.can <= 0 or oyuncu2.power <= 0 ):
        print("\033[92m\nSenin kaçacağını anlayıp iksiri değiştirmişlerdi.Bu iksir sana bolca can ve exburst hasar takviyesi yaptı.Sarı dövmeli adam hayatını kurtardı.Kardeşini Yendin.Hikaye devam ediyor...")
        time.sleep(3)
        import bolum7
        break
    if(oyuncu2.puan==50 or oyuncu1.can <= 0 or oyuncu1.power <= 0 ):
        print("Kaybettin. Bu bölümü baştan alıyorum.")
        time.sleep(5)
        import bolum7
    if(oyuncu2.can == 13 or oyuncu2.can == 15 or oyuncu2.can == 14 or oyuncu2.can == 1 or oyuncu2.can == 4 ):
        oyuncu2.can += 150
        oyuncu2.power -= 20
