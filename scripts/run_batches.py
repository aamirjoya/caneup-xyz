import subprocess
import sys
import os

scripts = [
    'scripts/gen_batch1.py',
    'scripts/gen_batch2.py',
    'scripts/gen_batch3.py',
    'scripts/gen_batch4.py'
]

for s in scripts:
    if os.path.exists(s):
        print(f'=== Running {s} ===')
        subprocess.run([sys.executable, s], check=True)
