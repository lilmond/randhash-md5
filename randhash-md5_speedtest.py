import threading
import hashlib
import random
import string
import base64
import time

def main():
    try:
        print(f"\nSelect a generator type:\n\n:1 - Easy-Fast\n:2 - Hard-Slow\n:3 - Base64_Enc-Hardest-Slowest\n:4 - Base64_Enc-Easy-Fast\n")
        try:
            gen_types = [1, 2, 3, 4]
            gen_type = int(input("Generator Type: "))
            if not gen_type in gen_types: raise ValueError
        except ValueError:
            print("Error: Invalid generator type.")
            return

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

        if gen_type == 1:
            while True:
                hashes.append(hashlib.md5("".join(random.choices(string.printable, k=20)).encode()).hexdigest())
        elif gen_type == 2:
            while True:
                hashes.append(hashlib.md5("".join(random.choices(string.printable, k=random.randrange(100, 999))).encode()).hexdigest())
        elif gen_type == 3:
            while True:
                hashes.append(hashlib.md5(base64.b64encode("".join(random.choices(string.printable, k=999)).encode())).hexdigest())
        elif gen_type == 4:
            while True:
                hashes.append(hashlib.md5(base64.b64encode("".join(random.choices(string.printable, k=20)).encode())).hexdigest())
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
