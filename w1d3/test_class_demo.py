class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1

#Note that when grouped into a class, tests share class attributes, like value = 0
#Therefore, test_two fails

#We can use pytest -k TestClassDemoInstance -q to test only tests that match the
#TestClassDemoInstance substring