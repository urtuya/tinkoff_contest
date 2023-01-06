import argparse
import re
import string

def parse_arguments():
    parser = argparse.ArgumentParser(prog = "compare.py",
                                     description='An anti-plagiarism utility \
                                        that compares two texts of Python \
                                        programs and gives an estimate of \
                                        their similarity.')
    parser.add_argument("input_file",
                        help="- a file contains one or several pairs of paths \
                                to python programs.")
    parser.add_argument("output_file",
                        nargs='?',
                        const=1,
                        type=str,
                        help="- a file contains path to the file for saving \
                            results. Default path: scores.txt .")
    args = parser.parse_args()

    path_to_files = []
    with open(args.input_file) as file:
        lines = file.readlines()
        for line in lines:
            path_to_files.append(line.split())

    input_files = []    # there will be saved all the texts from all the files
    output = "scores.txt" if args.output_file is None else args.output_file
    for pair_path in path_to_files:
        with open(pair_path[0]) as file1,\
             open(pair_path[1]) as file2:
            input_files.append([file1.read(), file2.read()])

    return path_to_files, input_files, output


def delete_spec_char(text):
    text = re.sub('[\f\t\uf101●➔·•]', '', text)  # removing specific chars
    text = re.sub('\n{2,}', '\n', text)     # removing repeating endlines
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\'", "")

    text = re.sub('( +)\n', '', text)       # removing empty strings
    text = re.sub(' {2,}', ' ', text)       # removing repeating spaces

    text = ''.join([char for char in text if char not in string.punctuation])
                        # to make "class._namex_namey" to "classnamexnamey"
    
    text = text.lower()
    return text


def clean_text(input_texts):
    for i in range(len(input_texts)):
        input_texts[i][0] = delete_spec_char(input_texts[i][0])
        input_texts[i][1] = delete_spec_char(input_texts[i][1])

    return input_texts
