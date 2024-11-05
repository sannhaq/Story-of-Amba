# Story of Amba

_Story of Amba_ adalah sebuah game petualangan berbasis teks (Command Line Interface) yang membawa pemain ke dalam dunia fantasi misterius. Pemain mengendalikan seorang karakter utama yang akan menghadapi berbagai tantangan dan teka-teki. Setiap pilihan yang diambil pemain akan memengaruhi akhir cerita, menciptakan beberapa variasi ending yang menambah replayability tanpa mengubah jalur utama cerita.

## Fitur Utama

- **Input Nama Karakter**: Pemain memasukkan nama karakter yang digunakan dalam narasi, memberikan pengalaman lebih personal.
- **Sistem Checkpoint**: Menyimpan progres permainan di titik-titik tertentu untuk dilanjutkan nanti. Data checkpoint disimpan dalam format JSON untuk manajemen yang mudah.
- **Inventarisasi Sederhana**: Pemain dapat mengumpulkan atau menyimpan item yang membantu dalam perkembangan cerita.
- **Efek Audio dan Suara Latar**: Menambah atmosfer petualangan dengan elemen suara, seperti suara hutan atau efek suara lainnya sesuai adegan.
- **Efek Typewriter untuk Narasi**: Efek typewriter membuat teks muncul seolah sedang diketik, memberikan kesan dramatis dan mendalam pada narasi.

## Persyaratan Sistem

- **Python** 3.7 atau lebih baru
- **Library yang dibutuhkan**:
  - `pygame`: untuk memutar suara latar dan efek suara
  - `InquirerPy`: untuk antarmuka interaktif di CLI
  - Semua dependensi lainnya ada di file `requirements.txt`

## Instalasi

1. **Kloning Repository**

   ```bash
   git clone https://github.com/username/story-of-amba.git
   cd story-of-amba

   ```

2. **Instalasi Library yang Dibutuhkan**
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Game

1. Pastikan Anda berada di dalam direktori story-of-amba
2. Jalankan file main.py dengan perintah:
   ```bash
   python main.py
   ```
