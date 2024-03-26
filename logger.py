import time
import sys

while True:
    time.sleep(2)
    ti = time.time()
    print(f"This is stdout, {ti}", file=sys.stdout)
    print(f"This is stderr, {ti}", file=sys.stderr)
