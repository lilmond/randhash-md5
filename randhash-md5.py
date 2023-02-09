import hashlib
import random
import string
import time

def main():
        try:
                try:
                        count = int(input("Number to generate: "))
                except ValueError:
                        print("error: must be integer")
                        return

                print("Generating random hash(es)...")
                hashes = []
                start_time = time.time()
                for i in range(count):
                        hashes.append(hashlib.md5("".join(random.choices(string.printable, k=random.randrange(100, 999))).encode()).hexdigest())
                end_time = time.time()

                print("\n\nRandom Hashes:\n")
                [print(hash) for hash in hashes]
                print(f"\n\nTook {(end_time - start_time):.2f} seconds to generate {count} hash(es).")
        except KeyboardInterrupt:
                return

if __name__ == "__main__":
        main()
