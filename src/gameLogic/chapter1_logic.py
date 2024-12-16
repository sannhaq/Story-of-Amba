import sys
import time
import pygame
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, typewriter, game_over_prompt, process_player_choice, add_item_to_inventory, show_player_choices, play_sound, play_sound_effect
from src.story.chapter1 import chapter_1, chapter_1_event_1, chapter_1_event_2, chapter_1_event_3, chapter_1_event_4, chapter_1_event_4_2, chapter_1_event_5, chapter_1_event_6, chapter_1_event_7, chapter_1_event_8, chapter_1_event_9, chapter_1_event_10
from src.story.opening import get_intro
from src.gameLogic.chapter2_logic import chapter2

# Inisiasi state permainan.
game_state = {
    "nama_karakter": "",
    "location": "Pantai",
    "progres": "Baru terbangun di pulau"
}

pygame.mixer.set_num_channels(2)

background_channel = pygame.mixer.Channel(0)
effect_channel = pygame.mixer.Channel(1)

def lanjutkan_game_dari_checkpoint(answers, state):
    from src.gameLogic.chapter2_logic import chapter2, chapter2_event1, chapter2_event2, chapter2_event3, chapter2_event4, chapter2_event5, chapter2_event6, chapter2_event7, chapter2_event8, chapter2_event9, chapter2_event10
    from src.gameLogic.chapter3_logic import chapter3, chapter3_event1, chapter3_event2, chapter3_event3, chapter3_event4, chapter3_event5, chapter3_event6, chapter3_event7, chapter3_event8, chapter3_event9, chapter3_event10
    from src.gameLogic.chapter4_logic import chapter4, chapter4_event1, chapter4_event2, chapter4_event3, chapter4_event4, chapter4_event5, chapter4_event6, chapter4_event7, chapter4_event8, chapter4_event9, chapter4_event10
    from src.gameLogic.chapter5_logic import chapter5, chapter5_event1, chapter5_event2, chapter5_event3, chapter5_event4, chapter5_event5, chapter5_event6, chapter5_event7, chapter5_event8, chapter5_event9, chapter5_event10

    global game_state
    if answers['continue_game']:
        game_state = state  # Memuat state dari checkpoint
        print(f"Melanjutkan dari {game_state['progres']}")
        display_state(game_state)

        # Logika berdasarkan progres
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

        # Progres untuk Chapter 2
        elif game_state['progres'] == "Perjalanan ke Pulau Amba":
            chapter2(game_state['nama_karakter'])
        elif game_state['progres'] == "Badai di Tengah Malam":
            chapter2_event1(game_state['nama_karakter'])
        elif game_state['progres'] == "Mengatasi kehausan":
            chapter2_event2(game_state['nama_karakter'])
        elif game_state['progres'] == "Hantu Kapal Bajak Laut":
            chapter2_event3(game_state['nama_karakter'])
        elif game_state['progres'] == "Perbaikan Layar yang Rusak":
            chapter2_event4(game_state['nama_karakter'])
        elif game_state['progres'] == "Masalah Kompas":
            chapter2_event5(game_state['nama_karakter'])
        elif game_state['progres'] == "Kehabisan Makanan":
            chapter2_event6(game_state['nama_karakter'])
        elif game_state['progres'] == "Arfan Membicarakan Kutukan":
            chapter2_event7(game_state['nama_karakter'])
        elif game_state['progres'] == "Serangan Burung Laut":
            chapter2_event8(game_state['nama_karakter'])
        elif game_state['progres'] == "Cahaya di Tengah Laut":
            chapter2_event9(game_state['nama_karakter'])
        elif game_state['progres'] == "Mendekati Pulau Amba":
            chapter2_event10(game_state['nama_karakter'])

        # Progres untuk Chapter 3
        elif game_state['progres'] == "Misteri Pulau Amba":
            chapter3(game_state['nama_karakter'])
        elif game_state['progres'] == "Jejak yang Tertinggal":
            chapter3_event1(game_state['nama_karakter'])
        elif game_state['progres'] == "Pohon Tua Berukir Simbol Aneh":
            chapter3_event2(game_state['nama_karakter'])
        elif game_state['progres'] == "Rintangan Jaring Laba-Laba":
            chapter3_event3(game_state['nama_karakter'])
        elif game_state['progres'] ==  "Lorong Batu di Perbukitan":
            chapter3_event4(game_state['nama_karakter'])
        elif game_state['progres'] == "Peti Kuno Berpaku Karat":
            chapter3_event5(game_state['nama_karakter'])
        elif game_state['progres'] == "Sumur Tua yang Terbengkalai":
            chapter3_event6(game_state['nama_karakter'])
        elif game_state['progres'] == "Jejak Cahaya di Kegelapan":
            chapter3_event7(game_state['nama_karakter'])
        elif game_state['progres'] ==  "Pertemuan dengan Patung Batu Berwajah Marah":
            chapter3_event8(game_state['nama_karakter'])
        elif game_state['progres'] == "Mencari Jalan di Reruntuhan Kuil Tua":
            chapter3_event9(game_state['nama_karakter'])
        elif game_state['progres'] == "Kode Tersembunyi pada Dinding":
            chapter3_event10(game_state['nama_karakter'])
    
        # Progres untuk Chapter 4
        elif game_state['progres'] == "Dalam Bayang-Bayang Kuil":
            chapter4(game_state['nama_karakter'])
        elif game_state['progres'] == "Pintu yang terkunci":
            chapter4_event1(game_state['nama_karakter'])
        elif game_state['progres'] == "Gema di lorong gelap":
            chapter4_event2(game_state['nama_karakter'])
        elif game_state['progres'] == "Jalan Berliku dan Tanda Darah":
            chapter4_event3(game_state['nama_karakter'])
        elif game_state['progres'] == "Teka-teki Suara":
            chapter4_event4(game_state['nama_karakter'])
        elif game_state['progres'] == "Lorong dengan Pijakan yang Runtuh":
            chapter4_event5(game_state['nama_karakter'])
        elif game_state['progres'] == "Makhluk Misterius":
            chapter4_event6(game_state['nama_karakter'])
        elif game_state['progres'] == "Pintu yang Terbuka dengan Kunci":
            chapter4_event7(game_state['nama_karakter'])
        elif game_state['progres'] == "Tempat Terlarang":
            chapter4_event8(game_state['nama_karakter'])
        elif game_state['progres'] == "Teka-teki Batu Raksasa":
            chapter4_event9(game_state['nama_karakter'])
        elif game_state['progres'] == "Ruang Harta Karun":
            chapter4_event10(game_state['nama_karakter'])

        # Progres untuk Chapter 5
        elif game_state['progres'] == "Rahasia Artefak Kuno":
            chapter5(game_state['nama_karakter'])
        elif game_state['progres'] == "Suara berbisik dari artefak":
            chapter5_event1(game_state['nama_karakter'])
        elif game_state['progres'] == "Jalan Keluar yang Hilang":
            chapter5_event2(game_state['nama_karakter'])
        elif game_state['progres'] == "Pengawal Bayangan":
            chapter5_event3(game_state['nama_karakter'])
        elif game_state['progres'] == "Jalan Buntu dengan Gua Gelap":
            chapter5_event4(game_state['nama_karakter'])
        elif game_state['progres'] == "Rantai Misterius yang Menghalangi Jalan":
            chapter5_event5(game_state['nama_karakter'])
        elif game_state['progres'] == "Cermin Pemanggil Kenangan":
            chapter5_event6(game_state['nama_karakter'])
        elif game_state['progres'] == "Serangan Jebakan Tombak":
            chapter5_event7(game_state['nama_karakter'])
        elif game_state['progres'] == "Persimpangan Berbahaya":
            chapter5_event8(game_state['nama_karakter'])
        elif game_state['progres'] == "Gerbang Terakhir":
            chapter5_event9(game_state['nama_karakter'])
        elif game_state['progres'] == "Pengorbanan Terakhir":
            chapter5_event10(game_state['nama_karakter'])

    else:
        delete_checkpoint()  # Hapus checkpoint jika pemain tidak mau melanjutkan
        print("Memulai permainan baru...\n")
        new_game()


