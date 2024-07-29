from exceptiongroup import ExceptionGroup
import pytest


# ExceptionGroup
# ExceptionGroup이란 여러 예외들을 하나의 그룹으로 묶어 한번에 처리할 수 있도록 하는 
# python 3.11부터 도입된 문법

def f():
    raise ExceptionGroup(
        "Group message",
        [
            RuntimeError(),
        ],
    )


def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        f()
    assert excinfo.group_contains(RuntimeError)
    assert not excinfo.group_contains(TypeError)