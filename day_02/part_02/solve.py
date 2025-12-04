import math

def get_next_power_of_two(number: int) -> int:
    return pow(10, math.ceil(math.log10(number + 1)))

def is_sequenced(input: str) -> bool:
    # Run from index 0 to half of input length
    input_len = len(input)
    if input_len == 1:
        return False

    pivot = math.ceil(len(input) / 2)

    for sequence_len in range(1, pivot + 1):
        if input_len % sequence_len != 0:
            continue
        
        contains_sequence = True
        sequence = input[0:sequence_len]
        for sequence_idx in range(1, int(input_len / sequence_len)):
            sequence_start = sequence_idx * sequence_len
            sequence_end = sequence_start + sequence_len
            if sequence != input[sequence_start:sequence_end]:
                contains_sequence = False
                break
        
        if contains_sequence:
            return True
        
    return False
                

with open('day_02/real-input.txt', 'r') as input:
    sequences = input.read().replace('\n', '').split(',')
    
    invalid_sequences: dict[str, list[str]] = {}
    
    for seq in sequences:
        [min, max] = seq.split('-')
        
        invalid_ids: list[str] = []
        current_number: str = min
        while int(current_number) <= int(max):
            if is_sequenced(current_number):
                invalid_ids.append(current_number)

            current_number = str(int(current_number) + 1)

        if len(invalid_ids) > 0:
            invalid_sequences[seq] = invalid_ids

    total = 0
    for invalid_sequence in invalid_sequences:
        for invalid_id in invalid_sequences[invalid_sequence]:
            total += int(invalid_id)

    print(total)