# kitestrings.py
import pathlib

DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)

KITE_MEMORY_PATH = DATA_DIR / "kite_memory.txt"

def process_and_save_attachment(file_bytes: bytes):
    # TODO: Add processing logic here (currently empty)
    processed_text = file_bytes.decode("utf-8")

    with open(KITE_MEMORY_PATH, "w", encoding="utf-8") as f:
        f.write(processed_text)
