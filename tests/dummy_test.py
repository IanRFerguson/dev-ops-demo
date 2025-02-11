import unittest

#####


class MyTestCase(unittest.TestCase):
    def test__dummy_v1(self):
        my_var = "foo"

        assert my_var == "foo"

    def test__dummy_v2(self):
        my_var = "foo"

        assert isinstance(my_var, str)
