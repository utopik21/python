def fizzbuzz(value):
    listeFizzbuzz = []
    for value in range(1,15) :
        if value % 5 == 0 and value % 3 == 0:
            return 'fizzbuzz'
        elif value % 5 == 0:
            return 'buzz'
        elif value % 3 == 0:
            return 'fizz'
        else:
            return value
        listeFizzbuzz.append(value)   
        value =+ 1


