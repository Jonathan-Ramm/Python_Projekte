ids = [
    
]
pairs = []
for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        pairs.append([ids[i], ids[j]])

unique_pairs = set()
for a, b in pairs:
    pair = tuple(sorted([a,b]))
    unique_pairs.add(pair)

unique_pairs = sorted(unique_pairs)

# n Paare pro Zeile
chunk_size = 10
for i in range(0, len(unique_pairs), chunk_size):
    chunk = unique_pairs[i:i+chunk_size]
    line = ", ".join(f'["{a}", "{b}"]' for a, b in chunk)
    print(line + ",")