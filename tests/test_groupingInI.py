import pytest


class Test_groups1:
    @pytest.mark.smoke
    def test_tc08(self):
        print("TC08")

    @pytest.mark.sanity
    def test_tc09(self):
        print("TCO9")

    @pytest.mark.regression
    def test_tc10(self):
        print("TC10")

    @pytest.mark.regression
    def test_tc11(self):
        print("TC11")

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_tc12(self):
        print("TC12")

