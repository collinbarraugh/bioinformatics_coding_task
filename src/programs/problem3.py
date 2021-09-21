import pandas as pd

class GenomeRangeAnnotations():

    def __init__(self, annotations):
        self.annotations = annotations # .gtf file name
        self.annotations_sorted = pd.DataFrame()

    '''
    Populates self.annotations_sorted with sorted annotations from self.annotations.
    haplotype = False (primary assembly annotations) OR True (haplotype annotations)
    '''
    def sort_gtf(self, haplotype=False):

        #read in gene annotations
        df = pd.read_csv(self.annotations, delimiter='\t|;', header=None)

        # Delete unecessary columns. Name columns properly. 
        df.drop(columns=[5, 7, 13], inplace=True)
        df.columns = ['seqname', 'source', 'splicing', 'start', 'end', 'strand', 'gene_id', 'transcript_id', 'exon_number', 'exon_id', 'gene_name']
        
        # Sort by reduced chromosome # and sequence start. 
        # Provides option to choose haplotype over primary assembly annotations
        df['Chromosome'] = df['seqname'].apply(lambda x: x.split('_')[0]) 
        if haplotype:
            df.sort_values(by=['Chromosome', 'start'], axis=0, inplace=True) # haplotype
        else:
            df.sort_values(by=['seqname', 'start'], axis=0, inplace=True) # primary assembly

        df.set_index(keys=['Chromosome'], drop=False, inplace=True)
        self.annotations_sorted = df



class GenomeCoordinates():

    def __init__(self, coords):
        self.coords = pd.read_csv(coords, sep='\t') # .tsv file of unannotated coordinates
        
    '''
    Adds annotations (from gtf_sorted) to unannotated genomic coordinates (self.coords).
    gtf_sorted = sorted annotations .gtf file read into DataFrame
    '''
    def add_annotations(self, gtf_sorted):

        self.coords['original index'] = self.coords.index #keep the original ordering of the tsv file

        annotations_pre_chromosome = []
        result = []

        for chromosome in self.coords['Chromosome'].unique():

            # Read in sorted gtf file with annotations for single chromosome
            gtf_chrom_df = gtf_sorted[gtf_sorted['Chromosome']==chromosome]
            gtf_chrom = gtf_chrom_df.values.tolist()


            # Read in tsv for single chromosome and sort by position
            tsv_chrom_df = self.coords[self.coords['Chromosome']==chromosome]
            tsv_chrom_df.sort_values(by=['Position'], axis=0, inplace=True)
            tsv_chrom = tsv_chrom_df.values.tolist()

            
            i = 0 # Points to .gtf annotations

            # Parse the tsv coordinates for single chromosome
            for row in range(len(tsv_chrom)):

                # Get position we want to annotate
                position = tsv_chrom[row][1]
                searching = True

                # Parse gtf annotations
                while i < len(gtf_chrom) and searching:

                    # Check if coordinate is in annotations range
                    more_than_start = (position > int(gtf_chrom[i][3]))
                    more_than_end = (position > int(gtf_chrom[i][4]))

                    # In range -> add annotation
                    if  more_than_start and not more_than_end:

                        searching = False
                        result.append(tsv_chrom[row] + gtf_chrom[i])

                    # Out of range -> look at next annotation range
                    elif more_than_end:

                        i = i+1

                    # No annotation exists -> empty string
                    else: 

                        result.append(tsv_chrom[row] + ([''] * len(gtf_chrom[i])))
                        searching = False

                if i >= len(gtf_chrom):
                    result.append(tsv_chrom[row] + ([''] * 12))

        # Clean annotated coordinate DataFrame. Restore original ordering.
        results_df = pd.DataFrame(result, columns = ['Chromosome', 'Position', 'original index', 'seqname', 'source', 'splicing', 'start', 'end', 'strand', 'gene_id', 'transcript_id', 'exon_number', 'exon_id', 'gene_name', 'Chromosome2'])
        results_df.sort_values(by='original index', axis=0, inplace=True)
        results_df.set_index(keys='original index', drop=True, inplace=True)
        results_df.drop(columns=['seqname', 'Chromosome2'], inplace=True)
        results_df.reset_index(drop=True, inplace=True)
        results_df.to_csv('annotated_coordinates.tsv', sep='\t')
        self.coords = results_df



