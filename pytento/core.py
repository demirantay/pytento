# Python Imports
import inspect

# My own library imports
from .case import TestCase


class Pytento():
    """
    A test runner is a component which orchestrates the execution of tests
    and provides the outcome to the user. The runner may use a graphical
    interface, a textual interface or something else.
    """
    main_status = True
    test_state = {}
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
            if test_fixture_status == True:
                pass
            else:
                test_fixture_state = False

        return test_fixture_state


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

        self.test_state = test_state

        return test_state


    # Test runner outputs the end result and shows which ones passed/failed
    def output(self):
        # Run the text fixture if it is False do not run the out put just
        # output `did not write tests correctly`
        state = self.check_fixture_body()

        output_text = "\n"

        if state == True:
            # adding the passed tests to output
            i = 0
            for state in self.test_state:
                i += 1

                if self.test_state.get(state) == True:
                    output_text += "test " + str(i) + " - ... ok\n"
                else:
                    output_text += "test " + str(i) + " - ... FAIL\n"

            output_text += "\n===================================================\n"

            # adding the failed tests to outpuit
            for state in self.test_state:
                if self.test_state.get(state) == False:
                    output_text += "\nFAILED test name: " + str(state) + "\n"
                    output_text += "\n===================================================\n"
        else:
            output_text += "User made a syntax-error while creating tests!\n"
            output_text += "Tests must start with 'test_*'\n"

        print(output_text)
