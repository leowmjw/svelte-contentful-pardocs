from pprint import pprint

import malaya


def test_preprocess():
    content = "abc def hello"
    string_4 = 'aahhh, malasnye nak pegi keje harini #mondayblues'
    preprocessing = malaya.preprocessing.preprocessing()
    pprint(preprocessing.process(string_4))
    # pprint(malaya.preprocessing.get_normalize())
    # tokenizer = malaya.preprocessing.SocialTokenizer().tokenize
    # pprint(tokenizer(string_4))


def main():
    print("Hello Malaya!!  " + malaya.home)
    malaya.print_cache()
    # corpus = ["bob", "dude"]
    # pprint(malaya.pos.available_deep_model())
    test_preprocess()


if __name__ == "__main__":
    main()