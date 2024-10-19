''' String Calculator '''
''' Structure reformatting and adding method to check number of calls to add method '''

class StringCalculator:
    def __init__(self):
        self.call_count = 0  # Initialize a counter

    def add(self, numbers: str) -> int:
        self.call_count += 1  # Increment the counter each time add is called

        if not numbers:
            return 0

        # Check for custom delimiter format at the start
        if numbers.startswith('//'):
            delimiter_part, numbers_part = numbers.split('\n', 1)  # Split into delimiter and numbers
            custom_delimiter = delimiter_part[2:]  # Get the custom delimiter from the format //;
            numbers = numbers_part.replace(custom_delimiter, ',')  # Replace the custom delimiter with a comma

        # Replace newlines with commas for standard processing
        numbers = numbers.replace('\n', ',')
        
        # Split the string and filter out any empty strings
        number_list = [int(num) for num in numbers.split(',') if num]

        # Check for negative numbers
        negatives = [num for num in number_list if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

        # Ignore numbers larger than 1000
        number_list = [num for num in number_list if num <= 1000]

        return sum(number_list)

    def get_called_count(self) -> int:
        return self.call_count  # Return how many times add has been called