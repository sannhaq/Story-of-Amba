import sys
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice
from src.story.chapter1 import chapter_1, chapter_1_event_1, chapter_1_event_2, chapter_1_event_3, chapter_1_event_4, chapter_1_event_5, chapter_1_event_6, chapter_1_event_7, chapter_1_event_8, chapter_1_event_9, chapter_1_event_10
from src.story.opening import get_intro

# Inisiasi state permainan.
game_state = {
    "nama_karakter": "",
    "location": "Pantai",
    "inventory": [],
    "progres": "Baru terbangun di pulau"
}

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Inventaris: {', '.join(state['inventory']) if state['inventory'] else 'Tidak ada item'}")
    print(f"Progres: {state['progres']}\n")

def intro():
    global game_state
    """Menampilkan narasi intro dan memeriksa checkpoint."""
    state = load_checkpoint()  # Coba memuat checkpoint
    if state:
        questions = [
            {
                'type': 'list',
                'name': 'continue_game',
                'message': 'Ada checkpoint yang ditemukan. Apakah Anda ingin melanjutkan permainan dari checkpoint?',
                'choices': [
                    {'name': 'Ya', 'value': True},
                    {'name': 'Tidak', 'value': False}
                ]
            }
        ]
        answers = prompt(questions)

        if answers['continue_game']:
            game_state = state  # Memuat state dari checkpoint
            print(f"Melanjutkan dari {game_state['progres']}")
            display_state(game_state)

            if game_state['progres'] == "Baru terbangun di pulau":
                new_game()
            elif game_state['progres'] == "Memasuki gudang rumah":
                chapter1()
            elif game_state['progres'] == "Duduk di lantai gudang":
                chapter1_event1(game_state['nama_karakter'])
            elif game_state['progres'] == "Menyelesaikan event di gudang":
                chapter1_event2(game_state['nama_karakter'])
            elif game_state['progres'] == "Mengumpulkan perbekalan":
                chapter1_event3(game_state['nama_karakter'])
            elif game_state['progres'] == "Mencari teman berlayar":
                chapter1_event4(game_state['nama_karakter'])
            elif game_state['progres'] == "Mendapatkan Kapal":
                chapter1_event5(game_state['nama_karakter'])
            elif game_state['progres'] == "Persiapan Navigasi":
                chapter1_event6(game_state['nama_karakter'])
            elif game_state['progres'] == "Peringatan Warga Desa":
                chapter1_event7(game_state['nama_karakter'])
            elif game_state['progres'] == "Memilih Jalur Berlayar":
                chapter1_event8(game_state['nama_karakter'])
            elif game_state['progres'] == "Mengatasi Keraguan":
                chapter1_event9(game_state['nama_karakter'])
            elif game_state['progres'] == "Keberangkatan":
                chapter1_event10(game_state['nama_karakter'])
        else:
            delete_checkpoint()  # Hapus checkpoint jika pemain tidak mau melanjutkan
            print("Memulai permainan baru...\n")
            new_game()  # Panggil new_game() jika pemain tidak ingin melanjutkan dari checkpoint
    else:
        # Jika tidak ada checkpoint, mulai permainan baru
        new_game()

def new_game():
    global game_state
    """Memulai permainan baru dengan state awal."""
    if not game_state.get("nama_karakter"):
        questions = [
            {
                'type': 'input',
                'name': 'nama_karakter',
                'message': 'Masukkan nama karakter Anda:',
            }
        ]
        answers = prompt(questions)
        game_state["nama_karakter"] = answers["nama_karakter"]  # Simpan nama karakter
        clear_console()

    # Mengatur state permainan ke awal
    game_state.update({
        "location": "Pantai",
        "inventory": [],
        "progres": "Baru terbangun di pulau"
    })

    # Menampilkan narasi intro
    for line in get_intro(game_state['nama_karakter']):
        typewriter(line)
    play_sound('intro.mp3')  # Memutar efek suara intro
    save_checkpoint(game_state)  # Simpan checkpoint di awal permainan
    clear_console()
    chapter1()

def chapter1():
    global game_state
    """Mengelola alur chapter 1."""

    for line in chapter_1(game_state['nama_karakter']):
        typewriter(line)
    game_state["location"] = "Gudang rumah"
    game_state["progres"] = "Memasuki gudang rumah"
    save_checkpoint(game_state)
    clear_console()

    chapter1_event1(game_state['nama_karakter'])

def chapter1_event1(nama_karakter):
    """Event pertama di gudang."""
    global game_state

    # Menampilkan narasi event pertama
    for line in chapter_1_event_1(nama_karakter):
        typewriter(line)
    game_state["location"] = "Lantai gudang"
    game_state["progres"] = "Duduk di lantai gudang"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter1_event2, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Baca surat dengan teliti", "value": "benar"},
            {"name": "Abaikan bagian penting dari surat", "value": "salah"}
        ],
        lambda: chapter1_event1(game_state['nama_karakter']),
        display_state
    )

