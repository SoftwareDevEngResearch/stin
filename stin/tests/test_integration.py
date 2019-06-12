from ..solution import run

def test_run_marker_general_1():
    res = run(0.2)
    for i in range(len(res)):
        assert len(res[i][0]) == len(res[i][1])-1

def test_run_marker_general_2():
    res = run(0.3)
    for i in range(len(res)):
        for j in range(len(res[i][0])):
            assert res[i][0][j] == res[0][0][j]

def test_run_particular():
    res = run(0.4)
    for i in range(len(res)):
        assert res[i][1][len(res[i][1])-1] == i
