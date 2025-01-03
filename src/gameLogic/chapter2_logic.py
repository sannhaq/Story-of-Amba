import sys
import threading
import time
import pygame
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, typewriter, game_over_prompt, process_player_choice, add_item_to_inventory, show_player_choices, play_sound, play_sound_effect
from src.story.chapter2 import chapter_2, chapter_2_event_1, chapter_2_event_2, chapter_2_event_3, chapter_2_event_4, chapter_2_event_5, chapter_2_event_6, chapter_2_event_7, chapter_2_event_8, chapter_2_event_9, chapter_2_event_10
from src.gameLogic.chapter3_logic import chapter3

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

pygame.mixer.set_num_channels(2)

background_channel = pygame.mixer.Channel(0)
effect_channel = pygame.mixer.Channel(1)


def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"nama_karakter:f {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")


def chapter2(nama_karakter):
    """Mengelola alur chapter 2."""

    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 0))
    ocean_thread.start()

    for line in chapter_2(nama_karakter):
        typewriter(line)
    background_channel.stop()
    # Mengupdate status game
    game_state["location"] = "Kapal"  # Update lokasi
    game_state["progres"] = "Perjalanan ke Pulau Amba"  # Update progres

    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter2_event1(game_state['nama_karakter'])


def chapter2_event1(nama_karakter):
    global game_state

    storm_thread2 = threading.Thread(
        target=play_sound_effect, args=("rain-thunder.mp3", True, 0))
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 1))
    storm_thread2.start()
    ocean_thread.start()

    for line in chapter_2_event_1(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()

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

    spaceship_ambient = threading.Thread(
        target=play_sound_effect, args=("spaceship-ambient.mp3", True, 0))
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 1))
    spaceship_ambient.start()
    ocean_thread.start()

    for line in chapter_2_event_2(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()
    game_state["progres"] = "Mengatasi kehausan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter2_event3,
        game_state,
        "Pilih aksi:",
        [
            {"name": "Minum banyak air tanpa menghemat — persediaan air cepat habis dan mereka kelelahan karena dehidrasi.", "value": "salah"},
            {"name": f"Hemat air dan berbagi sisa air dengan bijak, {
                nama_karakter} dan Arfan bertahan sampai menemukan cara untuk mendapatkan air segar di pulau nanti.", "value": "benar"},
        ],
        lambda: chapter2_event2(game_state['nama_karakter']),
        display_state
    )


