class Urun:
    def __init__(self, ad, fiyat, miktar):
        self.ad = ad
        self.fiyat = fiyat
        self.miktar = miktar

    def __str__(self):
        return f"{self.ad} - {self.miktar} x {self.fiyat:.2f} TL"


class Sepet:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self, urun):
        for mevcut_urun in self.urunler:
            if mevcut_urun.ad == urun.ad:
                mevcut_urun.miktar += urun.miktar
                return
        self.urunler.append(urun)

    def urun_cikar(self, urun_adi):
        self.urunler = [urun for urun in self.urunler if urun.ad != urun_adi]

    def sepeti_listele(self):
        if not self.urunler:
            print("Sepet boş.")
        else:
            for urun in self.urunler:
                print(urun)

    def toplam_tutar(self):
        return sum(urun.fiyat * urun.miktar for urun in self.urunler)


def urun_islemleri():
    # Hazır ürünler listesi
    hazir_urunler = [
        Urun("Elma", 5.0, 1),
        Urun("Ekmek", 3.0, 1),
        Urun("Süt", 10.0, 1),
        Urun("Yumurta", 15.0, 1)
    ]

    sepet = Sepet()
    devam = True
    while devam:
        print("\n1. Ürün Ekle")
        print("2. Sepeti Listele")
        print("3. Ürün Çıkar")
        print("4. Toplam Tutar")
        print("5. Çıkış")
        secim = input("Bir seçenek girin: ")

        if secim == "1":
            print("\n1. Hazır Ürünlerden Ekle")
            print("2. Yeni Ürün Ekle")
            alt_secim = input("Seçiminiz: ")

            if alt_secim == "1":
                print("\nHazır Ürünler:")
                for i, urun in enumerate(hazir_urunler, 1):
                    print(f"{i}. {urun.ad} - {urun.fiyat:.2f} TL")
                urun_secim = int(input("Eklenecek ürün numarasını seçin: ")) - 1
                if 0 <= urun_secim < len(hazir_urunler):
                    miktar = int(input("Kaç adet eklemek istiyorsunuz? "))
                    secilen_urun = hazir_urunler[urun_secim]
                    sepet.urun_ekle(Urun(secilen_urun.ad, secilen_urun.fiyat, miktar))
                    print(f"{secilen_urun.ad} sepete eklendi.")
                else:
                    print("Geçersiz seçim!")
            elif alt_secim == "2":
                ad = input("Ürün adı: ")
                fiyat = float(input("Ürün fiyatı: "))
                miktar = int(input("Ürün miktarı: "))
                urun = Urun(ad, fiyat, miktar)
                sepet.urun_ekle(urun)1
                print(f"{ad} sepete eklendi.")
            else:
                print("Geçersiz seçim!")
        elif secim == "2":
            print("\nSepetteki Ürünler:")
            sepet.sepeti_listele()
        elif secim == "3":
            urun_adi = input("Çıkarmak istediğiniz ürün adı: ")
            sepet.urun_cikar(urun_adi)
            print(f"{urun_adi} sepetten çıkarıldı.")
        elif secim == "4":
            print(f"Toplam Tutar: {sepet.toplam_tutar():.2f} TL")
        elif secim == "5":
            print("Çıkış yapılıyor...")
            devam = False
        else:
            print("Geçersiz seçim, tekrar deneyin.")

urun_islemleri()
