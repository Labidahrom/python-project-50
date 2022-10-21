import argparse
from gendiff.scripts.make_gendiff import generate_diff

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help="set format of output")
args = parser.parse_args()
if args.format:
    print("set format of output")
file_1 = args.first_file
file_2 = args.second_file


def main():
    generate_diff(file_1, file_2)