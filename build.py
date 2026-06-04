import os
import shutil
import platform
import subprocess
from pathlib import Path

# =========================
# CONFIG
# =========================

ENTRY_FILE = "Window.py"

ROOT_DIR = Path(__file__).parent.resolve()

BUILD_DIR = ROOT_DIR / "Build"
LINUX_DIR = BUILD_DIR / "Linux"
WINDOWS_DIR = BUILD_DIR / "Windows"

DIST_DIR = ROOT_DIR / "dist"
BUILD_TEMP_DIR = ROOT_DIR / "build"

APP_NAME = "GeradorConvites"

# =========================
# UTILS
# =========================

def remove_if_exists(path: Path):
    if path.exists():
        print(f"[INFO] Removendo: {path}")
        shutil.rmtree(path)

def clean_pyinstaller():
    remove_if_exists(DIST_DIR)
    remove_if_exists(BUILD_TEMP_DIR)

    spec_file = ROOT_DIR / f"{APP_NAME}.spec"

    if spec_file.exists():
        print(f"[INFO] Removendo: {spec_file}")
        spec_file.unlink()

def prepare_output_dir(target_dir: Path):
    if target_dir.exists():
        print(f"[INFO] Sobrescrevendo diretório existente: {target_dir}")
        shutil.rmtree(target_dir)

    target_dir.mkdir(parents=True, exist_ok=True)

# =========================
# BUILD
# =========================

def build(target_os: str):
    clean_pyinstaller()

    print(f"[INFO] Buildando para: {target_os}")

    cmd = [
        "pyinstaller",
        "--noconfirm",
        "--windowed",
        "--name", APP_NAME,
        ENTRY_FILE
    ]

    subprocess.run(cmd, check=True)

    source = DIST_DIR / APP_NAME

    if target_os == "Linux":
        target = LINUX_DIR
    else:
        target = WINDOWS_DIR

    prepare_output_dir(target)

    print(f"[INFO] Copiando build para: {target}")
    shutil.copytree(source, target / APP_NAME)

    clean_pyinstaller()

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    BUILD_DIR.mkdir(exist_ok=True)

    current = platform.system()

    if current == "Linux":
        build("Linux")

        print("\n[AVISO]")
        print("Build Windows precisa ser feita no Windows")
        print("ou usando Wine/cross-compilation.")

    elif current == "Windows":
        build("Windows")

        print("\n[AVISO]")
        print("Build Linux precisa ser feita no Linux.")

    else:
        print(f"Sistema não suportado: {current}")
