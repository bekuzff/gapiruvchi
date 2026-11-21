# 🗣️ Gapiruvchi Dastur (Python GUI Text-to-Speech)

Ushbu dastur kiritilgan istalgan matnni ovozga aylantirib (o‘qib) beruvchi sodda va qulay grafik interfeysli (GUI) Python ilovasidir. Ilova **internetsiz (offline)** ishlaydi va gapirish tezligini o‘zgartirish orqali ovozga robot effektini berish imkoniyatiga ega.

---

## ✨ Imkoniyatlari
* **Oflayn ishlash:** Internet ulanishi talab qilinmaydi (`pyttsx3` kutubxonasi yordamida).
* **Tezlikni boshqarish:** Slayder orqali nutq tezligini `80` dan `250` gacha sozlash (past tezlik robot ovozini beradi).
* **Qulay interfeys:** `Tkinter` asosida yaratilgan zamonaviy va tushunarli oyna.

---

## 🛠️ Talablar
* **Python 3.7** yoki undan yuqori versiya
* **PyCharm** (Community yoki Professional)
* `pyttsx3` kutubxonasi (`tkinter` Python bilan birga standart o‘rnatilgan bo‘ladi)

---

## 🚀 PyCharm'da o‘rnatish va ishga tushirish

### 1-qadam: Loyihani yaratish
1. **PyCharm** dasturini oching va **New Project** tugmasini bosing.
2. Loyiha nomini kiriting (masalan: `GapiruvchiDastur`) va **Create** tugmasini bosing.
3. Loyiha ichida `main.py` faylini oching (yoki yarating) va asosiy Python kodini unga joylashtiring.

### 2-qadam: Kerakli kutubxonani o‘rnatish
PyCharm pastki panelidagi **Terminal** bo‘limini oching va quyidagi buyruqni yozib `Enter` bosing:

```bash
pip install pyttsx3
