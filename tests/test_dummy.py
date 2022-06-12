import unittest
import pytest

class TestSuite1(unittest.TestCase):
    def setUp(self):
        pass

    @pytest.mark.smoke
    def test_1(self):
        self.assertEqual(1, 1)

    @pytest.mark.smoke
    def test_2(self):
        self.assertEqual(1, 1)

    @pytest.mark.regression
    def test_3(self):
        self.assertEqual(1, 1)

    @pytest.mark.regression
    @pytest.mark.functional
    def test_4(self):
        self.assertEqual(1, 1)

    @pytest.mark.regression
    def test_5(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass


class TestSuite2(unittest.TestCase):
    def setUp(self):
        pass

    @pytest.mark.regression
    @pytest.mark.functional
    def test_11(self):
        self.assertEqual(1, 1)

    @pytest.mark.regression
    @pytest.mark.functional
    def test_12(self):
        self.assertEqual(1, 1)

    @pytest.mark.skip
    def test_13(self):
        # under development
        pass

    @pytest.mark.skip
    def test_14(self):
        # under development
        pass

    @pytest.mark.skip
    def test_15(self):
        # under development
        pass

    def tearDown(self):
            pass


if __name__ == '__main__':
    unittest.main()
