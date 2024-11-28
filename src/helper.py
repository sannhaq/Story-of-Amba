import json
import os
from prettytable import PrettyTable
import pygame
import sys
import threading
import time
from InquirerPy import prompt

CHECKPOINT_DIR = 'system'
CHECKPOINT_FILE = os.path.join(CHECKPOINT_DIR, 'checkpoint.json')
INVENTORY_FILE = os.path.join(CHECKPOINT_DIR, 'inventory.json')

pygame.mixer.init()
pygame.mixer.set_num_channels(2)

background_channel = pygame.mixer.Channel(0)
effect_channel = pygame.mixer.Channel(1)

def ensure_inventory_file():
    """Pastikan file inventory.json ada."""
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "w") as f:
            json.dump([], f)

def load_inventory():
    """Memuat inventory dari file."""
    ensure_inventory_file()
    try:
        with open(INVENTORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Gagal memuat inventory: format file tidak valid.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat memuat inventory: {e}")
        return []


def save_inventory(inventory):
    """Menyimpan inventory ke file."""
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f)

def delete_inventory():
    """Menghapus file inventory.json."""
    if os.path.exists(INVENTORY_FILE):
        os.remove(INVENTORY_FILE)

def ensure_checkpoint_dir():
    """Membuat folder checkpoints jika belum ada."""
    if not os.path.exists(CHECKPOINT_DIR):
        os.makedirs(CHECKPOINT_DIR)
        print(f"Folder '{CHECKPOINT_DIR}' dibuat untuk menyimpan checkpoint.")

def save_checkpoint(state):
    """Menyimpan state permainan ke file checkpoint."""
    ensure_checkpoint_dir()  # Pastikan folder checkpoints sudah ada
    with open(CHECKPOINT_FILE, 'w') as file:
        json.dump(state, file)
    print("\nCheckpoint tersimpan.")

def load_checkpoint():
    """Memuat state permainan dari file checkpoint jika ada."""
    try:
        with open(CHECKPOINT_FILE, 'r') as file:
            state = json.load(file)
        print("Checkpoint dimuat.")
        return state
    except FileNotFoundError:
        print("Tidak ada checkpoint yang ditemukan.")
        clear_console()
        return None  # Mengembalikan None jika tidak ada checkpoint

def delete_checkpoint():
    """Menghapus file checkpoint jika ada."""
    if os.path.exists(CHECKPOINT_FILE):
        os.remove(CHECKPOINT_FILE)
        print("Checkpoint dihapus.")
        delete_inventory()
    else:
        print("Tidak ada checkpoint yang ditemukan untuk dihapus.")

