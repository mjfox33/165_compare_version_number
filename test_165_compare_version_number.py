from code_165_compare_version_number import Solution

def test_example_1():
    s = Solution()
    v1 = "1.01"
    v2 = "1.001"
    output = 0
    assert s.compareVersion(v1,v2) == output

def test_example_2():
    s = Solution()
    v1 = "1.0"
    v2 = "1.0.0"
    output = 0
    assert s.compareVersion(v1,v2) == output

def test_example_3():
    s = Solution()
    v1 = "0.1"
    v2 = "1.1"
    output = -1
    assert s.compareVersion(v1,v2) == output

# v1 longer and larger
def test_mjf_0():
    s = Solution()
    v1 = "1.0.1"
    v2 = "1.0"
    output = 1
    assert s.compareVersion(v1,v2) == output

#v2 longer and larger
def test_mjf_1():
    s = Solution()
    v1 = "1.0"
    v2 = "1.0.1"
    output = -1
    assert s.compareVersion(v1,v2) == output

# v1 longer and the same
def test_mjf_2():
    s = Solution()
    v1 = "1.0.0"
    v2 = "1.0"
    output = 0
    assert s.compareVersion(v1,v2) == output

def test_mjf_3():
    s = Solution()
    v1 = "2.0"
    v2 = "1.0.0"
    output = 1
    assert s.compareVersion(v1,v2) == output