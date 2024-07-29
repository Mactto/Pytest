# 클래스를 그룹화할 때 주의해야 할 점은 공유 객체를 사용할 수 있다는 점이다.
# 각 테스트는 격리되어야 한다는 점을 고려하면 객체를 공유하는 것은 치명적일 수 있음.

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1