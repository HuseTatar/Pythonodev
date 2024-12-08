class Kitap:
    def __init__(self, ad, yazar):
        self.ad = ad
        self.yazar = yazar
        self.odunc_alindi_mi = False

    def __str__(self):
        odunc_durumu = "Ödünç Alındı" if self.odunc_alindi_mi else "Mevcut"
        return f"Kitap: {self.ad}, Yazar: {self.yazar}, Durum: {odunc_durumu}"

class Kutuphane:
    def __init__(self):
        self.kitaplar = []  # Kütüphanedeki kitaplar
        self.odunc_alinan_kitaplar = []  # Ödünç alınan kitaplar

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def kitaplari_listele(self):
        mevcut_kitaplar = [kitap for kitap in self.kitaplar if not kitap.odunc_alindi_mi]  # Ödünç alınmamış kitapları al
        if not mevcut_kitaplar:
            print("Elimizde şu an mevcut kitap yok.")
        else:
            print("Mevcut Kitaplar:")
            for kitap in mevcut_kitaplar:
                print(kitap)

    def kitap_odunc_al(self, kitap_ad):
        for kitap in self.kitaplar:
            if kitap.ad.lower() == kitap_ad.lower() and not kitap.odunc_alindi_mi:
                kitap.odunc_alindi_mi = True
                self.odunc_alinan_kitaplar.append(kitap)
                print(f"{kitap_ad} ödünç alındı.")
                return
        print(f"{kitap_ad} adıyla mevcut kitap bulunamadı ya da kitap zaten ödünç alınmış.")

    def kitap_iade_et(self, kitap_ad):
        for kitap in self.odunc_alinan_kitaplar:
            if kitap.ad.lower() == kitap_ad.lower():
                kitap.odunc_alindi_mi = False
                self.odunc_alinan_kitaplar.remove(kitap)
                print(f"{kitap_ad} iade edildi.")
                return
        print(f"{kitap_ad} adıyla ödünç alınan kitap bulunamadı.")

# Kullanıcıdan kitap bilgilerini alma ve işlemleri yapma
kutuphane = Kutuphane()

while True:
    print("\nKütüphane Yönetim Sistemi")
    print("1. Kitap Ekle")
    print("2. Kitapları Listele")
    print("3. Kitap Ödünç Al")
    print("4. Kitap İade Et")
    print("5. Çıkış")
    
    secim = input("Bir işlem seçin (1-5): ")

    if secim == "1":
        kitap_ad = input("Kitap Adı: ")
        yazar = input("Yazar: ")
        kitap = Kitap(kitap_ad, yazar)
        kutuphane.kitap_ekle(kitap)
        print(f"{kitap_ad} adlı kitap kütüphaneye eklendi.")
    
    elif secim == "2":
        kutuphane.kitaplari_listele()
    
    elif secim == "3":
        kutuphane.kitaplari_listele()  # Ödünç almak için önce mevcut kitapları listele
        kitap_ad = input("Ödünç almak istediğiniz kitabın adını girin: ")
        kutuphane.kitap_odunc_al(kitap_ad)
    
    elif secim == "4":
        kitap_ad = input("İade etmek istediğiniz kitabın adını girin: ")
        kutuphane.kitap_iade_et(kitap_ad)
    
    elif secim == "5":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen 1-5 arasında bir seçenek girin.")
