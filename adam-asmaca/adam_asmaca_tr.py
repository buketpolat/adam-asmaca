#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Adam Asmaca (Türkçe, Unicode uyumlu)
Özellikler:
- En fazla 5 yanlış tahmin hakkı.
- Doğru/yanlış harfleri ve kalan hakları takip eder.
- Kelimeyi kullanıcıdan alır; istenirse getpass ile gizli girilebilir.
- Harf olmayan karakterler (boşluk, tire vb.) baştan açık kalır.
- Türkçe/dil uyumu: karşılaştırmalarda casefold() kullanılır.
- Tek harf girişi teşvik edilir; tekrar girilen harfler ceza almaz.
- Tam kelime tahmini hakkı vardır (yanlışsa 1 hak düşer).
- Yanlışlarda adam çizimi: 0: boş, 1: kafa, 2: gövde, 3: sol kol, 4: sağ kol, 5: iki bacak (adam tamamlanır).
- Hatalı girişlerde uyarı sesi (\\a) ve renkli çıktı (colorama) desteği.
"""

from __future__ import annotations

import sys
import getpass

try:
    # Renkli çıktı için (yoksa renksiz devam eder)
    from colorama import init as colorama_init
    from colorama import Fore, Style
    colorama_init(autoreset=True)
    C_OK = Fore.GREEN + Style.BRIGHT
    C_ERR = Fore.RED + Style.BRIGHT
    C_WARN = Fore.YELLOW + Style.BRIGHT
    C_INFO = Fore.CYAN + Style.BRIGHT
    C_DIM = Style.DIM
    C_RESET = Style.RESET_ALL
except Exception:  # colorama yoksa
    class _Dummy:
        def __getattr__(self, name): return ""
    Fore = Style = _Dummy()
    C_OK = C_ERR = C_WARN = C_INFO = C_DIM = C_RESET = ""

def draw_hangman(wrongs: int) -> str:
    """
    wrongs: 0..5
    0: boş iskele, 1: kafa, 2: gövde, 3: sol kol, 4: sağ kol, 5: iki bacak
    (5. yanlışta adam tamamlanır)
    """
    head  = "O" if wrongs >= 1 else " "
    body  = "|" if wrongs >= 2 else " "
    larm  = "/" if wrongs >= 3 else " "
    rarm  = "\\" if wrongs >= 4 else " "
    legs  = "/\\" if wrongs >= 5 else "  "

    lines = [
        "  _______ ",
        " |/      |",
        f" |      {head}",
        f" |     {larm}{body}{rarm}",
        f" |      {legs}",
        " |         ",
        "_|___      ",
    ]
    return "\n".join(lines)

def mask_word(secret: str, correct_letters: set[str]) -> str:
    """Harf olmayanlar açık; harfler '_' ile gizli. Doğru tahmin geldikçe açılır."""
    out = []
    for ch in secret:
        if ch.isalpha():
            if ch.casefold() in correct_letters:
                out.append(ch)  # orijinal harfi göster
            else:
                out.append("_")
        else:
            out.append(ch)  # boşluk/tire vb. açık
    return "".join(out)

def all_letters_revealed(secret: str, correct_letters: set[str]) -> bool:
    for ch in secret:
        if ch.isalpha() and ch.casefold() not in correct_letters:
            return False
    return True

def ask_secret_word() -> str:
    while True:
        try:
            choice = input(f"{C_INFO}Kelimeyi gizli girmek ister misiniz? (E/h): {C_RESET}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nÇıkılıyor.")
            sys.exit(0)
        if choice in ("e", "evet", "y"):
            try:
                word = getpass.getpass("Gizli kelime: ")
            except (EOFError, KeyboardInterrupt):
                print("\nÇıkılıyor.")
                sys.exit(0)
        else:
            try:
                word = input("Kelime: ")
            except (EOFError, KeyboardInterrupt):
                print("\nÇıkılıyor.")
                sys.exit(0)

        word = word.rstrip("\n")
        if any(c.strip() for c in word):
            return word
        print(C_WARN + "\aBoş olamaz, tekrar deneyin." + C_RESET)

def prompt_guess() -> str:
    """Tek harf ya da tüm kelime tahmini alır."""
    try:
        raw = input("Tahmin (tek harf veya tüm kelime): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nÇıkılıyor.")
        sys.exit(0)
    return raw

def main():
    print(C_INFO + "=== Adam Asmaca ===" + C_RESET)
    secret = ask_secret_word()
    secret_cf = secret.casefold()

    correct_letters: set[str] = set()
    wrong_letters: set[str] = set()
    wrongs = 0
    MAX_WRONG = 5

    print("\n" * 50)  # Kelimeyi giren kişiden ikinci oyuncuyu korumak için ekranı "temizle"
    print(C_DIM + "(Harf olmayan karakterler baştan açıktır)" + C_RESET)
    print(draw_hangman(wrongs))
    print("Kelime:", mask_word(secret, correct_letters))
    print(f"Kalan hak: {MAX_WRONG - wrongs}\n")

    while True:
        guess = prompt_guess()

        # Boş giriş
        if not guess:
            print(C_WARN + "\aBoş giriş geçersiz. Tek harf veya tüm kelime yazın." + C_RESET)
            continue

        # Tek harf mi?
        if len(guess) == 1:
            if not guess.isalpha():
                print(C_WARN + "\aLütfen bir HARF girin (rakam/sembol değil)." + C_RESET)
                continue

            g = guess.casefold()

            # Tekrar girilen harf cezalandırılmaz
            if g in correct_letters or g in wrong_letters:
                print(C_WARN + "Bu harfi zaten denediniz; ceza yok. Başka bir şey deneyin." + C_RESET)
                continue

            if g in [ch.casefold() for ch in secret if ch.isalpha()]:
                correct_letters.add(g)
                print(C_OK + "Doğru harf!" + C_RESET)
            else:
                wrong_letters.add(g)
                wrongs += 1
                print(C_ERR + "Yanlış harf!" + C_RESET + "\a")

        else:
            # Tüm kelime tahmini
            full = guess
            if full.casefold() == secret_cf:
                print(C_OK + "Doğru Tahmin! 🎉" + C_RESET)
                print("Kelime:", secret)
                break
            else:
                wrongs += 1
                print(C_ERR + "Yanlış kelime tahmini!" + C_RESET + "\a")

        # Durum çıktısı
        print()
        print(draw_hangman(wrongs))
        print("Kelime:", mask_word(secret, correct_letters))
        print(f"Doğru harfler: {', '.join(sorted(correct_letters)) if correct_letters else '-'}")
        print(f"Yanlış harfler: {', '.join(sorted(wrong_letters)) if wrong_letters else '-'}")
        print(f"Kalan hak: {MAX_WRONG - wrongs}\n")

        # Kazanma kontrolü
        if all_letters_revealed(secret, correct_letters):
            print(C_OK + "Doğru Tahmin! 🎉 Tüm harfleri açtınız." + C_RESET)
            print("Kelime:", secret)
            break

        # Kaybetme kontrolü
        if wrongs >= MAX_WRONG:
            print(C_ERR + "Oyun Bitti! Adam tamamlandı." + C_RESET)
            print("Doğru kelime:", secret)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nÇıkılıyor.")
