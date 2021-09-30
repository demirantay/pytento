# Simple Usage

Create a a new file in your project and test whatever you want!

```python
from pytento.case import TestCase
from pytento.core import Pytento

class TestFoo(TestCase):

    def test_equality(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)

    def test_not_true(self):
        a = 1
        b = 2
        return self.assertNotEqual(a, b)


class TestBar(TestCase):

    def test_bar(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)

    def test_for_ayyuce(self):
        name = "john"
        name2 = "silvia"
        return self.assertEqual(name, name2)

    def test_assert_is(self):
        arr = [1, 2]
        return self.assertIs(arr, arr)


new_test = TestFoo()
new_test2 = TestBar()

pytento = Pytento(new_test, new_test2)
pytento.test_runner()
pytento.output()
```
So now let's see what is happening above. First we import a test case and a pytento class from our newly downloaded `pytento` library.
