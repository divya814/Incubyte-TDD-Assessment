''' String Calulator '''
''' Allow the add method to Support different delimiters '''

def add(numbers: str) -> int:
    if not numbers:
        return 0

    # Check for custom delimiter format at the start
    if numbers.startswith('//'):
        delimiter_part, numbers_part = numbers.split('\n', 1)  # Split into delimiter and numbers
        custom_delimiter = delimiter_part[2:]  # Get the custom delimiter from the format //;
        numbers = numbers_part.replace(custom_delimiter, ',')  # Replace the custom delimiter with a comma

    # Replaced newlines with commas and split the string by commas
    numbers = numbers.replace('\n', ',')

    # Filtered out any empty strings after the split (to avoid errors for cases like ",,")
    number_list = [int(num) for num in numbers.split(',') if num]

    return sum(number_list)

