import time
import random



class Çar():

    def __init__(self, İsim="Bilinmiyor", HP=100, MP=100, Irk="Bilinmiyor", Tür="Bilinmiyor",
                 Seviye=1, Güç=1, Temel_savunma=1, Azami_HP=1, Azami_MP=1, Birincil_silah="Boş",
                 İkincil_silah="Boş", Kask="Boş", Göğüs_zırhı="Boş", Eldiven="Boş",
                 Bacaklık="Boş", Çizme="Boş", Para=0, Kolye="Boş", Yüzük_1="Boş", Yüzük_2="Boş",
                 Skill_1="Bilinmiyor", Skill_2="Bilinmiyor", Skill_3="Bilinmiyor", Skill_4="Bilinmiyor"):

        # Irksal Özellikler
        self.İsim = İsim
        self.HP = HP
        self.MP = MP
        self.Irk = Irk
        self.Tür = Tür
        self.Seviye = Seviye

        # Arttırılabilir Özellikler
        self.Güç = Güç
        self.Temel_savunma = Temel_savunma
        self.Azami_HP = Azami_HP
        self.Azami_MP = Azami_MP

        # Silahlar
        self.Birincil_silah = Birincil_silah
        self.İkincil_silah = İkincil_silah

        # Zırhlar
        self.Kask = Kask
        self.Göğüs_zırhı = Göğüs_zırhı
        self.Eldiven = Eldiven
        self.Bacaklık = Bacaklık
        self.Çizme = Çizme

        # Takılar
        self.Yüzük_1 = Yüzük_1
        self.Yüzük_2 = Yüzük_2
        self.Kolye = Kolye

        # --------------
        self.Para = Para

        # Skiller
        self.Skill_1 = Skill_1
        self.Skill_2 = Skill_2
        self.Skill_3 = Skill_3
        self.Skill_4 = Skill_4


    def Statları_göster(self):
        while True:
            Stat = input("Karakterinizin genel statları için 1, Detaylı Değerler için 2, Çıkmak için 3 giriniz. Cevabınız = ")

            if Stat == "1":
                print("""
                **************************
                
                İsim : {}
        
                Irk ve Tür : {} - {}
        
                Seviye : {}
        
                HP = {}
        
                MP = {}
        
                **************************
        
                Güç : {}
        
                Temel Savunma : {}
        
                Azami HP : {}
        
                Azami MP : {}
        
                **************************
        
                Birincil Silah : {}
        
                İkincil Silah : {}
        
                **************************
        
                Kask : {}
        
                Göğüs Zırhı : {}
        
                Eldiven : {}
        
                Bacaklık : {}
        
                Çizme : {}
        
                **************************
        
                Birinci Yüzük : {}
        
                İkinci Yüzük : {}
        
                Kolye : {}
                
        
        
                """.format(self.İsim,self.Irk,self.Tür,self.Seviye,self.HP,self.MP,
                           self.Güç,self.Temel_savunma,self.Azami_HP,self.Azami_MP,
                           self.Birincil_silah,self.İkincil_silah,self.Kask,self.Göğüs_zırhı,
                           self.Eldiven,self.Bacaklık,self.Çizme,self.Yüzük_1,self.Yüzük_2,self.Kolye))

            elif Stat == "2":
                print("""
                Kritik değer {}
                delme değeri {}
                sersemletme değeri {}
                """)

            elif Stat == "3":
                print("Stat ekranından çıkılıyor...")
                break
            else:
                print("Lütfen geçerli bir seçenek seçiniz.")
                continue

    def Pazar(self):
        while True:
            print("""
            **************************
            Pazara Hoşgeldiniz!
            **************************""")
            time.sleep(0.8)
            print("""
            Silah pazarına gitmek için 1

            Zırh pazarına gitmek için 2

            Takı pazarına gitmek için 3

            Demirciye gitmek için 4

            Simyacıya gitmek için 5

            Pazardan çıkmak için q
                """)
            seçim = input("Nereye gitmek istiyorsunuz? Seçiminiz = ")

            if seçim == "1":
                print("""
                **************************
                Silah Pazarına Hoşgeldiniz!
                **************************""")
                time.sleep(0.8)
                print("""
                isim : {}

                Irk : {}

                Tür : {}

                Para : {}

                """.format(self.İsim, self.Irk, self.Tür, self.Para))
                if self.Tür == "Savaşçı":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                            Silahlar
                        **************************

                        Silahları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Silah 1 : Parası

                        Silah 2 : Parası

                        Silah 3 : Parası

                        Silah 4 : Parası

                        Silah 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi silahı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")
                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Silah pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Büyücü":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                            Silahlar
                        **************************

                        Silahları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Silah 1 : Parası

                        Silah 2 : Parası

                        Silah 3 : Parası

                        Silah 4 : Parası

                        Silah 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi silahı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")
                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Silah pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Berserker":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                            Silahlar
                        **************************

                        Silahları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Silah 1 : Parası

                        Silah 2 : Parası

                        Silah 3 : Parası

                        Silah 4 : Parası

                        Silah 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi silahı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")
                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Silah pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Kara Büyücü":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                            Silahlar
                        **************************

                        Silahları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Silah 1 : Parası

                        Silah 2 : Parası

                        Silah 3 : Parası

                        Silah 4 : Parası

                        Silah 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi silahı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")
                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Silah pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

            elif seçim == "2":
                print("""
                **************************
                Zırh Pazarına Hoşgeldiniz!
                **************************""")
                time.sleep(0.8)
                print("""
                isim : {}

                Irk : {}

                Tür : {}

                Para : {}

                """.format(self.İsim, self.Irk, self.Tür, self.Para))
                if self.Tür == "Savaşçı":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Zırhlar
                        **************************

                        Zırhları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Zırh 1 : Parası

                        Zırh 2 : Parası

                        Zırh 3 : Parası

                        Zırh 4 : Parası

                        Zırh 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Zırhı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Zırh pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Büyücü":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Zırhlar
                        **************************

                        Zırhları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Zırh 1 : Parası

                        Zırh 2 : Parası

                        Zırh 3 : Parası

                        Zırh 4 : Parası

                        Zırh 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Zırhı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Zırh pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Berserker":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Zırhlar
                        **************************

                        Zırhları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Zırh 1 : Parası

                        Zırh 2 : Parası

                        Zırh 3 : Parası

                        Zırh 4 : Parası

                        Zırh 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Zırhı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Zırh pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Kara Büyücü":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Zırhlar
                        **************************

                        Zırhları almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Zırh 1 : Parası

                        Zırh 2 : Parası

                        Zırh 3 : Parası

                        Zırh 4 : Parası

                        Zırh 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Zırhı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Zırh 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Zırh pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

            elif seçim == "3":
                print("""
                **************************
                Takı Pazarına Hoşgeldiniz!
                **************************""")
                time.sleep(0.8)
                print("""
                isim : {}

                Irk : {}

                Tür : {}

                Para : {}

                """.format(self.İsim, self.Irk, self.Tür, self.Para))

                if self.Tür == "Savaşçı":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Takılar
                        **************************

                        Takı almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Yüzük 1 : Parası

                        Yüzük 2 : Parası

                        Kolye 3 : Parası

                        Takı 4 : Parası

                        Takı 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Takıyı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Takı pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Büyücü":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Takılar
                        **************************

                        Takı almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Yüzük 1 : Parası

                        Yüzük 2 : Parası

                        Kolye 3 : Parası

                        Takı 4 : Parası

                        Takı 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Takıyı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Takı pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Berserker":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Takılar
                        **************************

                        Takı almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Yüzük 1 : Parası

                        Yüzük 2 : Parası

                        Kolye 3 : Parası

                        Takı 4 : Parası

                        Takı 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Takıyı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Takı pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

                elif self.Tür == "Kara Büyücü":
                    while True:
                        time.sleep(0.8)
                        print("""
                        **************************
                                Takılar
                        **************************

                        Takı almak için lütfen numarasını giriniz.
                        Çıkmak için q giriniz.
                        """)
                        time.sleep(0.8)
                        print("""

                        Yüzük 1 : Parası

                        Yüzük 2 : Parası

                        Kolye 3 : Parası

                        Takı 4 : Parası

                        Takı 5 : Parası

                        """)
                        time.sleep(0.8)
                        Silah = input("Hangi Takıyı almak istiyorsunuz ? Cevabınız = ")

                        if Silah == "1":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "2":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 2 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "3":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 3 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "4":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 4 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "5":
                            time.sleep(0.8)
                            Sword_1.show()
                            while True:
                                Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                if Satın_alma == "1":
                                    print("Takı 5 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                    break
                                elif Satın_alma == "2":
                                    print("Geri gidiliyor.")
                                    break
                                else:
                                    print("Lütfen geçerli bir seçenek giriniz.")

                        elif Silah == "q":
                            time.sleep(0.8)
                            print("Takı pazarından çıkılıyor...")
                            break

                        else:
                            time.sleep(0.8)
                            print("Lütfen geçerli bir seçenek giriniz.")

            elif seçim == "4":
                print("""
                **************************
                Demirci Pazarına Hoşgeldiniz!
                **************************""")
                time.sleep(0.8)
                print("""
                isim : {}

                Irk : {}

                Tür : {}

                Para : {}

                """.format(self.İsim, self.Irk, self.Tür, self.Para))

                while True:
                    time.sleep(0.8)
                    print("""
                    **************************
                            Demirci
                    **************************

                    Eşyalarınızı güçlendirmek için envanterinizden istediğiniz
                    eşyayı seçin ve şanısınızı deneyin.

                    Şuan Çalışmıyor Zorlama amk.

                    Çıkmak için q giriniz.
                    """)
                    time.sleep(0.8)
                    # Karakter_New.Envanter_sistemi()
                    break

            elif seçim == "5":
                print("""
                **************************
                Simyacı Pazarına Hoşgeldiniz!
                **************************""")
                time.sleep(0.8)
                print("""
                isim : {}

                Irk : {}

                Tür : {}

                Para : {}

                """.format(self.İsim, self.Irk, self.Tür, self.Para))

                time.sleep(0.8)
                print("""
                **************************
                        Efsuncu
                **************************

                Silahlarınıza Efsun basmak için 1, İksirlere bakmak için 2 giriniz.

                Çıkmak için q giriniz.
                """)

                while True:
                    time.sleep(0.8)
                    Seçenek = input("Silahlarınıza Efsun basmak için 1, İksirlere bakmak için 2 giriniz. Cevabınız = ")

                    if Seçenek == "1":
                        # Envanter_sistemi()
                        time.sleep(0.8)
                        print("envanter sistemi gelecek")

                    elif Seçenek == "2":
                        while True:
                            time.sleep(0.8)
                            print("""
    
                            1 - Güç İksiri : Parası
    
                            2 - Direnç İksiri : Parası
    
                            3 - HP İksiri : Parası
    
                            4 - MP İksiri : Parası
    
                            Pazardan çıkmak için q giriniz
                            """)
                            İksir = input("İksirlere bakmak için lütfen numarasını giriniz. Cevabınız = ")
                            if İksir == "1":
                                time.sleep(0.8)
                                Sword_1.show()
                                while True:
                                    Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                    if Satın_alma == "1":
                                        print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                        break
                                    elif Satın_alma == "2":
                                        print("Geri gidiliyor.")
                                        break
                                    else:
                                        time.sleep(0.8)
                                        print("Lütfen geçerli bir seçenek giriniz.")

                            elif İksir == "2":
                                time.sleep(0.8)
                                Sword_1.show()
                                while True:
                                    Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                    if Satın_alma == "1":
                                        print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                        break
                                    elif Satın_alma == "2":
                                        print("Geri gidiliyor.")
                                        break
                                    else:
                                        time.sleep(0.8)
                                        print("Lütfen geçerli bir seçenek giriniz.")

                            elif İksir == "3":
                                time.sleep(0.8)
                                Sword_1.show()
                                while True:
                                    Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                    if Satın_alma == "1":
                                        print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                        break
                                    elif Satın_alma == "2":
                                        print("Geri gidiliyor.")
                                        break
                                    else:
                                        time.sleep(0.8)
                                        print("Lütfen geçerli bir seçenek giriniz.")

                            elif İksir == "4":
                                time.sleep(0.8)
                                Sword_1.show()
                                while True:
                                    Satın_alma = input("Satın almak için 1, Geri gitmek için 2 giriniz. Cevabınız = ")
                                    if Satın_alma == "1":
                                        print("Silah 1 alındı. Getirdiği efektler şunlardır. {}-{}-{}-{}-")
                                        break
                                    elif Satın_alma == "2":
                                        print("Geri gidiliyor.")
                                        break
                                    else:
                                        time.sleep(0.8)
                                        print("Lütfen geçerli bir seçenek giriniz.")

                            elif İksir == "q":
                                time.sleep(0.8)
                                print("İksir pazarından çıkılıyor...")
                                break

                            else:
                                time.sleep(0.8)
                                print("Lütfen geçerli bir seçenek giriniz.")

                    elif Seçenek == "q":
                        time.sleep(0.8)
                        print("Pazardan çıkılıyor...")
                        break

                    else:
                        time.sleep(0.8)
                        print("Lütfen geçerli bir seçenek giriniz.")

            elif seçim == "q":
                time.sleep(0.8)
                print("Pazardan çıkılıyor...")
                break
            else:
                time.sleep(0.8)
                print("Lütfen geçerli bir seçenek giriniz.")

    def Drop(self):

        if self.Tür == "Savaşçı":

            Silahlar = [1,5,9,46,8]
            Zırhlar = [2,5,6,4,9]
            Takılar = [3,7,8,9,4,6,2]
            Potion = ["Hp İksiri","MP İksiri","Direnç İksiri","Güç İksiri"]

            drop_list = random.choice([Silahlar,Zırhlar,Takılar,Potion])

            drop_item = random.choice(drop_list)

            Envanter.append(drop_item)

            print("""Tebrikler! Bir eşya aldınız.
            Eşyanız : {}""".format(drop_item))

        elif self.Tür == "Büyücü":

            Silahlar = [1,5,9,46,8]
            Zırhlar = [2,5,6,4,9]
            Takılar = [3,7,8,9,4,6,2]
            Potion = ["Hp İksiri","MP İksiri","Direnç İksiri","Güç İksiri"]

            drop_list = random.choice([Silahlar,Zırhlar,Takılar,Potion])

            drop_item = random.choice(drop_list)

            Envanter.append(drop_item)

            print("""Tebrikler! Bir eşya aldınız.
            Eşyanız : {}""".format(drop_item))


        elif self.Tür == "Berserker":

            Silahlar = [1,5,9,46,8]
            Zırhlar = [2,5,6,4,9]
            Takılar = [3,7,8,9,4,6,2]
            Potion = ["Hp İksiri","MP İksiri","Direnç İksiri","Güç İksiri"]

            drop_list = random.choice([Silahlar,Zırhlar,Takılar,Potion])

            drop_item = random.choice(drop_list)

            Envanter.append(drop_item)

            print("""Tebrikler! Bir eşya aldınız.
            Eşyanız : {}""".format(drop_item))

        elif self.Tür == "Kara Büyücü":

            Silahlar = [1,5,9,46,8]
            Zırhlar = [2,5,6,4,9]
            Takılar = [3,7,8,9,4,6,2]
            Potion = ["Hp İksiri","MP İksiri","Direnç İksiri","Güç İksiri"]

            drop_list = random.choice([Silahlar,Zırhlar,Takılar,Potion])

            drop_item = random.choice(drop_list)

            Envanter.append(drop_item)

            print("""Tebrikler! Bir eşya aldınız.
            Eşyanız : {}""".format(drop_item))

    def Karakter_oluşturma(self):

        print("Öncelikle bir karakter oluşturmalısınız...")

        time.sleep(0.8)

        while True:
            Karakter = input("""Karakterinizin insan olması için 1, Canavar olması için lütfen 2 giriniz. Cevabınız = """)

            if Karakter == "1":
                while True:
                    karakter_Irk = input(
                        """Karakterinizin Savaşçı olması için 1, Büyücü olması için lütfen 2 giriniz. Cevabınız = """)

                    if karakter_Irk == "1":
                        self.Irk = "İnsan"
                        self.Tür = "Savaşçı"
                        print("Karakteriniz insan ırkından bir Savaşçı olmuştur. Şans yanınızda olsun.")
                        break

                    elif karakter_Irk == "2":
                        self.Irk = "İnsan"
                        self.Tür = "Büyücü"
                        print("Karakteriniz insan ırkından bir Büyücü olmuştur. Şans yanınızda olsun.")
                        break
                    else:
                        print("Lütfen geçerli bir seçenek seçiniz.")
                        continue
                break

            elif Karakter == "2":
                while True:
                    karakter_Irk = input(
                        """karakterinizin Berserker olması için 1, Kara Büyücü olması için 2 giriniz. Cevabınız = """)
                    if karakter_Irk == "1":
                        self.Irk = "Yaratık"
                        self.Tür = "Berserker"
                        print("Karakteriniz Yaratık türünden bir Berserker olmuştur. Şans yanınızda olsun.")
                        break

                    elif karakter_Irk == "2":
                        self.Irk = "Yaratık"
                        self.Tür = "Kara Büyücü"
                        print("Karakteriniz Yaratık türünden bir Kara Büyücü olmuştur. Şans Yanınızda olsun.")
                        break
                    else:
                        print("Lütfen geçerli bir seçenek seçiniz.")
                        continue
                break
            else:
                print("Lütfen geçerli bir seçenek seçiniz.")
                continue
        while True:
            İsim = input("Karakterinizin adı ne olsun? Cevabınız = ")
            time.sleep(0.8)
            Onay = input("İsminizi onaylamak için 1, Yeniden isim girmek için 2 giriniz. Seçiminiz = ")
            if Onay == "1":
                self.İsim = İsim
                time.sleep(0.8)
                print("İsminiz kaydedilmiştir...")
                break
            elif Onay == "2":
                print("Yeniden isminizi giriniz.")
                time.sleep(0.8)
                continue
            else:
                print("Lütfen geçerli bir seçenek seçiniz.")
                time.sleep(0.8)
                continue


print("""
*******************************************
Merhabalar, Metin3 dünyasına hoşgeldiniz...
*******************************************
""")
Karakter_New = Çar()
Karakter_New.Karakter_oluşturma()
Karakter_New.Statları_göster()
Karakter_New.Pazar()






