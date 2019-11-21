import gzip
import sys
import os
import argparse


def linear_search(key, D):
    """ Funcion to search key
    Parameters
    -------
    key: item to search
    D: list to search

    Return
    -------
    key index
    """
    hits = -1
    for i in range(len(D)):
        if key == D[i]:
            return i
            hits = 1
    return -1


def binary_search(key, D):
    """ Function to search key
    Parameters
    --------
    Key: item to search
    D: list to search
    Return
    --------
    Found item

    """
    lo = -1
    hi = len(D)
    while (hi - lo > 1):
        mid = (hi + lo)//2
        if key == D[mid][0]:
            return D[mid][1]

        if key < D[mid][0]:
            hi = mid
        else:
            lo = mid
    return -1


def parse_args():
    # Parse arguments
    parser = argparse.ArgumentParser(
            description='Pass paramters')
    parser.add_argument('--count_file',
                        type=str,
                        help='Gene count file',
                        required=True)
    parser.add_argument('--gene_name',
                        type=str,
                        help='Gene name',
                        required=True)
    parser.add_argument('--out_file',
                        type=str,
                        help='Output file name',
                        required=True)
    return parser.parse_args()


def main():
    # get arguments from argparser
    args = parse_args()
    count_file = args.count_file
    gene_name = args.gene_name
    out_file = args.out_file
    # check file exit
    if (not os.path.exists(count_file)):
        print('Count file not exit')
        sys.exit(1)
    version = None
    dim = None
    data_header = None
    gene_counts = None
    output = open(out_file, 'w')
    # Get the data header and counts
    for line in gzip.open(count_file, 'rt'):
        if version is None:
            version = line
            continue
        if dim is None:
            dim = [int(x) for x in line.rstrip().split('\t')]
            continue
        if data_header is None:
            data_header = line.rstrip().split('\t')
            # Get the sample id column by searching for 'description'
            description_idx = linear_search("Description", data_header)
            if description_idx == -1:
                print('Wrong file, not description column')
                sys.exit(1)
            continue
        else:
            gene_counts = line.rstrip().split('\t')
            if gene_counts[description_idx] == gene_name:
                for i in range(description_idx + 1, len(data_header)-1):
                    output.write(data_header[i]+'\t'+gene_counts[i]+'\n')
    output.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
