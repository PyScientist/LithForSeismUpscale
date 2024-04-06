from matplotlib import pyplot as plt


def find_all_lith(depth_lith_list: list) -> list:
    """
    Get all lithology variations
    :param depth_lith_list: two-dimensional list [['depth', 'lith'],...]
    :return: list of lithology variation
    """
    if (len(depth_lith_list) >= 1) and (len(depth_lith_list[0]) == 2):
        return list(set([unit[1] for unit in depth_lith_list]))
    return []


def find_most_frequent(depth_lith_list: list, lith_variation: list) -> str:
    """
    Function return most frequent lithology
    :param depth_lith_list: two-dimensional list [['depth', 'lith'],...]
    :param lith_variation: list with lithologies variation
    :return: string representation of dominant lith
    """
    all_lith = [item[1] for item in depth_lith_list]
    counts = [all_lith.count(lith) for lith in lith_variation]
    return lith_variation[counts.index(max(counts))]


def convert_lith_char_to_digit(lith_char: str) -> int:
    """
    Convert char to digit
    :param lith_char: lithology in char
    :return: lithology in int
    """
    dict_lith = {
        'f': 1,
        'a': 2,
        'u': 3,
        'y': 4,
    }
    if lith_char in dict_lith.keys():
        return dict_lith[lith_char]
    else:
        return 0


def plot_original_and_upscale(original: list, upscale: list, file_name) -> bool:
    """
    Visualise original and upscale lith
    :param original: original data
    :param upscale: upscale data
    :param file_name: name of file to save figure with visualisation
    :return: state of visualisation
    """
    fig, ax = plt.subplots(1, 2, figsize=(7, 12))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
    ax[0].plot(original[1], original[0], color='black', label='original')
    ax[0].plot(upscale[1], upscale[0], color='red', linestyle='dashed', label='upscale')
    ax[0].set_xlim([0, 5])
    ax[0].legend()
    ax[0].set_title('Original data', color='black')
    ax[1].plot(upscale[1], upscale[0], color='green', linestyle='dashed', label='upscale')
    ax[1].set_xlim([0, 5])
    ax[1].set_title('Upscale data', color='black')
    ax[1].legend()
    plt.savefig(file_name, bbox_inches='tight')
    return True


# Import the data from the file
with open('data.txt', 'r', encoding='utf-8') as f:
    data = [line.replace('\n', '').split('\t') for line in f.readlines()][1:]

# Get all encountered lith types
liths = find_all_lith(data)

scale_of_upscaling = 20

# Perform up-scaling of lithology
new_set = []
for x in range(len(data)):
    if (x > scale_of_upscaling) and (x < len(data)-scale_of_upscaling):
        new_set.append([float(data[x][0]), find_most_frequent(data[x-scale_of_upscaling:x+scale_of_upscaling], liths)])
    else:
        new_set.append([float(data[x][0]), 'Missing'])

# Convert lith to int for visualisation of upscale data
new_set = [[item[0], convert_lith_char_to_digit(item[1])] for item in new_set]
# Convert lith to int for visualisation of original data
init_data = [[float(item[0]), convert_lith_char_to_digit(item[1])] for item in data]

# Show results on graphics save it to particular file
plot_original_and_upscale(list(zip(*init_data)), list(zip(*new_set)), 'result.png')
