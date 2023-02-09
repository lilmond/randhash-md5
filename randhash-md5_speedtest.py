import threading
import hashlib
import random
import string
import time

def main():
    try:
        hashes = []

        def _stats_check():
            min_count = None
            max_count = None

            time.sleep(1)

            while True:
                hashes_count = len(hashes)
                
                if max_count == None or hashes_count > max_count:
                    max_count = hashes_count
                if min_count == None or hashes_count < min_count:
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
