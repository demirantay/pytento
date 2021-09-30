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
- So now let's see what is happening above. First we import a test case and a pytento class from our newly downloaded `pytento` library.
- Then we created two test case classes that will act as containers to all of our tests.
- Test methods that return a boolean value. ALWAYS remember every test method must start with `test_` or the framework will NOT run! Remember this is a staticly-typed framework.
- Then we create the objs of our newly created test containers.
- After that we create a new `Pytento` objects which will handle everything for us.
- Finally we just run our testing framework with `.test_runner()` and use the `.output()` function to get the output of the tests.
