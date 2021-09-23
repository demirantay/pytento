import inspect

from case import TestCase


class TestRunner():
    """
    A test runner is a component which orchestrates the execution of tests
     and provides the outcome to the user. The runner may use a graphical
     interface, a textual interface or something else.
    """
    main_status = True
    all_status_codes = []
    inputted_test_cases = []

    def __init__(self, *tests):
        for test in tests:
            self.inputted_test_cases.append(test)

    # Viewing Methods for the class variables
    def get_main_status(self):
        return self.main_status

    def get_all_status_codes(self):
        return self.all_status_codes

    def get_inputted_test_cases(self):
        return self.inputted_test_cases

    # This function checks if all of the tests are written in a correct format
    # if there is something missing it throws an error, since this framework
    # is a strictly typed testing framework
    # Currently it only checks if the functions start with `test`
    def check_fixture_body(self):
        all_body_data = []
        for test in self.inputted_test_cases:
            test_case = TestCase()
            test_case_method_list = [attribute for attribute in dir(test_case) if callable(getattr(test_case, attribute)) and attribute.startswith('__') is False]
            method_list = [attribute for attribute in dir(test) if callable(getattr(test, attribute)) and attribute.startswith('__') is False]

            return len(test_case_method_list)


    def create_test_suite(self):
        pass
