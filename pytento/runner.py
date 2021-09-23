class TestRunner():
    """
    A test runner is a component which orchestrates the execution of tests
    and provides the outcome to the user. The runner may use a graphical
    interface, a textual interface or something else.
    """

    def __init__(self):
        self.status = True
        self.tests_status_list = []

    def check_syntax_is_correct(self, *test_cases):
        is_correct = False
        for case in test_cases:
            print(case)
