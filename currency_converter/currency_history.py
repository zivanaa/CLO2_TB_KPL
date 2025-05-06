import json
import os
import datetime

HISTORY_FILE_PATH = "currency_history.json"

def save_history_to_file(latest_rates):
    """
    Menyimpan data kurs terbaru ke file JSON dengan timestamp sebagai key.
    Tidak menimpa data lama.
    """
    history = {}
    
    # Muat data lama jika ada
    if os.path.exists(HISTORY_FILE_PATH):
        try:
            with open(HISTORY_FILE_PATH, "r") as f:
                history = json.load(f)
        except Exception as e:
            print(f"[ERROR] Gagal memuat riwayat dari file: {e}")

    # Tambahkan entry baru dengan timestamp saat ini
    timestamp = datetime.datetime.now().isoformat(timespec='minutes')
    history[timestamp] = latest_rates

    # Simpan kembali ke file
    try:
        with open(HISTORY_FILE_PATH, "w") as f:
            json.dump(history, f, indent=4)
        print(f"[INFO] Data kurs berhasil disimpan untuk {timestamp}")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan riwayat ke file: {e}")


def load_history_from_file():
    """
    Mengembalikan riwayat historis dari file JSON.
    """
    if os.path.exists(HISTORY_FILE_PATH):
        try:
            with open(HISTORY_FILE_PATH, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Gagal memuat riwayat dari file: {e}")
            return {}
    return {}

