from fizzbuzz import fizzbuzz

def testfizzbuzz():
    assert fizzbuzz(4) == 4
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(5) =='buzz'
    assert fizzbuzz(15) == 'fizzbuzz'