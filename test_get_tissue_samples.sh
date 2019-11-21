#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_codestyle pycodestyle test_get_tissue_samples.py
assert_no_stdout

run test_codestyle pycodestyle get_tissue_samples.py
assert_no_stdout


run test_file python get_tissue_samples.py --attribute_file GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --tissue_group 'Blood' --out_file test2.txt
assert_exit_code 0
rm test2.txt