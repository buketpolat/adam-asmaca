# 🎯 Adam Asmaca (Türkçe, Unicode Uyumlu)

Bu proje, **terminal tabanlı** ve **Türkçe karakter desteğine sahip** klasik **Adam Asmaca** oyunudur.  
Kullanıcı dostu tasarım, renkli çıktılar ve gizli kelime girişi gibi ek özellikler içerir.

---

## 🚀 Özellikler
- En fazla **5 yanlış tahmin hakkı**
- **Doğru/yanlış harfleri** ve kalan hakları takip etme
- Kelimeyi kullanıcıdan alma (gizli veya açık giriş)
- Harf olmayan karakterlerin (boşluk, tire vb.) baştan açık olması
- **Türkçe karakter desteği** ve büyük/küçük harf uyumu (`casefold`)
- Tek harf veya tüm kelime tahmini imkanı
- Yanlışlarda **ASCII adam çizimi**
- **Renkli çıktı** (Colorama kütüphanesi ile)
- Tekrar girilen harflerde ceza uygulanmaz
- Yanlış girişlerde **uyarı sesi** (`\a`)

---

## 📷 Örnek Ekran Görüntüsü
```
=== Adam Asmaca ===
(Harf olmayan karakterler baştan açıktır)
  _______ 
 |/      |
 |        
 |        
 |        
 |         
_|___      

Kelime: _ _ _ _ _
Kalan hak: 5
```

---

## 📦 Kurulum

### 1️⃣ Depoyu Klonlayın
```bash
git clone https://github.com/kullaniciadi/adam-asmaca-tr.git
cd adam-asmaca-tr
```

### 2️⃣ Gerekli Bağımlılıkları Yükleyin
```bash
pip install colorama
```

---

## ▶️ Çalıştırma
```bash
python adam_asmaca_tr.py
```

---

## 🔧 Oyun Kuralları
1. Oyun başında kelimeyi giren oyuncu isterse **gizli giriş** yapabilir.
2. Harf olmayan karakterler otomatik olarak açık olur.
3. Tek harf veya tüm kelime tahmini yapılabilir.
4. Yanlış tahminlerde **adam tamamlanmaya başlar** (5 yanlışta oyun biter).
5. Tekrar girilen harfler ceza puanı düşürmez.

---

## 📚 Kullanılan Teknolojiler
- **Python 3**
- **Colorama** (renkli terminal çıktısı)
- Standart Python kütüphaneleri: `sys`, `getpass`

---

## 📄 Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır.  
Dilediğiniz gibi kullanabilir, geliştirebilir ve paylaşabilirsiniz.

---

## ✨ Katkıda Bulunma
1. Bu projeyi forklayın.
2. Yeni bir dal (branch) oluşturun:  
   ```bash
   git checkout -b ozellik-adi
   ```
3. Değişikliklerinizi kaydedin ve açıklayıcı commit mesajı yazın.
4. Dalınızı GitHub'a gönderin:  
   ```bash
   git push origin ozellik-adi
   ```
5. Bir **Pull Request** açın.

---

👤 **Geliştirici:** Nehir Buket Polat  
📧 İletişim: [buketpolat08@outlook.com]
