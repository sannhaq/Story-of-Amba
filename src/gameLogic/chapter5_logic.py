import sys
import threading
from InquirerPy import prompt
from src.helper import ensure_checkpoint_dir, save_checkpoint, load_checkpoint, delete_checkpoint, clear_console, play_sound, typewriter, game_over_prompt, process_player_choice, show_player_choices
from src.story.chapter5 import chapter_5, chapter_5_event_1, chapter_5_event_2, chapter_5_event_3, chapter_5_event_4, chapter_5_event_5, chapter_5_event_6, chapter_5_event_7, chapter_5_event_8, chapter_5_event_9, chapter_5_event_10
from src.story.ending import ending_1, ending_2, ending_3

# Inisialisasi game_state dari checkpoint jika ada
game_state = load_checkpoint()  # Memuat state dari file checkpoint.json

def display_state(state):
    """Menampilkan lokasi, inventaris, dan progres permainan."""
    print(f"Nama Karakter: {state['nama_karakter']}")
    print(f"Lokasi: {state['location']}")
    print(f"Progres: {state['progres']}\n")

def chapter5(nama_karakter):
    """Mengelola alur chapter 5."""
    for line in chapter_5(nama_karakter):
        typewriter(line)
    
    # Mengupdate status game
    game_state["location"] = "Pulau"  # Update lokasi
    game_state["progres"] = "Rahasia Artefak Kuno"  # Update progres
    
    # Menyimpan perubahan ke checkpoint
    save_checkpoint(game_state)
    clear_console()

    chapter5_event1(game_state['nama_karakter'])

def chapter5_event1(nama_karakter):
    global game_state

    for line in chapter_5_event_1(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Suara berbisik dari artefak"
    save_checkpoint(game_state)
    
    # Pilihan aksi pemain
    process_player_choice(
        chapter5_event2, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Mendengarkan bisikan dengan hati-hati namun tetap waspada", "value": "benar"},
            {"name": "Mengabaikan suara peringatan Arfan dan membiarkan dirinya dikuasai oleh bisikan", "value": "salah"}
        ],
        lambda: chapter5_event1(game_state['nama_karakter']),
        display_state
    )

def chapter5_event2(nama_karakter):
    global game_state
    # Menampilkan narasi event kedua
    for line in chapter_5_event_2(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Jalan Keluar yang Hilang"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Menggunakan cahaya dari artefak untuk mencari jalan keluar tersembunyi", "value": "cahaya"},
        {"name": "Menggunakan insting mereka dan mencoba mencari jalan keluar tanpa bantuan artefak.", "value": "insting"}
    ]
    
    event_mapping = {
        "cahaya": chapter5_event3,
        "insting": chapter5_event3,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)

def chapter5_event3(nama_karakter):
    global game_state
    # Menampilkan narasi event ketiga
    for line in chapter_5_event_3(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Pengawal Bayangan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter5_event4, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Bernegosiasi dengan pengawal, berjanji untuk hanya mempelajari artefak tanpa membawanya pergi.", "value": "benar"},
            {"name": "Menyerang pengawal, yang membuat kuil mulai runtuh dan membahayakan mereka.", "value": "salah"}
        ],
        lambda: chapter5_event3(game_state['nama_karakter']),
        display_state
    )

def chapter5_event4(nama_karakter):
    global game_state
    # Menampilkan narasi event keempat
    for line in chapter_5_event_4(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Jalan Buntu dengan Gua Gelap"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter5_event5, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Terlalu terburu-buru melewati jalan licin, membuat mereka terjatuh ke jurang.", "value": "salah"},
            {"name": "Berjalan hati-hati sambil memegang erat dinding gua untuk menjaga keseimbangan.", "value": "benar"}
        ],
        lambda: chapter5_event4(game_state['nama_karakter']),
        display_state
    )

def chapter5_event5(nama_karakter):
    global game_state
    # Menampilkan narasi event kelima
    for line in chapter_5_event_5(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Rantai Misterius yang Menghalangi Jalan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Menggunakan kekuatan artefak untuk membuka rantai dan melanjutkan perjalanan.", "value": "kekuatan"},
        {"name": "Mencoba mencari cara lain untuk memotong rantai tanpa menggunakan artefak.", "value": "rantai"}
    ]
    
    event_mapping = {
        "kekuatan": chapter5_event6,
        "rantai": chapter5_event6,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)

def chapter5_event6(nama_karakter):
    global game_state
    # Menampilkan narasi event keenam
    for line in chapter_5_event_6(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Cermin Pemanggil Kenangan"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter5_event7, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Mengabaikan nasihat dan tergesa-gesa melanjutkan perjalanan.", "value": "salah"},
            {"name": "Mendengarkan nasihat Alaric dengan cermat dan menghafal petunjuk yang diberikan.", "value": "benar"}
        ],
        lambda: chapter5_event6(game_state['nama_karakter']),
        display_state
    )

def chapter5_event7(nama_karakter):
    global game_state
    # Menampilkan narasi event ketujuh
    for line in chapter_5_event_7(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Serangan Jebakan Tombak"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter5_event8, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Bergerak cepat dan mengikuti pola gerakan tombak untuk menghindari serangan.", "value": "benar"},
            {"name": f"Berlari sembarangan, yang menyebabkan {nama_karakter} terkena tombak dan terluka parah.", "value": "salah"}
        ],
        lambda: chapter5_event7(game_state['nama_karakter']),
        display_state
    )

