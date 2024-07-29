
# Test를 그룹화하면 얻을 수 있는 이점들
# 1. Test organization
# 2. Sharing fixtures for tests only in that particular class
# 3. Applying marks at the class level and having them implicitly apply to all tests



class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
