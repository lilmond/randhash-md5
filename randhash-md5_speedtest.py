import threading
import hashlib
import random
import string
import time

def main():
    try:
        hashes = []

        def _stats_check():
            min_count = 0
            max_count = 0

            time.sleep(1)

            while True:
                hashes_count = len(hashes)
                
                if hashes_count > max_count:
                    max_count = hashes_count
                if hashes_count < min_count or min_count == 0:
                    min_count = hashes_count

                print(f"{hashes_count} hashes per second | MIN: {min_count} / MAX: {max_count}")
                hashes.clear()
                time.sleep(1)

        threading.Thread(target=_stats_check, daemon=True).start()

        while True:
            hashes.append(hashlib.md5("".join(random.choices(string.printable, k=random.randrange(100, 999))).encode()).hexdigest())
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