def chapter1_event2(nama_karakter):
    global game_state

    for line in chapter_1_event_2(nama_karakter):
        typewriter(line)
    game_state["location"] = "Dalam gudang"
    game_state["progres"] = "Menyelesaikan event di gudang"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter1_event3, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Memutuskan untuk mengunjungi museum", "value": "benar"},
            {"name": "Memutuskan berangkat tanpa informasi lebih lanjut", "value": "salah"}
        ],
        lambda: chapter1_event2(game_state['nama_karakter']),
        display_state
    )

def chapter1_event3(nama_karakter):
    global game_state

    for line in chapter_1_event_3(nama_karakter):
        typewriter(line)
    game_state["location"] = "Rumah"
    game_state["progres"] = "Mengumpulkan perbekalan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter1_event4, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Siapkan makanan, air, dan persediaan kesehatan", "value": "benar"},
            {"name": "Membawa perbekalan seadanya", "value": "salah"}
        ],
        lambda: chapter1_event3(game_state['nama_karakter']),
        display_state
    )

def chapter1_event4(nama_karakter):
    global game_state

    for line in chapter_1_event_4(nama_karakter):
        typewriter(line)
    game_state["location"] = "Dermaga"
    game_state["progres"] = "Mencari teman berlayar"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter1_event5, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Pergi sendiri, mengandalkan keberanian dan nalurinya.", "value": "salah"},
            {"name": "Ajak Arfan yang berpengalaman", "value": "benar"}
        ],
        lambda: chapter1_event4(game_state['nama_karakter']),
        display_state
    )

def chapter1_event5(nama_karakter):
    global game_state

    for line in chapter_1_event_5(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Mendapatkan Kapal"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Menyewa kapal kuat namun menghabiskan tabungannya.", "value": "sewa"},
        {"name": "Meminjam kapal ayahnya dan berusaha memperbaikinya.", "value": "pinjam"}
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

    if answers['action'] == 'sewa':
        chapter1_event6(game_state['nama_karakter'])
    else:
        chapter1_event6(game_state['nama_karakter'])

def chapter1_event6(nama_karakter):
    global game_state

    for line in chapter_1_event_6(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Persiapan Navigasi"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter1_event7, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Pelajari dasar navigasi", "value": "benar"},
            {"name": "Abaikan pelatihan navigasi", "value": "salah"}
        ],
        lambda: chapter1_event6(game_state['nama_karakter']),
        display_state
    )

def chapter1_event7(nama_karakter):
    global game_state

    for line in chapter_1_event_7(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Peringatan Warga Desa"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Percayai peringatan warga dan bersiap secara spiritual.", "value": "percaya"},
        {"name": "Abaikan dan lanjutkan rencana dengan lebih percaya diri.", "value": "acuh"}
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

    if answers['action'] == 'percaya':
        chapter1_event8(game_state['nama_karakter'])
    else:
        chapter1_event8(game_state['nama_karakter'])

def chapter1_event8(nama_karakter):
    global game_state

    for line in chapter_1_event_8(nama_karakter):
        typewriter(line)
    game_state["location"] = "Rumah"
    game_state["progres"] = "Memilih Jalur Berlayar"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Lewati jalur aman sesuai saran Arfan.", "value": "aman"},
        {"name": "Pilih jalur singkat demi menghemat waktu.", "value": "singkat"}
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

    if answers['action'] == 'aman':
        chapter1_event9(game_state['nama_karakter'])
    else:
        chapter1_event9(game_state['nama_karakter'])

def chapter1_event9(nama_karakter):
    global game_state

    for line in chapter_1_event_9(nama_karakter):
        typewriter(line)
    game_state["location"] = "Pantai"
    game_state["progres"] = "Mengatasi Keraguan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter1_event10, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Yakinkan diri, merasa bersemangat untuk berangkat keesokan harinya.", "value": "benar"},
            {"name": "Batal pergi, membiarkan ketakutannya menang", "value": "salah"}
        ],
        lambda: chapter1_event9(game_state['nama_karakter']),
        display_state
    )

def chapter1_event10(nama_karakter):
    global game_state

    for line in chapter_1_event_10(nama_karakter):
        typewriter(line)
    game_state["location"] = "Dermaga"
    game_state["progres"] = "Keberangkatan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mengucapkan selamat tinggal pada orang tua untuk mendapatkan restu mereka.", "value": "pamit"},
        {"name": "Pergi tanpa berpamitan, merasa bahwa perpisahan akan membawa kesialan.", "value": "tanpa"}
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

    if answers['action'] == 'pamit':
        end_chapter(game_state['nama_karakter'])
    else:
        end_chapter(game_state['nama_karakter'])

def end_chapter(nama_karakter):
    typewriter("Chapter 1 selesai. Permainan berlanjut ke chapter berikutnya...")
