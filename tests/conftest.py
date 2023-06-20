import pytest
import os
import pandas as pd
import os.path

print('oka')
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
