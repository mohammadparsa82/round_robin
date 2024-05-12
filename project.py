
num_items = int(input('Number of items: '))
items = {}

for i in range(num_items):
    value = input (f" number of items{i + 1}: ")
    items[i] = value

for i ,  value in items.items():
    print(f"(p{i + 1},{value})")
        
