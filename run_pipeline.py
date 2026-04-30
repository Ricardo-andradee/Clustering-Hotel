#!/usr/bin/env python3
"""Simple reproducible pipeline runner."""

import hashlib
import subprocess
import sys
from pathlib import Path

# Paths and official hash
DATASET_PATH = Path("tables/hotel_bookings_course_release_v1.csv")
OFFICIAL_SHA256 = "7c2ae42a7353905ea136e5c2287f17c92c5435826598bfbb8491c6f0c7b1fc06"
NOTEBOOK_PATH = Path("src/hotel_analysis.ipynb")

def main():
    print("Starting pipeline execution...")

    # 1. Verify Dataset
    if not DATASET_PATH.exists():
        print(f"[ERROR] Dataset not found: {DATASET_PATH}")
        sys.exit(1)

    with open(DATASET_PATH, 'rb') as f:
        computed_hash = hashlib.sha256(f.read()).hexdigest()

    if computed_hash != OFFICIAL_SHA256:
        print("[ERROR] Dataset hash mismatch!")
        sys.exit(1)
    
    print("[OK] Dataset verified.")

    # 2. Run Notebook
    if not NOTEBOOK_PATH.exists():
        print(f"[ERROR] Notebook not found: {NOTEBOOK_PATH}")
        sys.exit(1)

    print("[INFO] Running notebook (this may take a while)...")
    
    # Using sys.executable ensures it uses the active environment's Python
    result = subprocess.run([
        sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", 
        "--execute", "--inplace", str(NOTEBOOK_PATH)
    ])

    if result.returncode == 0:
        print("[OK] Pipeline completed successfully.")
    else:
        print("[ERROR] Notebook execution failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()