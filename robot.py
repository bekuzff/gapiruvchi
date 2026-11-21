import tkinter as tk
import pyttsx3

def gapir():
    matn = matn_qutisi.get("1.0", tk.END).strip()
    if matn:
        engine = pyttsx3.init()
        engine.setProperty('rate', tezlik_slayder.get())  # Gapirish tezligi
        engine.say(matn)
        engine.runAndWait()

# Asosiy oynani yaratish
oyna = tk.Tk()
oyna.title("Gapiruvchi Dastur")
oyna.geometry("400x320")
oyna.configure(bg="#1e1e2e")

tk.Label(oyna, text="Gapirish uchun matn yozing:", bg="#1e1e2e", fg="white", font=("Arial", 12)).pack(pady=10)

# Matn yozish joyi
matn_qutisi = tk.Text(oyna, height=6, width=40, font=("Arial", 11))
matn_qutisi.pack(pady=5)
matn_qutisi.insert(tk.END, "Salom! Men Python dasturiman.")

# Tezlikni sozlash
tk.Label(oyna, text="Gapirish tezligi (past bo'lsa robotga o'xshaydi):", bg="#1e1e2e", fg="#aaaaaa", font=("Arial", 9)).pack(pady=(10, 0))
tezlik_slayder = tk.Scale(oyna, from_=80, to=250, orient=tk.HORIZONTAL, bg="#1e1e2e", fg="white", highlightthickness=0)
tezlik_slayder.set(140)
tezlik_slayder.pack()

# Tugma
tugma = tk.Button(oyna, text="🔊 GAPIRISH", command=gapir, bg="#00e676", fg="black", font=("Arial", 12, "bold"), padx=20, pady=5)
tugma.pack(pady=15)

oyna.mainloop()
