ids = [
   "b01","b02","b0l","b0r","b5l","cb","c5","b0r","b0l",
    "b5r","b6l","b6r","b7l","b7r","b8l","b8r","b3l","b3r","b1l","b1r","b2l","b2r","r5","l5","c5r","c5l",
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

# 10 Paare pro Zeile
chunk_size = 10
for i in range(0, len(unique_pairs), chunk_size):
    chunk = unique_pairs[i:i+chunk_size]
    line = ", ".join(f'["{a}", "{b}"]' for a, b in chunk)
    print(line + ",")