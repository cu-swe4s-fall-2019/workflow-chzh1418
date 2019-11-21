import gzip
import os
import sys
import argparse


def parse_args():
    # Parse arguments
    parser = argparse.ArgumentParser(
            description='Pass arguments')
    parser.add_argument('--attribute_file',
                        type=str,
                        help='Sample attribute file',
                        required=False)
    parser.add_argument('--tissue_group',
                        type=str,
                        help='A tissue group',
                        required=False)
    parser.add_argument('--out_file',
                        type=str,
                        help='Out file name',
                        required=False)
    return parser.parse_args()


def main():
    # Get arguments from argparser
    args = parse_args()
    tissue_group = args.tissue_group
    attribute_file = args.attribute_file
    out_file = args.out_file
    # check if file exit
    if (not os.path.exists(attribute_file)):
        print('Attribute file not exit')
        sys.exit(1)
    attribute_header = None
    output = open(out_file, 'w')
    attribute_info = None
    for line in open(attribute_file, 'rt'):
        if attribute_header is None:
            attribute_header = line.rstrip().split('\t')
            continue
        attribute_info = line.rstrip().split('\t')
        # Knowing the tissue type if in column 6, idx 5
        # Knowing the sample id is in column 1, idx 0
        if attribute_info[5] == tissue_group:
            output.write(attribute_info[0] + '\n')
    output.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
