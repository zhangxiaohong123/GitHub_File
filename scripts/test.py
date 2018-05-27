import pytest,allure

class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,2,3,4,6])
    def test_001(self,a):
        allure.attach('描述', '我是测试步骤002的描述~~~')
        assert a!=2

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤002")
    @pytest.mark.parametrize("b", [5, 4, 6])
    def test_002(self, b):
        allure.attach('描述','我是测试步骤002的描述~~~')
        assert b != 2