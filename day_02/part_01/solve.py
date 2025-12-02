import math

def get_next_power_of_two(number: int) -> int:
    return pow(10, math.ceil(math.log10(number + 1)))

with open('day_02/real-input.txt', 'r') as input:
    sequences = input.read().replace('\n', '').split(',')
    
    invalid_sequences: dict[str, list[str]] = {}
    
    for seq in sequences:
        [min, max] = seq.split('-')
        
        invalid_ids: list[str] = []
        current_number: str = min
        while int(current_number) <= int(max):
            num_digits = len(current_number)
            if num_digits % 2 != 0:
                current_number = str(get_next_power_of_two(int(current_number)))
                continue

            if current_number[:int(num_digits / 2)] == current_number[int(num_digits / 2):]:
                invalid_ids.append(current_number)

            current_number = str(int(current_number) + 1)

        if len(invalid_ids) > 0:
            invalid_sequences[seq] = invalid_ids

    total = 0
    print(invalid_sequences)
    for invalid_sequence in invalid_sequences:
        for invalid_id in invalid_sequences[invalid_sequence]:
            total += int(invalid_id)

    print(total)