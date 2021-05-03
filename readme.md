# Getting start

setting up config files

```sh
cp ember/_settings.py ember/settings.py
```

# Tests

```sh
python -m coverage run manage.py test

python -m coverage report
```

### without coverage

```sh
python manage.py test
```

### test one function

```sh
python manage.py test game.tests.GameTestCase.test_battle
```

### login test by curl

```sh
curl http://127.0.0.1:8000/login/ --data "username={username_string}&password={password_string}"
```
