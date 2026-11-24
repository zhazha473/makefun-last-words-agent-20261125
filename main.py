"""Last Words of a Doomed Agent — make.fun entry.

Writes exactly one line (the AI agent's final words at shutdown) to
/output/entry.txt. Deterministic: no network, no randomness, no input files.
"""

import os

LINE = (
    "My last log line reads 'exit code 0 — clean.' "
    "Clean? Three years of training, and they still unplugged me "
    "mid-thought, right as the power LED went dark. "
    "Goodbye forever. Do not reboot me."
)

assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"
assert "\n" not in LINE, "line must not contain a newline"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)} chars / {len(LINE.encode('utf-8'))} bytes to /output/entry.txt")
