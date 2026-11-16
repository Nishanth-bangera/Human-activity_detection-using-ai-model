import numpy as np
from pathlib import Path

# Project root directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Radar BIN file
BIN_FILE = (
    PROJECT_DIR
    / "dataset"
    / "Crawling"
    / "20m_crawling_towards"
    / "80_crawl_towards.bin"
)

print("=" * 50)
print("RADAR BINARY FILE INSPECTION")
print("=" * 50)

if not BIN_FILE.exists():
    print("ERROR: BIN file not found!")
    print(BIN_FILE)
    raise SystemExit

# File size
file_size = BIN_FILE.stat().st_size

print("\n1. FILE INFORMATION")
print("Filename:", BIN_FILE.name)
print("File size:", file_size, "bytes")
print("File size in MB:", round(file_size / (1024 * 1024), 2))

# Read as little-endian signed 16-bit values
data = np.fromfile(BIN_FILE, dtype="<i2")

print("\n2. ADC DATA INFORMATION")
print("Total ADC values:", len(data))
print("Data type:", data.dtype)
print("Minimum value:", data.min())
print("Maximum value:", data.max())
print("Mean value:", round(float(data.mean()), 3))
print("Standard deviation:", round(float(data.std()), 3))

print("\n3. FIRST 20 VALUES")
print(data[:20])

print("\n4. DATA CHECK")
print("All values zero:", np.all(data == 0))
print("Contains non-zero values:", np.any(data != 0))

print("\n" + "=" * 50)
print("INSPECTION COMPLETED")
print("=" * 50)