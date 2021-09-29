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

    def test_bar(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)

    def test_for_ayyuce(self):
        name = "ayyuce"
        demirs_name = "ayyuce"
        return self.assertEqual(name, demirs_name)


# Processing and Memory
new_test = TestFoo()
new_test2 = TestBar()

new_runner = TestRunner(new_test, new_test2)

# Output
#print(new_runner.check_fixture_body())


new_runner.test_runner()
print(new_runner.output())
