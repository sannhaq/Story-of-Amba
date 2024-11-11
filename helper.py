import json
import os
import pygame
import sys
import threading
import time

CHECKPOINT_FILE = 'checkpoint.json' 

def save_checkpoint(state):
    """Menyimpan state permainan ke file checkpoint."""
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
    else:
        print("Tidak ada checkpoint yang ditemukan untuk dihapus.")

def clear_console():
    """Menghapus layar console."""
    os.system('cls' if os.name == 'nt' else 'clear')