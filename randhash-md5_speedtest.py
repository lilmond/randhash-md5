import threading
import hashlib
import random
import string
import time

def main():
    try:
        hashes = []

        def _stats_check():
            while True:
                print(f"{len(hashes)} hashes per second.")
                hashes.clear()
                time.sleep(1)

        threading.Thread(target=_stats_check, daemon=True).start()

        while True:
            hashes.append(hashlib.md5("".join(random.choices(string.printable, k=random.randrange(100, 999))).encode()).hexdigest())
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
