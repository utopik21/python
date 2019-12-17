def test_primary():
    assert prime_factor(0) == []
    assert prime_factor(1) == []
    assert prime_factor(2) == [2]
    assert prime_factor(3) == [3]
    assert prime_factor(4) == [2,2]
    assert prime_factor(5) == [5]


def prime_factor(input):
    if input < 2 :
        return []
    elif input >= 2 :
        factors = []
        if input % 2 == 0 and input != 2:
            factors.extend([2,2])
        else:
            factors.append(input)

        return factors
