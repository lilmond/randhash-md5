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

        try:
            count = int(input("Number to generate: "))
        except ValueError:
                print("error: must be integer")
                return

        print("Generating random hash(es)...")
        hashes = []
        start_time = time.time()
        if gen_type == 1:
            for _ in range(count):
                hashes.append(hashlib.md5("".join(random.choices(string.printable, k=20)).encode()).hexdigest())
        elif gen_type == 2:
            for _ in range(count):
                hashes.append(hashlib.md5("".join(random.choices(string.printable, k=random.randrange(100, 999))).encode()).hexdigest())
        elif gen_type == 3:
            for _ in range(count):
                hashes.append(hashlib.md5(base64.b64encode("".join(random.choices(string.printable, k=999)).encode())).hexdigest())
        elif gen_type == 4:
            for _ in range(count):
                hashes.append(hashlib.md5(base64.b64encode("".join(random.choices(string.printable, k=20)).encode())).hexdigest())
        end_time = time.time()

        print("\n\nRandom Hashes:\n")
        [print(hash) for hash in hashes]
        print(f"\n\nTook {(end_time - start_time):.2f} seconds to generate {count} hash(es).")
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
        main()
