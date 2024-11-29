import sys
import threading
import time
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice, add_item_to_inventory, show_player_choices
from src.story.chapter3 import chapter_3, chapter_3_event_1, chapter_3_event_2, chapter_3_event_3, chapter_3_event_4, chapter_3_event_5, chapter_3_event_6, chapter_3_event_7, chapter_3_event_8, chapter_3_event_9, chapter_3_event_10
from src.gameLogic.chapter4_logic import chapter4

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter3(nama_karakter):
    """Mengelola alur chapter 2."""
    for line in chapter_3(nama_karakter):
        typewriter(line)
    
    # Mengupdate status game
    game_state["location"] = "Pulau"  # Update lokasi
    game_state["progres"] = "Misteri Pulau Amba"  # Update progres
    
    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter3_event1(game_state['nama_karakter'])

def chapter3_event1(nama_karakter):
    global game_state

    for line in chapter_3_event_1(nama_karakter):
        typewriter(line)
    game_state["location"] = " Di tepi hutan"
    game_state["progres"] = "Jejak yang Tertinggal"
    save_checkpoint(game_state)
    
    # pilihan aksi pemain
    process_player_choice(
        chapter3_event2,
        game_state,
        "Pilih aksi:",
        [
            {"name": "Mengikuti jejak itu dengan hati-hati, berharap menemukan petunjuk.", "value": "benar"},
            {"name": "Abaikan dan berjalan sembarangan, tetapi tersesat di hutan dan dikelilingi binatang buas.", "value": "salah"}
        ],
        lambda: chapter3_event1(game_state['nama_karakter']),
        display_state
    )

