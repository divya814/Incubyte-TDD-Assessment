''' String Calulator '''
''' Allow the add method to handle any amount of numbers. '''

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, numbers.split(',')))
