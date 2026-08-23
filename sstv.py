from PIL import Image
from pysstv.color import Robot36  # Ganti sesuai mode yang kamu pakai

def add_letterbox(image, target_width, target_height, bg_color=(0, 0, 0)):
    # 1. Dapatkan ukuran asli
    orig_width, orig_height = image.size
    
    # 2. Hitung skala agar gambar muat di dalam target
    #    Kita ambil skala terkecil agar tidak ada bagian yang terpotong
    scale = min(target_width / orig_width, target_height / orig_height)
    
    # 3. Hitung ukuran baru (mengecil secara proporsional)
    new_width = int(orig_width * scale)
    new_height = int(orig_height * scale)
    
    # 4. Resize gambar menggunakan kualitas terbaik (LANCZOS)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    # 5. Buat kanvas kosong berwarna hitam (atau warna pilihanmu)
    canvas = Image.new('RGB', (target_width, target_height), bg_color)
    
    # 6. Hitung posisi agar gambar berada tepat di TENGAH
    x_pos = (target_width - new_width) // 2
    y_pos = (target_height - new_height) // 2
    
    # 7. Tempelkan gambar yang sudah dikecilkan ke tengah kanvas
    canvas.paste(resized_image, (x_pos, y_pos))
    
    return canvas

# ---------- Jalankan Program ----------
# Baca gambar asli
file = input("masukan nama dan format gambar: ")
img = Image.open(f'./{file}').convert('RGB')

# Tentukan target sesuai mode SSTV yang kamu pakai
# Robot36 = 320x240
# PD120   = 640x480
# MartinM1 = 320x256
target_w, target_h = 320, 240  

# Proses gambar menjadi "mengecil dengan bingkai"
final_img = add_letterbox(img, target_w, target_h)

# Encode ke SSTV
sstv = Robot36(final_img, 48000, 16) 

jalur_hasil = f"hasil_sstv/{nama}.wav"

sstv.write_wav(jalur_hasil)

print(f"Selesai! Gambar to SSTV sudah berhasil dengan nama: {nama}.wav.")