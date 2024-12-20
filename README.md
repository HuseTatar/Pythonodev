# Alışveriş Sepeti Uygulaması

Bu proje, kullanıcıların ürün ekleyip çıkarabildiği ve sepetin toplam tutarını hesaplayabildiği basit bir alışveriş sepeti sistemidir. Uygulama, nesne tabanlı programlama ilkelerine göre tasarlanmıştır.

## Kullanılan Sınıflar

### **Urun**
- Ürün adı, fiyat ve miktar bilgilerini saklar.
- `__str__` metodu, ürün bilgilerini okunabilir formatta döndürür.

### **Sepet**
- Sepete ürün ekleme, çıkarma, sepeti listeleme ve toplam tutarı hesaplama işlevlerini içerir.
- Tüm ürünler `self.urunler` adlı bir liste içinde saklanır.

## Özellikler

- **Ürün Ekleme**: Kullanıcı, hazır ürünlerden birini seçebilir ya da kendi ürününü ekleyebilir. Eklenen miktar, fiyatla çarpılarak sepet toplamına yansır.
- **Sepetten Ürün Çıkarma**: Sepetten istenilen ürün kolayca çıkarılabilir.
- **Sepeti Listeleme**: Sepetteki tüm ürünler, adları, miktarları ve fiyatlarıyla görüntülenir.
- **Toplam Tutar Hesaplama**: Sepetteki ürünlerin toplam tutarı dinamik olarak hesaplanır.

## Örnek Kullanım

Kullanıcı, sepetine ürün ekleyebilir, çıkarabilir ve toplam tutarı kolayca görebilir:

```python
# Örnek Ürün ve Sepet
urun = Urun("Elma", 10.5, 3)
sepet = Sepet()
sepet.urun_ekle(urun)

# Sepeti Listele ve Toplam Tutarı Hesapla
print(sepet.listele())
print(f"Toplam Tutar: {sepet.toplam_hesapla()} TL")
# Kütüphane Yönetim Sistemi

Bu proje, kitapları ekleyip listeleyebileceğiniz, ödünç verebileceğiniz ve geri alabileceğiniz basit bir kütüphane yönetim sistemini modellemektedir.

## Kullanılan Sınıflar

### **Kitap**
- Kitap adı, yazar adı ve ödünç durumu gibi bilgileri saklar.
- `__str__` metodu kitabın adını ve yazarını kullanıcı dostu bir formatta gösterir.

### **Kutuphane**
- Kitap ekleme, ödünç verme ve geri alma işlemleri yapılır.
- Kütüphanedeki mevcut kitaplar ve ödünç alınan kitaplar listelenebilir.

## Özellikler

- **Kitap Ekleme**: Kütüphaneye kitap ekleyebilirsiniz.
- **Kitapları Listeleme**: Mevcut kitapları görüntüleyebilirsiniz.
- **Ödünç Verme**: Kitapları ödünç verebilirsiniz.
- **Geri Alma**: Ödünç alınan kitapları geri alabilirsiniz.