def chapter2_event3(nama_karakter):
    global game_state

    horror_thread = threading.Thread(
        target=play_sound_effect, args=("Gathering Darkness.mp3", True, 0))
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 1))
    horror_thread.start()
    ocean_thread.start()

    for line in chapter_2_event_3(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()

    game_state["progres"] = "Hantu Kapal Bajak Laut"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Dekati kapal itu dan periksa lebih dekat (berpotensi memicu gangguan supernatural).",
         "value": "dekati kapal"},
        {"name": f"Abaikan kapal tersebut dan kembali tidur ({
            nama_karakter} menghindari bahaya misterius).", "value": "abaikan"}
    ]
    event_mapping = {
        "dekati kapal": chapter2_event4,
        "abaikan": chapter2_event4
    }
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter2_event4(nama_karakter):
    global game_state
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 0))
    hammer_thread = threading.Thread(
        target=play_sound_effect, args=("hammering.mp3", True, 1))
    ocean_thread.start()
    hammer_thread.start()

    for line in chapter_2_event_4(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()
    print("\n")
    add_item_to_inventory("Tali Tambang")

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

    mysterious_ambience = threading.Thread(
        target=play_sound_effect, args=("Mysterious Ambience.mp3", True, 0))
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 1))
    mysterious_ambience.start()
    ocean_thread.start()

    for line in chapter_2_event_5(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()

    print("\n")
    add_item_to_inventory("Magnet")

    game_state["progres"] = "Masalah Kompas"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Coba arahkan kapal tanpa kompas, menggunakan posisi matahari sebagai panduan.",
            "value": "matahari"},
        {"name": "Putar arah kembali sedikit untuk mencari arah yang lebih jelas, berharap kompas kembali normal.", "value": "kompas"}
    ]

    event_mapping = {
        "matahari": chapter2_event6,
        "kompas": chapter2_event6
    }

    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter2_event6(nama_karakter):
    global game_state

    fishing_thread = threading.Thread(
        target=play_sound_effect, args=("Fishing Rod Tell.mp3", True, 0))
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 1))
    fishing_thread.start()
    ocean_thread.start()

    for line in chapter_2_event_6(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()

    game_state["progres"] = "Kehabisan Makanan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Hemat makanan dan makan sedikit demi sedikit untuk bertahan lebih lama.", "value": "hemat"},
        {"name": "Lanjutkan memancing meskipun hasilnya sedikit, berharap mendapat lebih banyak ikan.", "value": "memancing"}
    ]

    event_mapping = {
        "hemat": chapter2_event7,
        "memancing": chapter2_event7
    }

    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter2_event7(nama_karakter):
    global game_state

    horror_thread = threading.Thread(
        target=play_sound_effect, args=("horror.mp3", True, 0))
    ocean_thread = threading.Thread(
        target=play_sound_effect, args=("ocean-waves.mp3", True, 1))
    horror_thread.start()
    ocean_thread.start()

    for line in chapter_2_event_7(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()
    game_state["progres"] = "Arfan Membicarakan Kutukan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Percaya pada cerita Arfan dan berdoa untuk keselamatan.", "value": "percaya"},
        {"name": "Abaikan cerita tersebut dan memilih tetap fokus pada tujuan.", "value": "abaikan"}
    ]

    event_mapping = {
        "percaya": chapter2_event8,
        "abaikan": chapter2_event8
    }

    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter2_event8(nama_karakter):
    global game_state

    bird_thread = threading.Thread(
        target=play_sound_effect, args=("bird.mp3", True, 0))
    panic_thread = threading.Thread(
        target=play_sound_effect, args=("panic.mp3", True, 1))
    bird_thread.start()
    panic_thread.start()

    for line in chapter_2_event_8(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()
    game_state["progres"] = "Serangan Burung Laut"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Melawan burung-burung itu dengan tongkat untuk mengusir mereka.",
            "value": "lawan"},
        {"name": "Berlindung di dalam kabin dan berharap burung-burung itu segera pergi.",
            "value": "berlindung"}
    ]

    event_mapping = {
        "lawan": chapter2_event9,
        "berlindung": chapter2_event9
    }

    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter2_event9(nama_karakter):
    global game_state

    light_thread = threading.Thread(
        target=play_sound_effect, args=("Magical Light.mp3", True, 0))
    horror_thread = threading.Thread(
        target=play_sound_effect, args=("Dark Tension.mp3", True, 1))
    light_thread.start()
    horror_thread.start()

    for line in chapter_2_event_9(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()
    print("\n")
    add_item_to_inventory("Lentera")

    game_state["progres"] = "Cahaya di Tengah Laut"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mendekati cahaya itu untuk mencari tahu lebih lanjut.",
            "value": "mendekati"},
        {"name": "Mengabaikan cahaya dan tetap berlayar ke arah Pulau Amba.",
            "value": "mengabaikan"}
    ]

    event_mapping = {
        "mendekati": chapter2_event10,
        "mengabaikan": chapter2_event10
    }

    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)


def chapter2_event10(nama_karakter):
    global game_state

    wind_thread = threading.Thread(
        target=play_sound_effect, args=("Creepy Wind.mp3", True, 0))
    mysterious_ambience = threading.Thread(
        target=play_sound_effect, args=("Mysterious Ambience.mp3", True, 1))
    wind_thread.start()
    mysterious_ambience.start()

    for line in chapter_2_event_10(nama_karakter):
        typewriter(line)
    background_channel.stop()
    effect_channel.stop()
    print("\n")
    add_item_to_inventory("Peta Pulau Amba")

    game_state["progres"] = "Mendekati Pulau Amba"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        end_chapter,
        game_state,
        "Pilih aksi:",
        [
            {"name": f"Berlabuh di pantai dengan hati-hati, {
                nama_karakter} bersiap untuk masuk ke dalam pulau.", "value": "benar"},
            {"name": f"Berlabuh tanpa persiapan, {
                nama_karakter} terjatuh dan mati.", "value": "salah"}
        ],
        lambda: chapter2_event10(game_state['nama_karakter']),
        display_state
    )


def end_chapter(nama_karakter):
    """Akhiri Chapter 2 dan lanjutkan ke Chapter 3"""
    typewriter("Chapter 2 selesai. Permainan berlanjut ke chapter berikutnya...")
    time.sleep(2)
    clear_console()
    chapter3(game_state['nama_karakter'])
