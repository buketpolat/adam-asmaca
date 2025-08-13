README
Adam Asmaca (Türkçe, Unicode uyumlu)
Konsolda iki kişiyle (veya tek başına) oynanabilen, Türkçe karakterlerle sorunsuz çalışan bir Adam Asmaca oyunu. Renkli çıktı (isteğe bağlı), uyarı sesi ve Türkçe harf duyarlılığıyla keyifli bir terminal deneyimi sunar.

🧩 Özellikler
-En fazla 5 yanlış tahmin hakkı (6. denemede adam tamamlanır).
-Türkçe/dil uyumu: Karşılaştırmalarda casefold() kullanır, I/ı/İ/i gibi harfler için daha sağlam eşleştirme.
-Gizli kelime girişi (opsiyonel): getpass ile kelimeyi ekrana yazdırmadan girme.
-Harf olmayan karakterler (boşluk, tire vb.) baştan açık kalır.
-Tek harf girişi teşvik edilir; tekrar girilen harfler ceza almaz.
-Tam kelime tahmini yapabilirsiniz (yanlışsa sadece 1 hak düşer).

Adam çizimi aşamaları:

0: boş iskele
1: kafa
2: gövde
3: sol kol
4: sağ kol
5: iki bacak (adam tamam)

Renkli çıktı ve uyarı sesi desteği (colorama varsa renkli; yoksa renksiz devam eder).

📦 Depoyu Klonlama
bash
git clone https://github.com/<kullanici-adi>/<depo-adi>.git
cd <depo-adi>
Depo adınızı ve kullanıcı adınızı kendi GitHub bilginizle değiştirin.

📥 Bağımlılıkları Yükleme
Projede yalnızca renkli çıktı için opsiyonel colorama kullanılır. Yüklemezseniz oyun yine çalışır (renksiz).

Sanal ortam (önerilir):

bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

Kurulum:
bash
pip install --upgrade pip
pip install colorama

🖥 Gereksinimler
Python 3.9+ (3.10/3.11/3.12 ile uyumlu)

Terminal/komut satırı
(İsteğe bağlı) colorama paketi
Unicode destekli font ve kodlama (genelde varsayılan yeterlidir)

Gerekirse: PYTHONIOENCODING=utf-8

▶️ Kullanım
bash
# Çalıştırma (macOS / Linux)
python3 hangman_tr.py

# Çalıştırma (Windows)
python hangman_tr.py
Program açıldığında şu akış izlenir:

-“Kelimeyi gizli girmek ister misiniz? (E/h)” sorusuna E derseniz kelime gizli alınır (getpass), h derseniz normal giriş.
-Ekran temizlenir; iskelet, maske ve kalan haklar gösterilir.
-Sırayla tek harf veya tüm kelime tahminleri girilir.
-Doğru/yanlış harfler listelenir; tekrar girilen harfler ceza almaz.

🕹️ Oynanış
-Tek harf girişi: a, b, ç, ğ vb. (harf olmayan girişler reddedilir).
-Tüm kelime tahmini: Kelimeyi tamamı ile yazın (doğruysa anında kazanırsınız).
-Yanlış tahminlerde Kalan hak bir azalır ve adam çizimi ilerler.
-Tüm harfler açıldığında kazanırsınız.
-5 yanlışta adam tamamlanır ve oyun biter.

🧾 Örnek Çıktı
Renkli kısımlar konsolda yeşil/kırmızı/sarı görünebilir; burada renksiz örnek gösterilmiştir.

=== Adam Asmaca ===
Kelimeyi gizli girmek ister misiniz? (E/h): h
Kelime: İstanbul

(Harf olmayan karakterler baştan açıktır)
  _______
 |/      |
 |       
 |      
 |       
 |         
|__
Kelime: ________
Kalan hak: 5

Tahmin (tek harf veya tüm kelime): i
Doğru harf!

  _______
 |/      |
 |       
 |      
 |       
 |         
|__
Kelime: I_______
Doğru harfler: i
Yanlış harfler: -
Kalan hak: 5

Tahmin (tek harf veya tüm kelime): z
Yanlış harf!

  _______
 |/      |
 |      O
 |      |
 |        
 |         
|__
Kelime: I_______
Doğru harfler: i
Yanlış harfler: z
Kalan hak: 4

Tahmin (tek harf veya tüm kelime): İstanbul
Doğru Tahmin! 🎉
Kelime: İstanbul