def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
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
        clear_console()
        lanjutkan_game_dari_checkpoint(answers, state)
    else:
        # Jika tidak ada checkpoint, mulai permainan baru
        new_game()


def new_game():
    global game_state

    # Menghapus nama karakter jika sebelumnya sudah ada
    game_state["nama_karakter"] = ""  # Reset nama karakter

    """Memulai permainan baru dengan state awal."""
    while not game_state.get("nama_karakter"):
        questions = [
            {
                'type': 'input',
                'name': 'nama_karakter',
                'message': 'Masukkan nama karakter Anda (tidak boleh kosong):',
            }
        ]
        answers = prompt(questions)
        nama_karakter = answers.get("nama_karakter", "").strip()

        if nama_karakter:
            game_state["nama_karakter"] = nama_karakter
            clear_console()
        else:
            print("Nama tidak boleh kosong! Silakan coba lagi.")

    # Mengatur state permainan ke awal
    game_state.update({
        "location": "Pantai",
        "progres": "Baru terbangun di pulau"
    })

    # Menampilkan narasi intro
    for line in get_intro(game_state['nama_karakter']):
        typewriter(line)
    play_sound_effect("intro.mp3", is_background=True)
    
    # Tunggu sampai efek suara intro selesai
    while background_channel.get_busy():
        pygame.time.Clock().tick(10)
    
    save_checkpoint(game_state)
    clear_console()
    chapter1()

