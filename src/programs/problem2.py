import pandas as pd

class FASTAProcessor():

    def __init__(self, filename):
        self.filename = filename # fasta file to read in

    '''
    Generates DataFrame from self.filename .fasta file.
    RETURN: <DataFrame> .fasta sequence IDs and sequences
    '''
    def read_fasta(self):
        fasta = pd.read_csv(self.filename, sep='\n', header=None)
        df = pd.DataFrame()
        df['sequence_ID'] = fasta.iloc[::2].reset_index().drop(['index'], axis=1)
        df['sequence'] = fasta.iloc[1::2].reset_index().drop(['index'], axis=1)
        return df 
        
    '''
    Aggregates most frequently occuring sequences and # times they appear.
    RETURN: <DataFrame> sequences and # times they occur
    '''
    def top_sequences(self, top_n_sequences=10):

        sequences = self.read_fasta()
        num_unique_sequences = len(pd.unique(sequences['sequence'].values.flatten()))

        # If we ask for more sequences than total # of unique sequences
        if top_n_sequences > num_unique_sequences:
            # Just get all the unique sequences available
            top_n_sequences = num_unique_sequences

        # Get the frequency of each unique sequence
        top_sequences = pd.DataFrame(sequences['sequence'].value_counts())[:top_n_sequences]

        # Store sequence and counts in dataframe
        top_sequences.columns = ['frequency']
        top_sequences.index.name = 'sequence'

        return top_sequences