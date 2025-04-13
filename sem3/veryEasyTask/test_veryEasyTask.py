import pytest
from veryEasyTask import veryEasyTask  

@pytest.mark.parametrize("N, x, y, expected", [
    (0, 1, 1, 0),     
    (1, 100, 200, 100),
    (1, 200, 100, 100),
    (10, 1, 100, 10),   
    (10, 100, 1, 10),   
    (5, 2, 2, 6),       
    (10, 1, 1, 6),      
    (5, 2, 3, 8),       
    (3, 2, 3, 5),       
    (7, 3, 5, 15),      
    (4, 2, 3, 6),       
    (6, 2, 3, 8),       
    (1000, 1, 1, 501)
])
def test_veryEasyTask(N, x, y, expected):
    assert veryEasyTask(x, y, N) == expected