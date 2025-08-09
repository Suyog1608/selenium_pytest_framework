import pytest


class Test_Vtiger:

    @pytest.mark.order(1)
    def test_tc05(self):
        print("TC05")

    # @pytest.mark.skip(reason="Just testing")
    # def test_tc07(self):
    #     print("TC07")

    @pytest.mark.order(2)
    def test_tc06(self):
        print("TC06")
