''' String Calulator '''
''' Allow the add method to handle new lines between numbers (instead of commas). ("1\n2,3" should return 6) '''

def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Replaced newlines with commas and split the string by commas
    numbers = numbers.replace('\n', ',')

    # Filtered out any empty strings after the split (to avoid errors for cases like ",,")
    number_list = [int(num) for num in numbers.split(',') if num]

    return sum(number_list)

