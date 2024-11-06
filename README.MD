# Story of Amba

*Story of Amba* adalah sebuah game petualangan berbasis teks yang mengajak pemain ke dunia fantasi misterius melalui antarmuka Command Line (CLI). Dalam game ini, pemain akan menjalani berbagai tantangan dan teka-teki sebagai karakter utama yang dapat diberi nama sesuai keinginan pemain. Pilihan yang diambil akan membentuk jalur cerita dan memberikan pengalaman bermain yang bervariasi melalui beberapa pilihan akhir cerita. Meskipun pilihan pemain akan memengaruhi ending, jalur utama cerita tetap memberikan alur yang konsisten dan mendalam.

## 🎮 Fitur Utama

- **Input Nama Karakter**: Pemain dapat memasukkan nama karakter di awal permainan, yang akan digunakan dalam narasi, memberikan pengalaman lebih personal.
- **Sistem Checkpoint**: Menyimpan progres permainan di titik-titik tertentu agar dapat dilanjutkan di sesi berikutnya. Checkpoint disimpan dalam format JSON untuk mempermudah manajemen data penyimpanan.
- **Inventarisasi Sederhana**: Pemain dapat mengumpulkan atau menyimpan item yang dapat membantu dalam perkembangan cerita dan memengaruhi interaksi dengan lingkungan atau karakter lain.
- **Efek Audio dan Suara Latar**: Suara latar dan efek suara seperti hutan atau angin yang meningkatkan suasana cerita dan memberi pengalaman bermain yang lebih imersif.
- **Efek Typewriter untuk Narasi**: Narasi dengan efek typewriter membuat teks muncul perlahan seolah sedang diketik, memberikan kesan dramatis yang menambah kedalaman dan fokus pemain pada cerita.

## 🛠 Persyaratan Sistem

- **Python** 3.7 atau lebih baru
- **Library yang diperlukan**:
  - `pygame`: untuk memutar suara latar dan efek suara
  - `InquirerPy`: untuk antarmuka interaktif di CLI
  - Semua dependensi lainnya sudah terdaftar di dalam `requirements.txt`

## 🚀 Instalasi

1. **Kloning Repository**
   ```bash
   git clone https://github.com/username/story-of-amba.git

   ```bash
   cd story-of-amba

2. **Instalasi Library yang Dibutuhkan**
   ```bash
   pip install -r requirements.txt

## 🎲 Cara Menjalankan Game

1. Buka terminal atau command prompt, pastikan Anda berada di direktori *story-of-amba*

2. Jalankan game dengan perintah:
   ```bash
   python main.py

3. Ikuti petunjuk di layar untuk memasukkan nama karakter dan memulai petualangan Anda di Story of Amba.

## 💾 Sistem Checkpoint

Game secara otomatis menyimpan progres di checkpoint pada beberapa titik penting, memungkinkan pemain untuk melanjutkan dari titik terakhir yang dicapai di sesi permainan sebelumnya. Data checkpoint ini disimpan dalam format JSON, memudahkan untuk pengelolaan dan kompatibilitas.

## 📝 Catatan

- Jika terdapat kesalahan saat menjalankan *pygame*, pastikan semua file suara atau efek audio berada di dalam folder *sounds/*.
