import glob
import pandas as pd

class FASTQDirectorySearch:
    
    def __init__(self, directory):
        self.directory = directory # Location to search for .fastq
        self.report = [] # Report containing .fastq info for directory

    '''
    Recursively finds all files with .fastq within the self.directory.
    RETURN: <list> of .fastq file names
    '''
    def find_all_fastq_files(self):
        pathname = self.directory + "/**/*.fastq"
        files = glob.glob(pathname, recursive=True)
        return files

    '''
    Reports all .fastq files in self.directory and % of sequences over minimum length.
    RETURN: <DataFrame> of .fastq file names & percentages
    '''
    def generate_report(self, min_sequence_length=30):

        fastq_file_list = self.find_all_fastq_files()
        report = {}

        # Calculates % sequences over 30 nucleotides long for each file
        for i, filename in enumerate(fastq_file_list,1):
            fastq_file_metadata = FASTQFileMetadata(filename)
            percent_sequence_length = fastq_file_metadata.percent_sequences_minLength(min_sequence_length)
            report[fastq_file_metadata.filename] = percent_sequence_length

        # Stores report in DataFrame
        report_df = pd.DataFrame.from_dict(report, orient='index', columns=['Percentage Files Over ' + str(min_sequence_length) + ' Nucleotides'])
        report_df.index.name = 'File Name'
        self.report = report_df




class FASTQFileMetadata:
    
    def __init__(self, filename):
        self.filename = filename

    '''
    Calculates % of sequences in file exceeding minimum length
    RETURN: <Float> percentage of sequences over minimum length
    '''
    def percent_sequences_minLength(self, min_sequence_length=30):

        num_sequences = 0
        sequences_over_minLength = 0

        # Count sequences exceeding minimum length
        with open(self.filename) as f:
            for index, line in enumerate(f, 1):
                # If fastq file line is a sequence
                if index%4 == 2:
                    num_sequences += 1
                    # And if the sequence is over the minimum length
                    if len(line) - 1 > min_sequence_length: 
                        #Add to count
                        sequences_over_minLength += 1

        # If no sequences in file, prevent division by 0
        if num_sequences == 0: 
            return 0
        
        # Calculate percentage
        return sequences_over_minLength / num_sequences * 100
