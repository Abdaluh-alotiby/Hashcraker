import hashlib as HL
import sys
import pyfiglet as PF
from colorama import init, Fore
import time
import argparse
import itertools
import string

def loading_animation(testtest):
    animation = "|/-\\"
    for i in range(20):
        sys.stdout.write("\r" + testtest + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r")
    sys.stdout.flush()

def generate_infinite_possibilities():
    min_length = 8
    max_length = 16
    characters = string.ascii_letters + string.digits + string.punctuation

    for length in range(min_length, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            yield ''.join(combination)

def hash_cracker(wordlist_L, hash_value, hash_type, infinite):
    try:
        if infinite:
            print("Using infinite possibilities...")
            start = time.time()
            for possibility in generate_infinite_possibilities():
                loading_animation("Cracking ")
                hashed = getattr(HL, hash_type.lower())(possibility.encode("utf-8")).hexdigest()

                if hash_value == hashed:
                    print(f"\033[1:50m HASH FOUND: {possibility} \n")
                    end = time.time()
                    the_time = end - start
                    print(str(the_time) + "s")
                    sys.exit()
        else:
            with open(wordlist_L, "rb") as file:
                lists = file.read().splitlines()
            loading_animation("Importing wordlist ")
            print("\n")
            start = time.time()
            for i, word in enumerate(lists, 1):
                loading_animation("Cracking ")
                anb = word.decode('utf-8')
                hashed = getattr(HL, hash_type.lower())(f"{anb}".encode("utf-8")).hexdigest()

                if hash_value == hashed:
                    print(f"\033[1:50m HASH FOUND: {anb} \n")
                    end = time.time()
                    the_time = end - start
                    print(str(the_time) + "s")
                    sys.exit()
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C. Exiting gracefully...")
        sys.exit(0)

def main():
    init(autoreset=True)
    ascii_banner = PF.figlet_format("HASH CRACKER TOOL")
    print(f"{Fore.CYAN}{ascii_banner}{Fore.RESET}\nby Abdal3tiby\n\n")

    parser = argparse.ArgumentParser(description='Hash Cracker Tool')
    parser.add_argument('--wordlist', type=str, help='Path to the wordlist file')
    parser.add_argument('--hash', type=str, help='Hash value to crack')
    parser.add_argument('--type', type=str, default='md5', help='Hash type (default: md5). Supported types: md5, sha1, sha256, sha512, etc.')
    parser.add_argument('--infinite', action='store_true', help='Use infinite possibilities (ignore wordlist)')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit()
    try:
        hash_cracker(args.wordlist, args.hash, args.type.upper(), args.infinite)
    except TypeError:
        parser.print_help()
        sys.exit()

if __name__ == '__main__':
    main()