def clear_console():
    """Menghapus layar console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_sound_effect(sound_file, is_background=False, channel_id=None):
    """Memutar file suara yang diberikan."""
    sound_file_path = os.path.join('assets/sounds', sound_file).replace('\\', '/')
    
    if os.path.exists(sound_file_path):
        try:
            sound = pygame.mixer.Sound(sound_file_path)
            
            # Gunakan channel tertentu atau cari channel kosong
            if channel_id is not None:
                channel = pygame.mixer.Channel(channel_id)
            else:
                channel = pygame.mixer.find_channel()

            if channel:
                channel.play(sound, loops=0 if is_background else 0)
            else:
                print(f"Tidak ada channel yang tersedia untuk memutar '{sound_file}'")
        except pygame.error as e:
            print(f"Gagal memutar suara '{sound_file}': {e}")
    else:
        print(f"File suara '{sound_file}' tidak ditemukan.")

def play_sound(sound_file):
    """Memutar file suara yang diberikan."""
    # Tentukan path file suara
    sound_file_path = os.path.join('assets/sounds', sound_file).replace('\\', '/')
    
    # Periksa apakah file suara ada
    if os.path.exists(sound_file_path):
        # Inisialisasi pygame mixer untuk memutar suara
        pygame.mixer.init()
        
        # Memuat dan memutar suara
        try:
            pygame.mixer.music.load(sound_file_path)
            pygame.mixer.music.play()
            
            # Tunggu hingga suara selesai diputar
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)  # Menjaga agar program tidak mengganggu suara
        except pygame.error as e:
            print(f"Gagal memutar suara '{sound_file}': {e}")
    else:
        print(f"File suara '{sound_file}' tidak ditemukan.")

# Fungsi untuk mencetak teks dengan efek typewriter
def typewriter(text, typing_sound_file='typing.mp3', delay=0.05):
    """Menampilkan teks dengan efek typewriter dan suara ketikan."""
    # Jalankan suara ketikan di thread terpisah
    sound_thread = threading.Thread(target=play_sound, args=(typing_sound_file,))
    sound_thread.start()  # Memulai suara ketikan

    for char in text:
        sys.stdout.write(char)  # Menulis karakter ke console
        sys.stdout.flush()  # Memaksa output ke console
        time.sleep(delay)  # Delay antara karakter

    # Hentikan suara ketikan setelah selesai
    pygame.mixer.music.stop()
    sound_thread.join()  # Tunggu hingga suara ketikan selesai
    print()  # Pindah ke baris baru setelah teks selesai dicetak

def game_over_prompt(game_state, load_checkpoint, display_state, restart_chapter, restart_args=()):
    """Menampilkan pesan Game Over dan memberikan opsi untuk mengulang dari checkpoint."""
    typewriter("Game Over, apakah anda ingin mengulang game dari checkpoint?")
    
    # Menampilkan prompt pilihan ulang
    questions = [
        {
            'type': 'confirm',
            'name': 'restart',
            'message': 'Apakah anda ingin mengulang dari checkpoint?',
            'default': True
        }
    ]
    restart_answer = prompt(questions)
    
    if restart_answer['restart']:
        game_state.update(load_checkpoint())
        display_state(game_state)
        restart_chapter(*restart_args)
    else:
        print("Permainan berakhir. Terima kasih telah bermain!")
        sys.exit()

def process_player_choice(event_func, game_state, message, options, fail_func, display_state):
    while True:
        # Tambahkan opsi 'Lihat Inventory'
        extended_options = options + [{"name": "Lihat Inventory", "value": "inventory"}]

        # Prompt untuk pemain
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': message,
                'choices': extended_options
            }
        ]
        answers = prompt(questions)
        clear_console()

        action = answers['action']

        if action == "inventory":
            inventory_menu()
            continue

        for option in options:
            if option['value'] == action:
                if action == "benar":
                    event_func(game_state['nama_karakter'])
                else:
                    game_over_prompt(game_state, load_checkpoint, display_state, fail_func)
                return

def ask_to_continue_game():
    """Menanyakan apakah pemain ingin melanjutkan permainan"""
    questions = [
        {
            'type': 'confirm',
            'name': 'continue_game',
            'message': 'Ada checkpoint yang ditemukan. Apakah Anda ingin melanjutkan permainan dari checkpoint?',
            'default': True
        }
    ]
    answers = prompt(questions)

    if answers['continue_game']:
        return True
    else:
        return False

def add_item_to_inventory(items):
    """Menambahkan beberapa item ke inventory dengan konfirmasi pemain menggunakan list."""
    inventory = load_inventory()
    
    # Pastikan input selalu berupa list
    if isinstance(items, str):  # Jika hanya satu item sebagai string
        items = [items]
    
    for item in items:
        if item not in inventory:
            questions = [
                {
                    'type': 'list',
                    'name': 'take_item',
                    'message': f"Apakah Anda ingin mengambil {item}?",
                    'choices': [
                        {"name": "Ya", "value": True},
                        {"name": "Tidak", "value": False}
                    ]
                }
            ]
            answers = prompt(questions)
            
            if answers['take_item']:
                inventory.append(item)
                save_inventory(inventory)
                print(f"{item} telah ditambahkan ke inventory Anda.")
            else:
                print(f"{item} tidak diambil.")
        else:
            print(f"{item} sudah ada di inventory Anda.")
    
    # Simpan inventory setelah semua proses selesai
    save_inventory(inventory)

def display_inventory():
    """Menampilkan inventory dalam bentuk tabel."""
    inventory = load_inventory()
    table = PrettyTable()
    table.field_names = ["No.", "Item"]
    
    for idx, item in enumerate(inventory, 1):
        table.add_row([idx, item])
    
    print(table)

def sort_inventory():
    """Mengurutkan inventory berdasarkan abjad."""
    inventory = load_inventory()
    inventory.sort()
    save_inventory(inventory)
    print("Inventory berhasil diurutkan.")

def search_inventory(item_name):
    """Mencari item dalam inventory dan menampilkannya dalam bentuk tabel dengan nomor urut."""
    inventory = load_inventory()

    item_name = item_name.lower()
    found_items = [item for item in inventory if item_name in item.lower()]
    
    clear_console()
    
    if found_items:
        table = PrettyTable()
        table.field_names = ["No", "Item"]
        
        for idx, item in enumerate(found_items, start=1):
            table.add_row([idx, item])
        
        print(f"Hasil pencarian untuk '{item_name}':\n")
        print(table)
    else:
        print(f"Item '{item_name}' tidak ditemukan di inventory.")

def inventory_menu():
    """Menampilkan menu inventory dengan pilihan sorting atau searching."""
    while True:
        print("\n---- INVENTORY ----")
        
        inventory = load_inventory()
        if not inventory:
            print("Inventory kosong.")
        else:
            table = PrettyTable()
            table.field_names = ["No", "Item"]

            table.align["No"] = "c"
            table.align["Item"] = "l"

            for idx, item in enumerate(inventory, 1):
                table.add_row([idx, item])
            
            print(table)

        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'Pilih aksi:',
                'choices': ['Sorting Inventory', 'Mencari Item', 'Kembali ke Permainan']
            }
        ]
        
        answers = prompt(questions)
        action = answers['action'].lower()

        if action == 'sorting inventory':
            sort_inventory()
        elif action == 'mencari item':
            item_name = input("Masukkan nama item yang ingin dicari: ")
            search_inventory(item_name)
        elif action == 'kembali ke permainan':
            clear_console()
            return
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def show_player_choices(nama_karakter, message, options, event_mapping, add_inventory_option=True):
    """Menampilkan pilihan aksi setelah narasi selesai dengan opsi dinamis."""
    if add_inventory_option:
        options.append({"name": "Lihat Inventory", "value": "inventory"})
    
    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': message,
            'choices': options
        }
    ]
    
    answers = prompt(questions)
    clear_console()

    if answers['action'] == 'inventory':
        inventory_menu()
        clear_console()
        show_player_choices(nama_karakter, message, options, event_mapping, add_inventory_option=False)
    else:
        action = answers['action']
        
        if action in event_mapping:
            event_mapping[action](nama_karakter)
        else:
            print("Pilihan tidak valid.")

