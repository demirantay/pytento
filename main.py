from pytento.case import TestCase
from pytento.runner import TestRunner

# Input
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

    def tes_bar(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)


class TestBaz(TestCase):

    def test_baz(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)


    def test_this_will_come_wrong(self):
        a = 1
        b = 2
        return self.assertEqual(a, b)


# Processing and Memory
new_test = TestFoo()
new_test2 = TestBar()
new_test3 = TestBaz()

new_runner = TestRunner(new_test, new_test2, new_test3)

# Output
print(new_runner.check_fixture_body())
new_runner.test_runner()


# Test
getattr(new_runner, "test")() #call
