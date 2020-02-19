# http-server

git clone https://github.com/alvexs/http-server.git
cd http_server
pip3 install -r requirements

### Run server
```
cd server
python3 anagram_server.py
```

### Run tests
```
cd tests
python3 tests.py
```

## Using curl
### To upload dictionary

curl localhost:8080/load -d '["foobar", "aabb", "baba", "boofar", "test"]'

### To check anagrams

curl 'localhost:8080/get?word={word for check}'

curl 'localhost:8080/get?word=foobar' => ["foobar","boofar"]
