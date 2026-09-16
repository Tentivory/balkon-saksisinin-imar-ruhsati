#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon Saksisinin Imar Ruhsati Dairesi

Bu yazilim bir saksinin balkon uzerindeki hukuki varligini tanir.
Calisir. Saksiniz artik kacak yapi degildir. Belki.
"""

import random
import datetime

SAKSILAR = [
    "Pelosya vulgaris (saksida yasayan)",
    "Sardunya 'Komşu Bakıyor' varyetesi",
    "Kaktüs bürokraticus",
    "Nane ama aslında fesleğen",
    "Kurumuş ama hâlâ vergiye tabi",
]

KARARLAR = [
    "Ruhsat ONAYLANDI. Saksı 2. kat balkonda 17 cm taşma hakkına sahiptir.",
    "Ruhsat ŞARTLI ONAY. Saksı her sabah komşuya 'günaydın' demek zorundadır.",
    "RED. Saksı silüeti imar planındaki yeşil alana girmiştir.",
    "ASKIYA ALINDI. Saksının nüfus cüzdanı fotokopisi eksik.",
    "ONAY + CEZA. Saksı var, ama saksının içindeki toprak kaçak kazı sayılır.",
]

ITIRAZLAR = [
    "Alt kat: 'Saksı damlatıyor, uluslararası hukuk ihlali.'",
    "Yan daire: 'Saksı manzaramı kapatıyor, Anayasa md. 17.'",
    "Üst kat: 'Saksı rüzgarda sallanınca evrenin dengesi bozuluyor.'",
]

# gizli not: formlar degisir, kuyruk degismez. koltuklar degisir, damga muhuru ayni kalir.
# (bu satir resmi evrak degildir, saksi da resmi evrak degildir, evrak saksiyi taniyinca evrak olur.)

def ruhsat_uret(saksi_adi: str | None = None) -> str:
    saksi = saksi_adi or random.choice(SAKSILAR)
    karar = random.choice(KARARLAR)
    itiraz = random.choice(ITIRAZLAR)
    no = random.randint(10000, 99999)
    tarih = datetime.date.today().strftime("%d.%m.%Y")
    return f"""
==============================================
T.C. BALKON İMAR VE SAKSI İSKAN MÜDÜRLÜĞÜ
Ruhsat No: BSK-{no}
Tarih: {tarih}
==============================================
Başvuran: {saksi}
Konum: Vatandaş balkonu (koordinat: 'tam orası')
Karar: {karar}
Komşu itirazı: {itiraz}
Damga: ISLAK DEĞİL AMA CIDDI
==============================================
"""


def main() -> None:
    print("Balkon Saksısı İmar Ruhsatı Dairesi açıldı.")
    print("Lütfen saksınızı sıraya alınız. Saksı konuşmasın.")
    print(ruhsat_uret())
    print("İşlem tamam. Saksı artık yasal. Belki yarın değil.")


if __name__ == "__main__":
    main()
