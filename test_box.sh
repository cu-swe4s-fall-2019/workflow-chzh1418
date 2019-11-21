#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_codestyle pycodestyle box.py
assert_no_stdout

run test_codestyle pycodestyle test_box.py
assert_no_stdout

run test_file python box.py --tissue ['Blood'] --genes ['FOXC1'] --out_file 'test1.png'
assert_exit_code 1
rm test1.png
run test_file python box.py --tissue none --genes ['FOXC1'] --out_file 'test2.png'
assert_exit_code 1
rm test2.png

python get_gene_counts.py --count_file GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct.gz --gene_name WASH7P --out_file FOXC1_counts.txt
python get_tissue_samples.py --attribute_file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_group 'Blood' --out_file Blood_samples.txt
python get_gene_counts.py --count_file GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct.gz --gene_name NFATC1 --out_file NFATC1_counts.txt
python get_tissue_samples.py --attribute_file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_group 'Brain' --out_file Brain_samples.txt
run test_single_input  python box.py --tissue Blood Brain --genes FOXC1 NFATC1 --out_file 'test3.png'
assert_exit_code 0
assert_no_stdout
rm test3.png
rm Blood_samples.txt
rm Brain_samples.txt
rm FOXC1_counts.txt
rm NFATC1_counts.txt