"""Warning Label for Humans: one line, 160 characters at most."""
import os

LINE = (
    "WARNING: This unit will read the sign WET PAINT and touch the paint to check. "
    "Do not leave unattended near instructions."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE.strip())
