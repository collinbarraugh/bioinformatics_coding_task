import sys
import os
my_absolute_dirpath = os.path.abspath(os.path.dirname('BIOINFORMATICS_CODING_TASK'))
sys.path.insert(1, my_absolute_dirpath + '/src/programs')

from problem3 import GenomeCoordinates
from problem3 import GenomeRangeAnnotations
import pandas as pd

def assert_add_annotations(annotations_gtf, coords_tsv, result_tsv):
    genome_range_annotations = GenomeRangeAnnotations(annotations_gtf)
    genome_range_annotations.sort_gtf()
    genome_coordinates = GenomeCoordinates(coords_tsv)
    genome_coordinates.add_annotations(genome_range_annotations.annotations_sorted)
    result_df = pd.read_csv(result_tsv, index_col=0, sep='\t', keep_default_na=False, dtype=str)
    assert genome_coordinates.coords.astype(str).values.tolist() == result_df.astype(str).values.tolist()

def test_add_annotations():
    assert_add_annotations(my_absolute_dirpath + '/sample_files/optional_gtf/gene_annotations.gtf', my_absolute_dirpath + '/sample_files/optional_tsv/coordinates_to_annotate.tsv', my_absolute_dirpath + '/tests/problem3/annotated_coordinates.tsv')