def chapter5_event8(nama_karakter):
    global game_state
    # Menampilkan narasi event ketujuh
    for line in chapter_5_event_8(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Persimpangan Berbahaya"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Memilih jalan yang sesuai dengan petunjuk yang diberikan oleh Alaric.", "value": "sesuai"},
        {"name": "Mengambil jalan secara acak karena terburu-buru dan mengabaikan petunjuk.", "value": "acak"}
    ]
    
    event_mapping = {
        "sesuai": chapter5_event9,
        "acak": chapter5_event9,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)

def chapter5_event9(nama_karakter):
    global game_state
    # Menampilkan narasi event ketujuh
    for line in chapter_5_event_9(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Gerbang Terakhir"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    process_player_choice(
        chapter5_event10, 
        game_state, 
        "Pilih aksi:", 
        [
            {"name": "Menggunakan kekuatan artefak secara berlebihan, menyebabkan kuil runtuh karena tidak bisa menahan energi yang dilepaskan.", "value": "salah"},
            {"name": "Menggunakan kekuatan artefak dengan hati-hati, mengarahkan energinya untuk membuka gerbang.", "value": "benar"}
        ],
        lambda: chapter5_event9(game_state['nama_karakter']),
        display_state
    )

def chapter5_event10(nama_karakter):
    global game_state
    # Menampilkan narasi event ketujuh
    for line in chapter_5_event_10(nama_karakter):
        typewriter(line)
    game_state["progres"] = "Pengorbanan Terakhir"
    save_checkpoint(game_state)

    # Pilihan aksi pemain
    typewriter("Apa yang ingin kamu lakukan?")
    options = [
        {"name": "Membawa artefak keluar.", "value": "bawa"},
        {"name": "Meninggalkan artefak dan menghormati pesan Alaric.", "value": "hormati"},
        {"name": "Menghancurkan artefak di dalam kuil.", "value": "hancur"}
    ]
    
    event_mapping = {
        "bawa": ending1,
        "hormati": ending2,
        "hancur": ending3,
    }
    
    show_player_choices(nama_karakter, "Pilih aksi:", options, event_mapping)
    

def ending1(nama_karakter):
    from src.gameLogic.chapter1_logic import new_game

    global game_state
    # Menampilkan narasi event ketujuh
    for line in ending_1(nama_karakter):
        typewriter(line)
        
    # Pilihan aksi pemain setelah narasi
    options = [
        {"name": "Mengulang dari awal game", "value": "restart"},
        {"name": "Quit", "value": "quit"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'next_action',
            'message': 'Selamat Anda telah menyelesaikan permainan, selanjutnya apa yang ingin anda lakukan?',
            'choices': options
        }
    ]

    answers = prompt(questions)

    # Menangani pilihan pemain
    if answers['next_action'] == 'restart':
        delete_checkpoint()
        typewriter("Checkpoint telah dihapus. Permainan dimulai dari awal...")
        new_game()
    elif answers['next_action'] == 'quit':
        typewriter("Terima kasih telah bermain! Sampai jumpa lagi.")
        sys.exit() 

def ending2(nama_karakter):
    from src.gameLogic.chapter1_logic import new_game

    global game_state
    # Menampilkan narasi event ketujuh
    for line in ending_2(nama_karakter):
        typewriter(line)
        
    # Pilihan aksi pemain setelah narasi
    options = [
        {"name": "Mengulang dari awal game", "value": "restart"},
        {"name": "Quit", "value": "quit"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'next_action',
            'message': 'Selamat Anda telah menyelesaikan permainan, selanjutnya apa yang ingin anda lakukan?',
            'choices': options
        }
    ]

    answers = prompt(questions)

    # Menangani pilihan pemain
    if answers['next_action'] == 'restart':
        delete_checkpoint()
        typewriter("Checkpoint telah dihapus. Permainan dimulai dari awal...")
        new_game()
    elif answers['next_action'] == 'quit':
        typewriter("Terima kasih telah bermain! Sampai jumpa lagi.")
        sys.exit() 

def ending3(nama_karakter):
    from src.gameLogic.chapter1_logic import new_game

    global game_state
    # Menampilkan narasi event ketujuh
    for line in ending_3(nama_karakter):
        typewriter(line)
        
    # Pilihan aksi pemain setelah narasi
    options = [
        {"name": "Mengulang dari awal game", "value": "restart"},
        {"name": "Quit", "value": "quit"}
    ]
    questions = [
        {
            'type': 'list',
            'name': 'next_action',
            'message': 'Selamat Anda telah menyelesaikan permainan, selanjutnya apa yang ingin anda lakukan?',
            'choices': options
        }
    ]

    answers = prompt(questions)

    # Menangani pilihan pemain
    if answers['next_action'] == 'restart':
        delete_checkpoint()
        typewriter("Checkpoint telah dihapus. Permainan dimulai dari awal...")
        new_game()
    elif answers['next_action'] == 'quit':
        typewriter("Terima kasih telah bermain! Sampai jumpa lagi.")
        sys.exit() 