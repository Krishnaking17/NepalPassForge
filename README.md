# NepalPassForge 🇳🇵

NepalPassForge is a culturally intelligent password profiling engine tailored for Nepal. It generates massive wordlists using real Nepali names, cities, districts, castes, festivals, and mutation logic.

## Features
- GUI interface for easy generation
- Mutation engine (leetspeak, symbols, capitalization)
- Output up to 10 million entries
- Ready for use with Hydra, Hashcat, Aircrack-ng

## Installation
```bash
git clone https://github.com/Krishnaking17/NepalPassForge.git
cd NepalPassForge/data
pip install -r requirements.txt
python src/gui.py
