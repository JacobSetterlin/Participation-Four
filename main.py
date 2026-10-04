numbers_to_add = []

current_numbers = [1,2]

next_number = 0

while next_number <= 4000000:
    if current_numbers[1] % 2 == 0:
        numbers_to_add.append(current_numbers[1])

    next_number = current_numbers[0] + current_numbers[1]

    current_numbers[0] = current_numbers[1]
    current_numbers[1] = next_number