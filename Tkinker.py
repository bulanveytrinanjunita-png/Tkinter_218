import tkinter as tk

def cek_prediksi():
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

root = tk.Tk()
root.title("Hitung Prodi")
root.geometry("350x580")

tk.Label(root, text="Hitung Prodi", font=("Arial", 14, "bold")).pack(pady=10)

daftar_matkul = [
    "Dasar Jaringan", "Dasar Pemrograman", "Probabilita dan Statistika", "Basis Data", 
    "Jaringan Komputer", "Switching", "Algoritma", "Implementasi Basis Data", 
    "Bahasa Inggris", "Pancasila"
]

for matkul in daftar_matkul:
    tk.Label(root, text=f"Nilai {matkul}:").pack()
    tk.Entry(root).pack(pady=2)

btn = tk.Button(root, text="Hasil Prediksi", command=cek_prediksi)
btn.pack(pady=15)

label_hasil = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="green")
label_hasil.pack()

root.mainloop()