class TestFixture():
    """
    A test fixture represents the preparation needed to perform one or
    more tests, and any associated cleanup actions. This may involve,
    for example, creating temporary or proxy databases, directories, or
    starting a server process.
    """

    def __init__(self):
        self.main_status = False
        self.all_status_codes = []
