import sys
import threading
import pygame
import time
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice,add_item_to_inventory,play_sound, play_sound_effect
from src.story.chapter4 import chapter_4, chapter_4_event_1,chapter_4_event_2,chapter_4_event_3,chapter_4_event_4,chapter_4_event_5,chapter_4_event_6,chapter_4_event_7,chapter_4_event_8,chapter_4_event_9,chapter_4_event_10
from src.gameLogic.chapter5_logic import chapter5

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

pygame.mixer.set_num_channels(2)
background_channel = pygame.mixer.Channel(0)
effect_channel = pygame.mixer.Channel(1)

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter4(nama_karakter):
    """Mengelola alur chapter 4."""
    for line in chapter_4(nama_karakter):
        typewriter(line)
    
    # Mengupdate status game
    game_state["location"] = "Kuil"  # Update lokasi
    game_state["progres"] = "Dalam Bayang-Bayang Kuil"  # Update progres
    
    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter4_event1(game_state['nama_karakter'])

def chapter4_event1(nama_karakter):
    global game_state
    gravel_thread = threading.Thread(target=play_sound_effect, args=("Footsteps in Gravel.mp3", True, 1))
    run_thread = threading.Thread(target=play_sound_effect, args=("Run.mp3", True, 0))
    run_thread.start()
    gravel_thread.start()
    for line in chapter_4_event_1(nama_karakter):
        typewriter(line)
    game_state["location"] = "Pintu Besar"
    game_state["progres"] = "Pintu yang terkunci"
    background_channel.stop()
    add_item_to_inventory('Peta Kuno')
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter4_event2, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Meletakkan tangan di atas batu untuk membuka pintu.", "value": "benar"},
            {"name": "Mengabaikan batu dan mencoba mendorong pintu", "value": "salah"}
        ],
        lambda: chapter4_event1(game_state['nama_karakter']),
        display_state
    )
        
def chapter4_event2(nama_karakter):
    global game_state
    horrorsound_thread = threading.Thread(target=play_sound_effect, args=("horrorsound.mp3", True, 0))
    horrorsound_thread.start()
    rustlingpaper_thread = threading.Thread(target=play_sound_effect, args=("Rustling Paper.mp3", True, 1))
    rustlingpaper_thread.start()
    for line in chapter_4_event_2(nama_karakter):
        typewriter(line)
    game_state["location"] = "Lorong sempit"
    game_state["progres"] = "Gema di lorong gelap"
    background_channel.stop()
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter4_event3, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Bergerak cepat ke arah cahaya untuk mencari tahu sumbernya.", "value": "benar"},
            {"name": "Berdiri diam, menunggu suara itu mendekat.", "value": "salah"}
        ],
        lambda: chapter4_event2(game_state['nama_karakter']),
        display_state
    )

def chapter4_event3(nama_karakter):
    global game_state
    gong_thread = threading.Thread(target=play_sound_effect, args=("gong.mp3", True, 0))
    gong_thread.start()
    for line in chapter_4_event_3(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Jalan Berliku dan Tanda Darah"
    background_channel.stop()
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mengikuti jejak darah yang tampaknya menuju ke sebuah pintu besar.", "value": "ikuti"},
        {"name": "Menghindari jejak darah dan mengambil jalur yang tampaknya lebih aman.", "value": "hindari"}
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

    if answers['action'] == 'ikuti':
        chapter4_event4(game_state['nama_karakter'])
    else:
        chapter4_event4(game_state['nama_karakter'])

def chapter4_event4(nama_karakter):
    global game_state
    mysterysound_thread = threading.Thread(target=play_sound_effect, args=("mysterysong.mp3", True, 0))
    weirdsound_thread = threading.Thread(target=play_sound_effect, args=("sfxaneh.mp3", True, 1))
    weirdsound_thread.start()
    mysterysound_thread.start()
    for line in chapter_4_event_4(nama_karakter):
        typewriter(line)
    game_state["location"] = "jalan Berliku"
    game_state["progres"] = "Teka-teki Suara"
    background_channel.stop()
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter4_event5, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Memecahkan teka-teki berdasarkan petunjuk yang ditemukan", "value": "benar"},
            {"name": "Menebak dengan sembarangan", "value": "salah"}
        ],
        lambda: chapter4_event4(game_state['nama_karakter']),
        display_state
    )
