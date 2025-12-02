import math

def get_next_power_of_two(number: int) -> int:
    return pow(10, math.ceil(math.log10(number + 1)))

def is_sequenced(input: str) -> bool:
    # Register the initial sequence
    initial_sequence: list[str] = []
    
    ptr = 0
    while ptr < len(input):
        if input[ptr] == initial_sequence[0]:
            break

        initial_sequence.append(input[ptr])
        ptr += 1
    
    if len(initial_sequence) == 0 or len(input) % len(initial_sequence) != 0:
        return False
    
    sequences: list[str] = []
    current_sequence: list[str] = []
    while ptr < len(input):
        sequence_position = ptr % len(initial_sequence)        
        if sequence_position == 0 and input[ptr] == initial_sequence[0]:
            sequences.append(''.join(current_sequence))
            current_sequence = []

        if input[ptr] != initial_sequence[sequence_position]:
            return False
        
        current_sequence.append(input[ptr])
        ptr += 1

    sequences.append(''.join(current_sequence))
    print(sequences)
    return True

    

with open('day_02/test-input.txt', 'r') as input:
    sequences = input.read().replace('\n', '').split(',')
    
    invalid_sequences: dict[str, list[str]] = {}
    
    for seq in sequences:
        [min, max] = seq.split('-')
        
        invalid_ids: list[str] = []
        current_number: str = min
        while int(current_number) <= int(max):
            if is_sequenced(current_number):
                current_number = str(int(current_number) + 1)

        if len(invalid_ids) > 0:
            invalid_sequences[seq] = invalid_ids

    total = 0
    print(invalid_sequences)
    for invalid_sequence in invalid_sequences:
        for invalid_id in invalid_sequences[invalid_sequence]:
            total += int(invalid_id)

    print(total)