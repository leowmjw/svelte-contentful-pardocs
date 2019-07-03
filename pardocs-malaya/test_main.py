from pprint import pprint

import simplejson as json
from unittest import TestCase
from main import hello_world
from PyPDF2 import PdfFileReader

class TestHelloWorld(TestCase):
    def test_hello_world(self):
        out = hello_world("bob", 123)
        print(out)
        # msg = '{"message": "Goodbye 123 World!! bob! Sib!!!", "took": 2.3743000000020498e-05}'
        msg = "{'message': 'Goodbye 123 World!! bob! Sib!!!', 'took': 3}"
        data = json.loads(msg)
        print("DATA ==> " + data['message'])
        # self.fail()

    def test_malaya(self):
        pread = PdfFileReader(open("/Users/leow/GOMOD/go-pardocs/splitout/par14sesi1-soalan-BukanLisan-3.pdf",  "rb"))

        print(pread.getNumPages())

        pg1 = pread.getPage(0).extractText()
        # pprint(' '.join(pg1.splitlines()).split())
        pg2 = pread.getPage(1).extractText()
        # pprint(pg2)
        # questionpg = ''.join(pg1.splitlines()).split()
        questionpg = ' '.join(''.join(pg1.splitlines()).split())
        questionpg += ' '.join(''.join(pg2.splitlines()).split())

        # finalpg = questionpg.splitlines()
        # pprint(questionpg.split()[12])

        pprint(questionpg)
        print("\n\n\n")
        print(questionpg)
        # pprint(' '.join(finalpg))
