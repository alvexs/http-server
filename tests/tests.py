import unittest
import requests
import json

data = '["foobar", "aabb", "baba", "boofar", "test"]'
requests.post('http://localhost:8080/load', data=data)


class AnagramTestCase(unittest.TestCase):
    def test_get_foobar(self):
        r = requests.get('http://localhost:8080/get?word=foobar')
        resp = r.content.decode()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.dumps(['foobar','boofar']), resp)


    def test_get_raboof(self):
        r = requests.get('http://localhost:8080/get?word=raboof')
        resp = r.content.decode()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.dumps(['foobar','boofar']), resp)


    def test_get_abba(self):
        r = requests.get('http://localhost:8080/get?word=abba')
        resp = r.content.decode()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.dumps(["aabb","baba"]), resp)


    def test_get_upper(self):
        r = requests.get('http://localhost:8080/get?word=FOOBAR')
        resp = r.content.decode()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.dumps(['foobar','boofar']), resp)


    def test_get_wrong(self):
        r = requests.get('http://localhost:8080/get?word=aba')
        resp = r.content.decode()
        self.assertEqual(r.status_code, 200)
        self.assertEqual('null', resp)


if __name__ == '__main__':
    unittest.main()
