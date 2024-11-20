import sys
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice
from src.story.chapter2 import chapter_2, chapter_2_event_1, chapter_2_event_2, chapter_2_event_3, chapter_2_event_4, chapter_2_event_5, chapter_2_event_6, chapter_2_event_7, chapter_2_event_8, chapter_2_event_9, chapter_2_event_10
from src.gameLogic.chapter3_logic import chapter3

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"nama_karakter:f {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter2(nama_karakter):
    """Mengelola alur chapter 2."""
    for line in chapter_2(nama_karakter):
        typewriter(line)
    
    # Mengupdate status game
    game_state["location"] = "Kapal"  # Update lokasi
    game_state["progres"] = "Perjalanan ke Pulau Amba"  # Update progres
    
    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter2_event1(game_state['nama_karakter'])

def chapter2_event1(nama_karakter):
    global game_state

    for line in chapter_2_event_1(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Badai di Tengah Malam"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter2_event2, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": f"{nama_karakter} menahan kemudi dan membantu Arfan melawan badai, meski ketakutan namun berhasil mengendalikan kapal hingga badai mereda.", "value": "benar"},
            {"name": f"{nama_karakter} panik dan bersembunyi di bawah dek, kehilangan kendali dan kapal terbalik oleh ombak besar.", "value": "salah"}
        ],
        lambda: chapter2_event1(game_state['nama_karakter']),
        display_state
    )   

def chapter2_event2(nama_karakter):
    global game_state

    for line in chapter_2_event_2(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Mengatasi kehausan"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter2_event3, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": f"Hemat air dan berbagi sisa air dengan bijak, {nama_karakter} dan Arfan bertahan sampai menemukan cara untuk mendapatkan air segar di pulau nanti.", "value": "benar"},
            {"name": "Minum banyak air tanpa menghemat — persediaan air cepat habis dan mereka kelelahan karena dehidrasi.", "value": "salah"}
        ],
        lambda: chapter2_event2(game_state['nama_karakter']),
        display_state
    )   

def chapter2_event3(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_2_event_3(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Hantu Kapal Bajak Laut"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Dekati kapal itu dan periksa lebih dekat (berpotensi memicu gangguan supernatural).", "value": "dekati kapal"},
        {"name": f"Abaikan kapal tersebut dan kembali tidur ({nama_karakter} menghindari bahaya misterius).", "value": "abaikan"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'dekati kapal':
        chapter2_event4(game_state['nama_karakter'])
    else:
        chapter2_event4(game_state['nama_karakter'])

def chapter2_event4(nama_karakter):
    global game_state

    for line in chapter_2_event_4(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Perbaikan Layar yang Rusak"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter2_event5, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": f"{nama_karakter} dengan hati-hati mengikuti instruksi Arfan dan memperbaiki layar, mengembalikan kapal ke kondisi baik.", "value": "benar"},
            {"name": f"{nama_karakter} tidak memperhatikan petunjuk Arfan dan merobek layar lebih parah, memperlambat perjalanan dan kehilangan arah. ", "value": "salah"}
        ],
        lambda: chapter2_event4(game_state['nama_karakter']),
        display_state
    )   

def chapter2_event5(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_2_event_5(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Masalah Kompas"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Coba arahkan kapal tanpa kompas, menggunakan posisi matahari sebagai panduan.", "value": "matahari"},
        {"name": "Putar arah kembali sedikit untuk mencari arah yang lebih jelas, berharap kompas kembali normal.", "value": "kompas"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'matahari':
        chapter2_event6(game_state['nama_karakter'])
    else:
        chapter2_event6(game_state['nama_karakter'])

def chapter2_event6(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_2_event_6(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Kehabisan Makanan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Hemat makanan dan makan sedikit demi sedikit untuk bertahan lebih lama.", "value": "hemat"},
        {"name": "Lanjutkan memancing meskipun hasilnya sedikit, berharap mendapat lebih banyak ikan.", "value": "memancing"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'hemat':
        chapter2_event7(game_state['nama_karakter'])
    else:
        chapter2_event7(game_state['nama_karakter'])

def chapter2_event7(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_2_event_7(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Arfan Membicarakan Kutukan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Hemat makanan dan makan sedikit demi sedikit untuk bertahan lebih lama.", "value": "hemat"},
        {"name": "Lanjutkan memancing meskipun hasilnya sedikit, berharap mendapat lebih banyak ikan.", "value": "memancing"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'hemat':
        chapter2_event8(game_state['nama_karakter'])
    else:
        chapter2_event8(game_state['nama_karakter'])

def chapter2_event8(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_2_event_8(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Serangan Burung Laut"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Melawan burung-burung itu dengan tongkat untuk mengusir mereka.", "value": "lawan"},
        {"name": "Berlindung di dalam kabin dan berharap burung-burung itu segera pergi.", "value": "berlindung"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'lawan':
        chapter2_event9(game_state['nama_karakter'])
    else:
        chapter2_event9(game_state['nama_karakter'])


def chapter2_event9(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_2_event_9(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Cahaya di Tengah Laut"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mendekati cahaya itu untuk mencari tahu lebih lanjut.", "value": "mendekati"},
        {"name": "Mengabaikan cahaya dan tetap berlayar ke arah Pulau Amba.", "value": "mengabaikan"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Pilih aksi:',
            'choices': options
        }
    ]
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'mendekati':
        chapter2_event10(game_state['nama_karakter'])
    else:
        chapter2_event10(game_state['nama_karakter'])

def chapter2_event10(nama_karakter):
    global game_state

    for line in chapter_2_event_10(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Mendekati Pulau Amba"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        end_chapter, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": f"Berlabuh di pantai dengan hati-hati, {nama_karakter} bersiap untuk masuk ke dalam pulau.", "value": "benar"},
            {"name": f"Berlabuh tanpa persiapan, {nama_karakter} terjatuh dan mati.", "value": "salah"}
        ],
        lambda: chapter2_event10(game_state['nama_karakter']),
        display_state
    )   


def end_chapter(nama_karakter):
    """Akhiri Chapter 2 dan lanjutkan ke Chapter 3"""
    typewriter("Chapter 2 selesai. Permainan berlanjut ke chapter berikutnya...")
    clear_console()
    chapter3(game_state['nama_karakter'])