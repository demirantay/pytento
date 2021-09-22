from case import TestCase


class TestFoo(TestCase):

    def test_equal(self):
        a = 1
        b = 1
        return self.assertEqual(a, b)

    def test_not_equal(self):
        a = 1
        b = 2
        return self.assertNotEqual(a, b)


# placeholder runner test
new_test = TestFoo()
print(new_test.test_not_equal())
