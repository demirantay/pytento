# Python Imports
import inspect
from itertools import ifilter

# My own library imports
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

    def __str__(self):
        return "Test Runner for Pytento"

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
        holder_arr = []

        test_case = TestCase()
        test_case_method_list = [attribute for attribute in dir(test_case) if callable(getattr(test_case, attribute)) and attribute.startswith('__') is False]

        for test in self.inputted_test_cases:
            method_list = [attribute for attribute in dir(test) if callable(getattr(test, attribute)) and attribute.startswith('__') is False]

            for method in method_list[len(test_case_method_list):]:
                holder_arr.append(method)

        # for each method in holder arr check
        # if they start with `test` if it doesnt
        # the check fixture methods returns false and doesnt
        # start the framework remember this is a staticly typed
        # testing framework
        test_fixutre_holder = []
        test_fixture_state = True

        for test in holder_arr:
            if test[:5] == "test_":
                test_fixutre_holder.append(True)
            else:
                test_fixutre_holder.append(False)

        for test_fixture_status in test_fixutre_holder:
            if test_fixture_status == False:
                test_fixture_state = False
            else:
                test_fixture_state = True

        return test_fixture_state

        # THIS CODE ABOVE IS NOT WORKING !!!!!!! RETURNING WRONGLY


    # Test Runner
    # this method contains the algorithms that bascially runs through all of
    # the tests indivudually and returns you a state that shows which one
    # of those tests passed (True) and which one of those failed (False)
    # with their test names written in a key-value pairing
    def test_runner(self):
        test_state = {}

        test_case = TestCase()
        test_case_method_list = [attribute for attribute in dir(test_case) if callable(getattr(test_case, attribute)) and attribute.startswith('__') is False]

        for test in self.inputted_test_cases:
            method_list = [attribute for attribute in dir(test) if callable(getattr(test, attribute)) and attribute.startswith('__') is False]

            for method in method_list[len(test_case_method_list):]:
                result = getattr(test, method)() #call
                test_state[method] = result

        return test_state


    # Test runner outputs the end result and shows which ones passed/failed
    def output(self):
        output_text = """
test0 - ... ok
test1 - ... ok
test2 - ... FAIL

======================================================

FAIL: test0
Test Name: test_to_button

======================================================

FAIL: test0
Test Name: test_to_button
"""
        return output_text

        