def chapter1():
    global game_state
    """Mengelola alur chapter 1."""

    wood_thread = threading.Thread(target=play_sound_effect, args=("Wood Creaking.mp3", True, 0))
    wind_thread = threading.Thread(target=play_sound_effect, args=("wind.mp3", True, 1))
    wood_thread.start()
    wind_thread.start()

    for line in chapter_1(game_state['nama_karakter']):
        typewriter(line)
    background_channel.stop()
    print("\n")
    add_item_to_inventory('Surat')
    game_state["location"] = "Gudang rumah"
    game_state["progres"] = "Memasuki gudang rumah"
    save_checkpoint(game_state)
    clear_console()

    chapter1_event1(game_state['nama_karakter'])


def chapter1_event1(nama_karakter):
    """Event pertama di gudang."""
    global game_state

    music_thread = threading.Thread(target=play_sound_effect, args=("Rustling Paper.mp3", True))
    music_thread.start()

    # Menampilkan narasi event pertama
    for line in chapter_1_event_1(nama_karakter):
        typewriter(line)
    background_channel.stop()
    print("\n")
    add_item_to_inventory('Peta Kuno')
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

    foot_thread = threading.Thread(target=play_sound_effect, args=("Footsteps in Gravel.mp3", True, 0))
    water_thread = threading.Thread(target=play_sound_effect, args=("Water Splash.mp3", True, 1))
    foot_thread.start()
    water_thread.start()

    for line in chapter_1_event_2(nama_karakter):
        typewriter(line)
    background_channel.stop()
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
    print("\n")
    add_item_to_inventory('Pisau Saku')
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

    play_sound_effect("Fishing Rod Tell.mp3")
    fishing_thread = threading.Thread(target=play_sound_effect, args=("Fishing Rod Tell.mp3", True))
    fishing_thread.start()

    for line in chapter_1_event_4(nama_karakter):
        typewriter(line)
    
    background_channel.stop()

    man_thread = threading.Thread(target=play_sound_effect, args=("old man.mp3", True))
    man_thread.start()

    for line in chapter_1_event_4_2(nama_karakter):
        typewriter(line)
    
    background_channel.stop()

    print("\n")
    add_item_to_inventory('Kerang Ajaib')
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

    music_thread = threading.Thread(target=play_sound_effect, args=("Sails flapping in the wind.mp3", True))
    music_thread.start()

    for line in chapter_1_event_5(nama_karakter):
        typewriter(line)
    background_channel.stop()
    game_state["progres"] = "Mendapatkan Kapal"
    save_checkpoint(game_state)

    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Menyewa kapal kuat namun menghabiskan tabungannya.", "value": "sewa"},
        {"name": "Meminjam kapal ayahnya dan berusaha memperbaikinya.", "value": "pinjam"},
    ]
    
    event_mapping = {
        "sewa": chapter1_event6,
        "pinjam": chapter1_event6,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)

