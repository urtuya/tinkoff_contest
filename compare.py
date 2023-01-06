import text_parsing

def calc_lev_dist(text1, text2):
    """
    Formula for Levenshtein distance:
    https://en.wikipedia.org/wiki/Levenshtein_distance
    """

    len_t1, len_t2 = len(text1), len(text2)

    if len_t1 > len_t2:                 # to minimize time of calculating
        text1, text2 = text2, text1
        len_t1, len_t2 = len_t2, len_t1

    curr = range(len_t1 + 1)
    for i in range(1, len_t2 + 1):
        prev, curr = curr, [i] + [0]*len_t1
        for j in range(1, len_t1 + 1):
            add, delete = prev[j] + 1, curr[j - 1] + 1
            change = prev[j - 1]
            if text1[j - 1] != text2[i - 1]:
                change = change + 1
            curr[j] = min(add, delete, change)

    return curr[len_t1]

def levenshtein_dist(input_texts):
    """
    This function calculates the Levenshtein distance for each pair of
    files from input. The result is integer minimun number of edits required
    to change one string into the other between every file pair.

    For example:
    string1 = "beat"
    string2 = "beet"
    The levenshtein distance between string1 and string2 is 1.

    return: a list of integers with length equal to the number of file pairs
    """

    dist_results = []

    for pair in input_texts:
        dist_results.append(calc_lev_dist(pair[0], pair[1]))

    return dist_results

def normalized_lev_dist(dist, input_texts):
    """
    This function calculates Levenshtein distance in normalized form
    from 0 to 1 which is equivalent to from 0% to 100%.
    What does it mean:
        0 - no matches between program files or definitely not plagiarism,
        1 - 100% matches or copy-paste.
    """

    normalized_dist = []

    for idx, pair in enumerate(input_texts):
        normalized_dist.append(
            1 - dist[idx] / max(len(pair[0]), len(pair[1]))
            )
    return normalized_dist

def save_result(output_file, path_to_files, dist, save_all=0):
    file = open(output_file, 'w')

    for i, val in enumerate(dist):
        if save_all == 1:
            if i != len(dist) - 1:
                print(path_to_files[i], ":", round(val, 5))
                file.write("{}: {}\n".format(path_to_files[i], round(val, 5)))
            else:
                print(print(path_to_files[i], ":", round(val, 5)), end="")
                file.write(
                    "{}: {}".format(path_to_files[i], round(val, 5))
                    )
        else:
            if i != len(dist) - 1:
                print(round(val, 5))
                file.write("{}\n".format(round(val, 5)))
            else:
                print(round(val, 5), end="")
                file.write("{}".format(round(val, 5)))
    file.close()


if __name__ == '__main__':
    """
    The program is divided into 4 parts:
        1. Initialization of input arguments;
        2. Cleaning the text from file paths in input file
        3. Calculating the Levenshtein distance
        4. Writing and printing results of calculating
    """

    path_to_files, input_files, output_file = text_parsing.parse_arguments()

    input_files = text_parsing.clean_text(input_files)

    lev_dist = levenshtein_dist(input_files)
    norm_dist = normalized_lev_dist(lev_dist, input_files)

    save_result(output_file, path_to_files, norm_dist)