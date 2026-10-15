import urllib.request
import zipfile
import os
import sys

NODE_URL = "https://nodejs.org/dist/v20.18.0/node-v20.18.0-win-x64.zip"
TARGET_DIR = r"C:\Users\ASUS\nodejs"
ZIP_PATH = r"C:\Users\ASUS\node-dist.zip"

print(f"Downloading Node.js from {NODE_URL}...")
def reporthook(block_num, block_size, total_size):
    if block_num % 500 == 0:
        downloaded = block_num * block_size
        percent = (downloaded / total_size) * 100 if total_size > 0 else 0
        print(f"Downloaded {downloaded // (1024*1024)}MB / {total_size // (1024*1024)}MB ({percent:.1f}%)")

urllib.request.urlretrieve(NODE_URL, ZIP_PATH, reporthook)
print("Download complete. Extracting...")

with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
    zip_ref.extractall(r"C:\Users\ASUS")

extracted_folder = r"C:\Users\ASUS\node-v20.18.0-win-x64"
if os.path.exists(TARGET_DIR):
    import shutil
    shutil.rmtree(TARGET_DIR, ignore_errors=True)

os.rename(extracted_folder, TARGET_DIR)

if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)

print("Node.js successfully installed at:", TARGET_DIR)
