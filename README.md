#Adam Asmaca (Türkçe, Unicode Uyumlu)

Bu proje, geleneksel Adam Asmaca oyununun Unicode uyumlu, iki oyunculu bir terminal versiyonudur. İlk oyuncu kelimeyi belirler, ikinci oyuncu ise bu kelimeyi harf tahminleri yaparak bulmaya çalışır.

##Özellikler
* **Gizli Kelime Girişi:** Kelimeyi giren kişinin, kelimeyi ikinci oyuncuya göstermeden girmesi için getpass modülü kullanılır.
* **Kapsamlı Oyun Takibi:** Oyuncu, 5 yanlış tahmin hakkına sahiptir. Doğru ve yanlış harfler ayrı ayrı listelenir, kalan hak bilgisi her adımda güncellenir.
* **Unicode Uyumluluğu:** Türkçe karakterler dahil olmak üzere tüm harflerle uyumludur. Karşılaştırmalar casefold() yöntemiyle yapıldığı için büyük/küçük harf duyarlılığı yoktur.
* **Esnek Tahmin Seçenekleri:** Oyuncu, tek bir harf tahmin edebileceği gibi, dilediği zaman tüm kelimeyi de tahmin edebilir. Yanlış kelime tahmini, bir hak kaybına neden olur.
* **Gelişmiş Kullanıcı Deneyimi:** Hatalı girişler için uyarı sesleri (\a) ve mesajları bulunur.colorama kütüphanesi yüklüyse, çıktı renkli ve daha okunaklı hale gelir.Daha önce tahmin edilen harfler tekrar girildiğinde oyuncu ceza almaz.Kelimedeki boşluk veya tire gibi harf olmayan karakterler, ipucu olarak oyunun başında otomatik olarak gösterilir.
* **Grafiksel Geri Bildirim:** Yanlış tahminlerde, adamın parçaları sırayla çizilir (kafa, gövde, kollar ve bacaklar).

##Nasıl Kullanılır
1.  Bu Python dosyasını (adam_asmaca.py) bilgisayarınıza indirin.
2.  Renkli çıktıları görmek için colorama kütüphanesini yükleyin:

'''Bash


pip install colorama
Bir terminal veya komut istemi açın ve dosyanın bulunduğu dizine gidin.

Aşağıdaki komutu çalıştırın:

Bash

python3 adam_asmaca.py
Program, kelimeyi gizli mi yoksa açık mı girmek istediğinizi soracaktır. E veya e yazarak gizli girişi seçebilirsiniz.

Kelime girildikten sonra, oyun başlar ve ikinci oyuncu kelimeyi tahmin etmeye çalışır.

Oyuncu, tek bir harf veya tüm kelimeyi tahmin edebilir.

Oyun, kelime doğru bulunduğunda ya da tüm haklar bittiğinde sona erer.

Fonksiyonlar
draw_hangman(wrongs): Yanlış tahmin sayısına göre adamın asılma sahnesini çizer.

mask_word(secret, correct_letters): Kelimenin tahmin edilmemiş harflerini alt çizgi (_) ile maskeler.

all_letters_revealed(secret, correct_letters): Gizli kelimedeki tüm harflerin doğru tahmin edilip edilmediğini kontrol eder.

ask_secret_word(): Kullanıcıdan gizlenecek kelimeyi almayı yönetir.

prompt_guess(): Kullanıcıdan harf veya kelime tahminini alır.

main(): Oyunun ana döngüsünü yönetir, tüm fonksiyonları koordine eder ve oyunun sonucunu gösterir.
