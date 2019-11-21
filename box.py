import sys
import os
import argparse
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(
            description='Pass parameters')
    parser.add_argument('--tissue',
                        type=str,
                        nargs='+',
                        help='Tissue types',
                        required=True)
    parser.add_argument('--genes',
                        type=str,
                        nargs='+',
                        help='Gene names',
                        required=True)
    parser.add_argument('--out_file',
                        type=str,
                        help='out file name',
                        required=True)

    return parser.parse_args()


def box_plot(Array, title, xticks, out_file):
    """ Boxplot of numerical array
    Paratmeters
    --------
    Array, array contains list of numbers
    title, tile of figures
    box_names
    out_file, output file name

    Return
    --------
    boxplot
    """
    if out_file is None:
        print('Not outfile name specified')
        sys.exit(1)
    # Creat a set of subplots
    plt.subplots(len(title), 1, dpi=500)
    # Adding individual subplot, index starts at 1
    for i in range(len(title)):
        plt.subplot(len(title), 1, i+1)
        plt.boxplot(Array)
        plt.title(title[i])
        plt.ylabel('Count')
        plt.xticks(range(1, len(xticks)+1), xticks, rotation='horizontal')
    plt.savefig(out_file, dpi=500)


def main():
    # get parameters
    args = parse_args()
    tissues = args.tissue
    genes = args.genes
    outfile = args.out_file
    # Test input
    if (os.path.exists(outfile)):
        print('Outfile exits')
        sys.exit(1)
    # Decide not to use box_plot function
    else:
        fig, axes = plt.subplots(len(tissues), 1, figsize=(10, 8))
        q = 0
        for i in tissues:
            tissue_sample_id = []
            if (not os.path.exists(i + '_samples.txt')):
                print(i + '_samples.txt file not found')
                sys.exit(1)
            else:
                for line in open(i + '_samples.txt'):
                    tissue_sample_id.append(line.rstrip().split()[0])
            all_gene_counts = []
            for j in genes:
                single_gene_single_tissue = []
                single_gene_counts = []
                single_gene_sample_id = []
                if (not os.path.exists(j + '_counts.txt')):
                    print(j + '_counts.txt file not exit')
                    sys.exit(1)
                else:
                    for line in open(j + '_counts.txt'):
                        single_gene_counts.append(
                            int(line.rstrip().split('\t')[1]))
                        single_gene_sample_id.append(
                            line.rstrip().split('\t')[0])
                for k in tissue_sample_id:
                    for m in range(len(single_gene_sample_id)):
                        if k == single_gene_sample_id[m]:
                            single_gene_single_tissue.append(
                                single_gene_counts[m])
                all_gene_counts.append(single_gene_single_tissue)
            # print(all_gene_counts)
            axes[q].boxplot(all_gene_counts)
            axes[q].set_title(i)
            axes[q].set_ylabel('Count')
            axes[q].set_xticklabels(genes, rotation='horizontal')
            q += 1
        plt.savefig(outfile, bbox_inches='tight', dpi=500)


if __name__ == '__main__':
    main()