def chapter4_event5(nama_karakter):
    global game_state
    woodcrack_thread = threading.Thread(target=play_sound_effect, args=("Wood Creaking.mp3", True, 0))
    boom = threading.Thread(target=play_sound_effect, args=("boom.mp3", True, 1))
    woodcrack_thread.start()
    boom.start()
    for line in chapter_4_event_5(nama_karakter):
        typewriter(line)
    game_state["location"] = "lorong jauh"
    game_state["progres"] = "Lorong dengan Pijakan yang Runtuh"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter4_event6, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Langkah hati-hati dan pastikan untuk menghindari tempat-tempat yang rapuh.", "value": "benar"},
            {"name": "Mengambil langkah cepat", "value": "salah"}
        ],
        lambda: chapter4_event5(game_state['nama_karakter']),
        display_state
    )

def chapter4_event6(nama_karakter):
    global game_state
    growl_thread = threading.Thread(target=play_sound_effect, args=("growl.mp3", True, 0))
    colossalboom = threading.Thread(target=play_sound_effect, args=("colossal.mp3", True, 1))
    growl_thread.start()
    colossalboom.start()
    for line in chapter_4_event_6(nama_karakter):
        typewriter(line)
    game_state["location"] = "lorong dalam"
    game_state["progres"] = "Makhluk Misterius"
    background_channel.stop()
    add_item_to_inventory('Lendir Monster')
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter4_event7, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Bersembunyi di balik batu besar untuk menghindari makhluk tersebut.", "value": "benar"},
            {"name": "Mencoba melawan makhluk itu", "value": "salah"}
        ],
        lambda: chapter4_event6(game_state['nama_karakter']),
        display_state
    )
        
def chapter4_event7(nama_karakter):
    global game_state
    gong = threading.Thread(target=play_sound_effect, args=("gong.mp3", True, 0))
    gong.start()
    for line in chapter_4_event_7(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Pintu yang Terbuka dengan Kunci"
    background_channel.stop()
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Mencari petunjuk di ruangan sekitarnya untuk menemukan kunci yang hilang.", "value": "cari"},
        {"name": "Mencoba membuka pintu dengan kekuatan fisik", "value": "paksa"}
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

    if answers['action'] == 'cari':
        chapter4_event8(game_state['nama_karakter'])
    else:
        chapter4_event8(game_state['nama_karakter'])

def chapter4_event8(nama_karakter):
    global game_state
    cradle = threading.Thread(target=play_sound_effect, args=("cradle.mp3", True, 0))
    cradle.start()
    for line in chapter_4_event_8(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Tempat Terlarang"
    game_state["location"] = "Ruangan Artefak"
    background_channel.stop()
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Menjauh dari tempat terlarang dan mencari jalan lain.", "value": "menjauh"},
        {"name": "Mencoba melanggar pagar energi dengan hati-hati", "value": "melanggar"}
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

    if answers['action'] == 'menjauh':
        chapter4_event9(game_state['nama_karakter'])
    else:
        chapter4_event9(game_state['nama_karakter'])

def chapter4_event9(nama_karakter):
    global game_state
    tomb = threading.Thread(target=play_sound_effect, args=("tomb.mp3", True, 0))
    tomb.start()
    for line in chapter_4_event_9(nama_karakter):
        typewriter(line)
    
    game_state["progres"] = "Teka-teki Batu Raksasa"
    background_channel.stop()
    save_checkpoint(game_state)

    process_player_choice(
        chapter4_event10, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Memecahkan teka-teki batu berdasarkan pola yang ada di dinding.", "value": "benar"},
            {"name": "Mencoba memindahkan batu", "value": "salah"}
        ],
        lambda: chapter4_event9(game_state['nama_karakter']),
        display_state
    )
        
def chapter4_event10(nama_karakter):
    global game_state
    mysterysong = threading.Thread(target=play_sound_effect, args=("mysterysong.mp3", True, 0))
    mysterysong.start()
    for line in chapter_4_event_10(nama_karakter):
        typewriter(line)
    game_state["location"] = "Ruang Harta Karun"
    game_state["progres"] = "Ruang Harta Karun"
    background_channel.stop()
    add_item_to_inventory('Emas')
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        end_chapter, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Mengambil artefak dengan hati-hati dan memeriksa apa yang membuatnya sangat istimewa.", "value": "benar"},
            {"name": "Melompat ke tumpukan harta karun", "value": "salah"}
        ],
        lambda: chapter4_event10(game_state['nama_karakter']),
        display_state
    )
def end_chapter(nama_karakter):
    """Akhiri Chapter 4 dan lanjutkan ke Chapter 5"""
    typewriter("Chapter 4 selesai. Permainan berlanjut ke chapter berikutnya...")
    time.sleep(2)
    clear_console()
    chapter5(game_state['nama_karakter'])