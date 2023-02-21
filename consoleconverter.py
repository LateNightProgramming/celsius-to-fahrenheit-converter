inputvar = 0
outputvar = 0

def conversion():
    inputvar = int(input('input the temperature in celsius '))
    outputvar = inputvar * 1.8 + 32
    print('temperature in fahrenheit =',outputvar)
    conversion()

conversion()
