# Pytento

Pytento is a lightweight and staticly-typed testing framework written for python. It is not designed or coded to be used for production level projects. I just coded this project in order to understand more about testing in general and packaging python projects. However, still it is a micro-testing framework and it works! So you can use it anywhere if you would like to!

## Installing

Install and update using pip:
```
$ pip install pytento
```

## A Simple Example

```python
# filename.py

from pytento.case import TestCase
from pytento.core import Pytento

class TestFoo(TestCase):

    def test_equality(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)

class TestBar(TestCase):

    def test_unequality(self):
        a = 1
        b = 2
        return self.assertNotEqual(a, b)

new_test = TestFoo()
new_test2 = TestBar()

pytento = Pytento(new_test, new_test2)
pytento.test_runner()
pytento.output()
```
```
$ python filename.py
```

## Links

- Documentation: https://github.com/demirantay/pytento/docs/index.md
- Changes: https://github.com/demirantay/pytento/docs/changes_log.md
- PyPI Releases: https://pypi.org/project/pytento/
- Source Code: https://github.com/demirantay/pytento/
- Issue Tracker: https://github.com/demirantay/pytento/issues/
