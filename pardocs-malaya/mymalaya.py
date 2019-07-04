from pprint import pprint

import malaya


def main():
    print("Hello Malaya!!  ")
    malaya.print_cache()
    corpus = ["bob", "dude"]
    pprint(malaya.pos.available_deep_model())


if __name__ == "__main__":
    main()