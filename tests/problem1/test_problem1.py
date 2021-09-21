import sys
import os
my_absolute_dirpath = os.path.abspath(os.path.dirname('BIOINFORMATICS_CODING_TASK'))
sys.path.insert(1, my_absolute_dirpath + '/src/programs')

from problem1 import FASTQDirectorySearch
from problem1 import FASTQFileMetadata
import pandas as pd

def assert_find_all_fastq_files(directory, true_file_list):
    filelist = FASTQDirectorySearch(directory).find_all_fastq_files()
    assert set(filelist) == set(true_file_list)
    assert len(set(filelist)) == len(filelist)

def test_find_all_fastq_files():
    assert_find_all_fastq_files(my_absolute_dirpath + '/sample_files', [my_absolute_dirpath + '/sample_files/fastq/read1/Sample_R1.fastq', my_absolute_dirpath + '/sample_files/fastq/read2/Sample_R2.fastq'])
    assert_find_all_fastq_files(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_00', [])
    assert_find_all_fastq_files(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_01', [my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_01/test_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_01/test_R2.fastq'])
    assert_find_all_fastq_files(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02', [my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_02_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_02_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_01_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_00_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_01_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_00_R2.fastq'])
    assert_find_all_fastq_files(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_03', [my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_03/dir_00/test_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_03/dir_00/test_R2.fastq'])
    assert_find_all_fastq_files(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04', [my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/test_01_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/test_00_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/test_01_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/test_00_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_00/test_01_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_00/test_00_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_00/test_01_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_00/test_00_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_01/test_01_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_01/test_00_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_01/test_01_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_04/dir_01/test_00_R2.fastq'])

def assert_percent_sequences_minLength(file, true_percentage, min_sequence_length):
    sequence_over_minLength = FASTQFileMetadata(file).percent_sequences_minLength(min_sequence_length)
    assert abs(sequence_over_minLength - true_percentage) <= 0.0001

def test_percent_sequences_minLength():
    file = my_absolute_dirpath + '/sample_files/fastq/read1/Sample_R1.fastq'
    assert_percent_sequences_minLength(file, 80.64243448858834, 30)
    assert_percent_sequences_minLength(file, 73.79543533389688, 60)
    assert_percent_sequences_minLength(file, 45.646661031276416, 100)
    assert_percent_sequences_minLength(file, 24.85207100591716, 150)
    assert_percent_sequences_minLength(file, 99.74640743871514, 0)
    assert_percent_sequences_minLength(file, 0.0, 100000000)

def assert_generate_report(directory, min_sequence_length, true_file_list, true_percents):
    fastq_directory_search = FASTQDirectorySearch(directory)
    fastq_directory_search.generate_report(min_sequence_length)
    report = fastq_directory_search.report
    assert set(report.index.values) == set(true_file_list)
    assert len(set(report.index.values)) == len(report.index.values)
    i=0
    for file, percent in  report.iterrows():
        assert abs(true_percents[i] - percent.values[0]) <= 0.0001
        i+=1

def test_generate_report():
    assert_generate_report(my_absolute_dirpath + '/sample_files', 30, [my_absolute_dirpath + '/sample_files/fastq/read2/Sample_R2.fastq', my_absolute_dirpath + '/sample_files/fastq/read1/Sample_R1.fastq'], [83.60101437024514, 80.64243448858834])
    assert_generate_report(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_00', 30, [], [])
    assert_generate_report(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_01', 60, [my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_01/test_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_01/test_R2.fastq'], [72.0, 78.0])
    assert_generate_report(my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02', 10000, [my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_02_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_02_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_01_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_00_R1.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_01_R2.fastq', my_absolute_dirpath + '/tests/problem1/expanded_fastq/dir_02/test_00_R2.fastq'], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
