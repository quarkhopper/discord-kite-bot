# kitestrings.py
import pathlib
import shutil

DATA_DIR = pathlib.Path("data")
DATA_DIR.mkdir(exist_ok=True)

KITE_MEMORY_PATH = DATA_DIR / "kite_memory.txt"
KITE_MEMORY_BACKUP_PATH = DATA_DIR / "kite_memory.bak"

def process_into_memory(file_bytes: bytes) -> str:
    # TODO: Add actual processing logic here (currently returns original content)
    return file_bytes.decode("utf-8")

def set_memory(file_bytes: bytes):
    # Backup current memory before overwriting
    if KITE_MEMORY_PATH.exists():
        shutil.copy(KITE_MEMORY_PATH, KITE_MEMORY_BACKUP_PATH)

    processed_content = process_into_memory(file_bytes)
    with open(KITE_MEMORY_PATH, "w", encoding="utf-8") as f:
        f.write(processed_content)

def export_memory() -> pathlib.Path:
    return KITE_MEMORY_PATH

def export_backup() -> pathlib.Path:
    return KITE_MEMORY_BACKUP_PATH
