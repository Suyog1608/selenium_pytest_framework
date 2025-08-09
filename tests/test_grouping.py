import pytest


class Test_groups:
    def test_tc01(self):
        print("TC01")

    @pytest.mark.skip  #To skip the test cases
    def test_tc02(self):
        print("TCO2")

    def test_tc04(self):
        print("TC04")