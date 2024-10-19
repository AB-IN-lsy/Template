import random


class DataGenerator:
    def __init__(self):
        self.generated_data = []

    def gen_n(self, min_val, max_val):
        """Generate a single random number within the given range and add it to generated_data."""
        number = random.randint(min_val, max_val)
        self.generated_data.append(number)
        return number

    def gen_n_(self, min_val, max_val):
        """Generate a single random number within the given range without adding it to generated_data."""
        number = random.randint(min_val, max_val)
        return number

    def gen_n_mul(self, num_count, min_val, max_val):
        """Generate multiple random numbers within the given range and add them to generated_data."""
        numbers = [random.randint(min_val, max_val) for _ in range(num_count)]
        self.generated_data.append(numbers)
        return numbers

    def gen_arr(self, length, min_val, max_val):
        """Generate an array of random numbers of a given length within the specified range and add it to generated_data."""
        array = [random.randint(min_val, max_val) for _ in range(length)]
        self.generated_data.append(array)
        return array

    def save_to_file(self, filename):
        """Save the generated data to a file. Each list of numbers is written on a new line."""
        with open(filename, 'w') as file:
            for item in self.generated_data:
                if isinstance(item, list):
                    file.write(' '.join(map(str, item)) + '\n')
                else:
                    file.write(str(item) + '\n')


gen = DataGenerator()

n = gen.gen_n(1, 10)
arr = gen.gen_arr(n, -10000, 10000)
n, m = gen.gen_n_mul(2, 1, 10)

gen.save_to_file('input.txt')
