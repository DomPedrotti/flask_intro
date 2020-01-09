def fizzbuzz(start):
    response = ''
    if start % 3 == 0:
        response += 'FIZZ'
    if start % 5 == 0:
        response += 'BUZZ'
    print(start if response == '' else response)
    if start < 100:
        start += 1
        fizzbuzz(start)

fizzbuzz(1)