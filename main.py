with open('data.txt', 'r', encoding='utf-8') as f:
    data = [line.replace('\n', '').split('\t') for line in f.readlines()][1:]


def find_all_lith(data):
    return set([unit[1] for unit in data])

def find_most(data, liths):
    print(liths)

liths = find_all_lith(data)

new_set = []
for x in range(len(data)):
    new_set.append([data[x][0], 'Missing'])
    if x > 20 and x < len(data)-20:
        find_most(data[x-20:x+20], liths)

# print(new_set)