def chapter1_event6(nama_karakter):
    global game_state

    music_thread = threading.Thread(target=play_sound_effect, args=("Twinkling Stars.mp3", True))
    music_thread.start()

    for line in chapter_1_event_6(nama_karakter):
        typewriter(line)
    
    background_channel.stop()

    print("\n")
    add_item_to_inventory(['Kompas', 'Buku Navigasi'])
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
    print("\n")
    add_item_to_inventory('Jimat Pelindung')
    game_state["progres"] = "Peringatan Warga Desa"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Percayai peringatan warga dan bersiap secara spiritual.", "value": "percaya"},
        {"name": "Abaikan dan lanjutkan rencana dengan lebih percaya diri.", "value": "acuh"}
    ]

    event_mapping = {
        "percaya": chapter1_event8,
        "acuh": chapter1_event8,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter1_event8(nama_karakter):
    global game_state

    music_thread = threading.Thread(target=play_sound_effect, args=("wind2.mp3", True))
    music_thread.start()

    for line in chapter_1_event_8(nama_karakter):
        typewriter(line)
    
    background_channel.stop()

    game_state["location"] = "Rumah"
    game_state["progres"] = "Memilih Jalur Berlayar"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Lewati jalur aman sesuai saran Arfan.", "value": "aman"},
        {"name": "Pilih jalur singkat demi menghemat waktu.", "value": "singkat"}
    ]

    event_mapping = {
        "aman": chapter1_event9,
        "singkat": chapter1_event9,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)

def chapter1_event9(nama_karakter):
    global game_state

    music_thread = threading.Thread(target=play_sound_effect, args=("Water Splash.mp3", True))
    music_thread.start()

    for line in chapter_1_event_9(nama_karakter):
        typewriter(line)
    
    background_channel.stop()

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

    music_thread = threading.Thread(target=play_sound_effect, args=("pirates.mp3", True, 0))
    boat_thread = threading.Thread(target=play_sound_effect, args=("Boat Horn.mp3", True, 1))
    boat_thread.start()
    music_thread.start()

    for line in chapter_1_event_10(nama_karakter):
        typewriter(line)
        
    print("\n")
    add_item_to_inventory('Kacamata')
    game_state["location"] = "Dermaga"
    game_state["progres"] = "Keberangkatan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mengucapkan selamat tinggal pada orang tua untuk mendapatkan restu mereka.", "value": "pamit"},
        {"name": "Pergi tanpa berpamitan, merasa bahwa perpisahan akan membawa kesialan.", "value": "tanpa"}
    ]
    
    event_mapping = {
        "pamit": end_chapter,
        "tanpa": end_chapter,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)

def end_chapter(nama_karakter):
    """Akhiri Chapter 1 dan lanjutkan ke Chapter 2"""
    typewriter("Chapter 1 selesai. Permainan berlanjut ke chapter berikutnya...")
    time.sleep(2)
    background_channel.stop()
    clear_console()
    chapter2(game_state['nama_karakter'])
