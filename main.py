from pytento.case import TestCase
from pytento.runner import TestRunner

# Input


class TestFoo(TestCase):

    def test_equality(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)


# Processing and Memory
new_test = TestFoo()


new_fixture = TestRunner(new_test)


# Output
print(new_fixture.check_fixture_body())
