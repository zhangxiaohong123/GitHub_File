import pytest

class Test_001:
    @pytest.mark.parametrize("a",[1,2,3,4,6])
    def test_abc(self,a):
        assert a!=2