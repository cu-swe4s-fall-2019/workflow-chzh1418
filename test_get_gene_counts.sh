#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_codestyle pycodestyle test_get_gene_counts.py
assert_no_stdout

run test_codestyle pycodestyle get_gene_counts.py
assert_no_stdout

run test_file python get_gene_counts.py --count_file GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct.gz --gene_name FOXC1 --out_file test1.txt  
assert_exit_code 0
assert_no_stdout
rm test1.txt