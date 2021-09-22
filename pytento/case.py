class TestCase():
    """
     A test case is the individual unit of testing. It checks for a specific
     response to a particular set of inputs. unittest provides a base class,
     TestCase, which may be used to create new test cases.
    """

    def __init__(self):
        pass

    # this methos checks if a and b are equal
    def assertEqual(self, a, b):
        if a == b:
            return True
        else:
            return False

    # this method checks if a and b are not equal
    def assertNotEqual(self, a, b):
        if a != b:
            return True
        else:
            return False

    # checks if x is true
    def assertTrue(self, x):
        if x == True:
            return True
        else:
            return False

    # checks if x is false
    def assertFalse(self, x):
        if x == False:
            return True
        else:
            return False

    # checks if a is b
    def assertIs(self, a, b):
        if a is b:
            return True
        else:
            return False

    # checks if a is not b
    def assertIsNot(self, a, b):
        if a is not b:
            return True
        else:
            return False

    # check if the value is none
    def assertIsNone(self, x):
        if x == None:
            return True
        else:
            return False

    # check if the value is not note
    def assertIsNotNone(self, x):
        if x != None:
            return True
        else:
            return False

    # checks if a is in b
    def assertIsIn(self, a ,b):
        if a in b:
            return True
        else:
            return False
