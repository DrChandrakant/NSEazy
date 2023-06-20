import pytest
import os
import pandas as pd
import os.path

def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
