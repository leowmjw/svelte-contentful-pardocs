import simplejson as json
from unittest import TestCase
from main import hello_world


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        out = hello_world("bob", 123)
        print(out)
        # msg = '{"message": "Goodbye 123 World!! bob! Sib!!!", "took": 2.3743000000020498e-05}'
        msg = "{'message': 'Goodbye 123 World!! bob! Sib!!!', 'took': 3}"
        data = json.loads(msg)
        print("DATA ==> " + data['message'])
        # self.fail()
