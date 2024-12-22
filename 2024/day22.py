from inputs import input_day22
numbers = [int(row.strip()) for row in input_day22.strip().split("\n")]

def secret_number_sequence(num, iterations):
    banana = []
    for _ in range(iterations):
        num = (num ^ (num * 64)) % 16777216
        num = (num ^ (num // 32)) % 16777216
        num = (num ^ (num * 2048)) % 16777216
        banana.append(num % 10)
    return banana

def sequence_change(input_data):
    return [input_data[i+1] - input_data[i] for i in range(len(input_data) - 1)]

def find_best_sequence(bans, chans):
    sequence_map = {}
    for idx, ch_list in enumerate(chans):
        seen_sequences = set()
        for i in range(len(ch_list) - 4):
            sequence = tuple(ch_list[i:i+4])
            if sequence not in seen_sequences:
                seen_sequences.add(sequence)
                if sequence not in sequence_map:
                    sequence_map[sequence] = 0
                sequence_map[sequence] += bans[idx][i+4]
    max_bananas = max(sequence_map.values())
    return max_bananas

bananas = [secret_number_sequence(n, 2000) for n in numbers]
changes = [sequence_change(banana) for banana in bananas]
max_bananas = find_best_sequence(bananas, changes)
print(max_bananas)
