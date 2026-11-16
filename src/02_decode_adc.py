
import numpy as np
from pathlib import Path

# Project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Radar recording
BIN_FILE = (
    PROJECT_DIR
    / "dataset"
    / "Crawling"
    / "20m_crawling_towards"
    / "80_crawl_towards.bin"
)

# Radar configuration
NUM_RX = 4
NUM_ADC_SAMPLES = 256
NUM_CHIRPS_PER_FRAME = 128
IQ_COMPONENTS = 2
BYTES_PER_COMPONENT = 2

print("=" * 55)
print("RADAR ADC DATA STRUCTURE VERIFICATION")
print("=" * 55)

if not BIN_FILE.exists():
    print("ERROR: BIN file not found!")
    raise SystemExit

# Read raw binary data
raw_data = np.fromfile(BIN_FILE, dtype="<i2")

# Calculate expected values per chirp
values_per_chirp = (
    NUM_RX
    * NUM_ADC_SAMPLES
    * IQ_COMPONENTS
)

# Calculate expected bytes per chirp
bytes_per_chirp = (
    values_per_chirp
    * BYTES_PER_COMPONENT
)

# Actual file information
file_size = BIN_FILE.stat().st_size

# Calculate possible number of chirps
total_chirps = file_size // bytes_per_chirp

# Calculate possible frames
frames = total_chirps / NUM_CHIRPS_PER_FRAME

print("\n1. RADAR CONFIGURATION")
print("RX Channels:", NUM_RX)
print("ADC Samples:", NUM_ADC_SAMPLES)
print("Chirps per frame:", NUM_CHIRPS_PER_FRAME)
print("I/Q components:", IQ_COMPONENTS)

print("\n2. DATA SIZE CALCULATION")
print("Total bytes:", file_size)
print("Values per chirp:", values_per_chirp)
print("Bytes per chirp:", bytes_per_chirp)
print("Total possible chirps:", total_chirps)
print("Calculated frames:", frames)

print("\n3. DATA VALIDATION")

if file_size % bytes_per_chirp == 0:
    print("Chirp size alignment: VALID")
else:
    print("Chirp size alignment: INVALID")

if total_chirps % NUM_CHIRPS_PER_FRAME == 0:
    print("Frame alignment: VALID")
else:
    print("Frame alignment: INVALID")

print("\n4. RAW DATA CHECK")
print("Total int16 values:", len(raw_data))
print("First 10 values:", raw_data[:10])

print("\n5. IMPORTANT")
print("This verifies a possible data layout.")
print("I/Q ordering and RX lane arrangement")
print("must still be confirmed before reshaping.")

print("\n" + "=" * 55)
print("VERIFICATION COMPLETED")
print("=" * 55)