def chapter3_event2(nama_karakter):
    global game_state

    for line in chapter_3_event_2(nama_karakter):
        typewriter(line)
    game_state["location"] = "Di tengah hutan"
    game_state["progres"] = "Pohon Tua Berukir Simbol Aneh"
    save_checkpoint(game_state)

    # pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Teliti simbol itu lebih dekat dan buat sketsa sebagai petunjuk.", "value": "teliti"},
        {"name": "Abaikan simbol dan teruskan perjalanan.", "value": "abaikan"}
    ]
   
    event_mapping = {
        "teliti": chapter3_event3,
        "abaikan": chapter3_event3,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter3_event3(nama_karakter):
    global game_state

    for line in chapter_3_event_3(nama_karakter):
        typewriter(line)
    print("\n")
    add_item_to_inventory('Pisau')
    game_state["progres"] = "Rintangan Jaring Laba-Laba"
    save_checkpoint(game_state)

    # pilihan aksi pemain
    process_player_choice(
        chapter3_event4,
        game_state,
        "Pilih Aksi:",
        [
            {"name": "{nama_karakter} menggunakan pisau untuk memotong jaring dan membebaskan mereka.", "value": "benar"},
            {"name": "Berusaha melepaskan dengan tangan kosong, tetapi jaring semakin merekat dan laba-laba itu menyerang.", "value": "salah"}
        ],
        lambda: chapter3_event3(game_state['nama_karakter']),
        display_state
    )

def chapter3_event4(nama_karakter):
    global game_state

    for line in chapter_3_event_4(nama_karakter):
        typewriter(line)
    game_state["location"] = "Lorong batu di lereng bukit"
    game_state["progres"] = "Lorong Batu di Perbukitan"
    save_checkpoint(game_state)

        # pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
            {"name": "Berjalan melalui lorong dengan tenang, menjaga kewaspadaan.", "value": "lorong"},
            {"name": "Mencari jalan memutar, meskipun lorong ini terlihat lebih langsung.", "value": "memutar"}
        ]
    
    event_mapping = {
        "lorong": chapter3_event5,
        "memutar": chapter3_event5,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter3_event5(nama_karakter):
    global game_state

    for line in chapter_3_event_5(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Peti Kuno Berpaku Karat"
    save_checkpoint(game_state)

        # pilihan aksi pemain
    process_player_choice(
            chapter3_event6,
            game_state,
            "Pilih aksi:",
            [
                {"name": "Membuka peti dengan hati-hati menggunakan pisau untuk memeriksa jebakan.", "value": "benar"},
                {"name": "Membuka peti dengan tangan kosong, dan terkena racun dari paku karat.", "value": "salah"}
            ],
            lambda: chapter3_event5(game_state['nama_karakter']),
            display_state
        )

def chapter3_event6(nama_karakter):
    global game_state

    for line in chapter_3_event_6(nama_karakter):
        typewriter(line)
    print("\n")
    add_item_to_inventory(['Tali', 'Batu'])
    game_state["progres"] = "Sumur Tua yang Terbengkalai"
    save_checkpoint(game_state)

        # pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
            {"name": "Turun menggunakan tali untuk memeriksa bagian dalam sumur", "value": "tali"},
            {"name": "Mengambil batu dan melemparkannya ke dalam sumur untuk memeriksa kedalamannya.", "value": "batu"}
        ]
   
    event_mapping = {
        "tali": chapter3_event7,
        "batu": chapter3_event7,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter3_event7(nama_karakter):
    global game_state

    for line in chapter_3_event_7(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Jejak Cahaya di Kegelaapan"
    save_checkpoint(game_state)

        # pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
            {"name": "Mengikuti cahaya itu untuk melihat ke mana ia menuju.", "value": "mengikuti"},
            {"name": "Mengabaikan cahaya dan tetap pada jalur yang mereka pilih.", "value": "mengabaikan"}
        ]
    
    event_mapping = {
        "mengikutii": chapter3_event8,
        "mengabaikaan": chapter3_event8,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter3_event8(nama_karakter):
    global game_state

    for line in chapter_3_event_8(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Pertemuan dengan Patung Batu Berwwajah Marah"
    save_checkpoint(game_state)

    # pilihan aksi pemain
    process_player_choice(
        chapter3_event9,
        game_state,
        "Pilih aksi:",
        [
            {"name": "Menghormati patung dengan menundukkan kepala sebelum melanjutkan.", "value": "benar"},
            {"name": "Melewati patung dengan angkuh, membuat jebakan batu runtuh", "value": "salah"}
        ],
        lambda: chapter3_event8(game_state['nama_karakter']),
        display_state
    )

def chapter3_event9(nama_karakter):
    global game_state

    for line in chapter_3_event_9(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Mencari Jalan di Reruntuhan Kuil Tua"
    save_checkpoint(game_state)

    # pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
    {"name": "Memeriksa jalur dengan hati-hati dan mencoba menghindari jebakan.", "value": "memeriksa"},
    {"name": "Masuk tanpa melihat tanda-tanda di lantai dan mengambil risiko tersandung jebakan.", "value": "tanpa melhat"}
    ]
    
    event_mapping = {
        "memeriksa": chapter3_event10,
        "tanpa melihat": chapter3_event10,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter3_event10(nama_karakter):
    global game_state

    for line in chapter_3_event_10(nama_karakter):
        typewriter(line)
    game_state["location"] = "Di dalam kuil"
    game_state["progres"] = "Kode Tersembunyi pada Dinding"
    save_checkpoint(game_state)

    # pilihan aksi pemain
    process_player_choice(
        end_chapter,
        game_state,
        "Pilih aksi:",
        [
            {"name": "Menyusun simbol sesuai ingatan dari tanda di pohon, membuka pintu rahasia di dinding.", "value": "benar"},
            {"name": "Menyusun simbol sembarangan, memicu jebakan dan dinding kuil runtuh.", "value": "salah"}
        ],
        lambda: chapter3_event10(game_state['nama_karakter']),
        display_state
    )

def end_chapter(nama_karakter):
    """Akhiri Chapter 3 dan lanjutkan ke Chapter 4"""
    typewriter("Chapter 3 selesai. Permainan berlanjut ke chapter berikutnya...")
    time.sleep(2)
    clear_console()
    chapter4(game_state['nama_karakter'])