import random
import os

my_absolute_dirpath = os.path.abspath(os.path.dirname('BIOINFORMATICS_CODING_TASK'))

class FASTQ_Entry:
    def __init__(self, identifier, sequence, separator, quality_scores):
        self.id = identifier + "1:N:0:2"
        self.seq = sequence
        self.sep = separator
        self.quality = quality_scores
    def r1(self):
        return self.id + "\n" + self.seq + "\n" + self.sep + "\n" + self.quality + "\n"
    def r2(self):
        return self.r2id + "\n" + self.r2seq + "\n" + self.sep + "\n" + self.r2quality + "\n"
    def add_r2(self, identifier, sequence, separator, quality_scores):
        self.r2id = identifier + "2:N:0:2"
        self.r2seq = sequence
        self.r2quality = quality_scores

with open(my_absolute_dirpath+"/sample_files/fastq/read1/Sample_R1.fastq") as r1:
    lines = r1.readlines()
    id_dict = dict()
    index = 0
    id = ""
    seq = ""
    sep = ""
    quality = ""
    for line in lines:
        if index % 4 == 1:
            seq = line.replace("\n", "")
        elif index % 4 == 2:
            sep = line.replace("\n", "")
        elif index % 4 == 3:
            quality = line.replace("\n", "")
        else:
            if index != 0:
                id_dict[id] = FASTQ_Entry(id, seq, sep, quality)
            id = line.split()[0]
        index = index + 1
    id_dict[id] = FASTQ_Entry(id, seq, sep, quality)

with open(my_absolute_dirpath+"/sample_files/fastq/read2/Sample_R2.fastq") as r2:
    lines = r2.readlines()
    index = 0
    id = ""
    seq = ""
    sep = ""
    quality = ""
    for line in lines:
        if index % 4 == 1:
            seq = line.replace("\n", "")
        elif index % 4 == 2:
            sep = line.replace("\n", "")
        elif index % 4 == 3:
            quality = line.replace("\n", "")
        else:
            if index != 0:
                id_dict[id].add_r2(id, seq, sep, quality)
            id = line.split()[0]
        index = index + 1
    id_dict[id].add_r2(id, seq, sep, quality)

# Generate two new .fastq files (corresponding reads) with 50 randomy sampled entries
def generate_new_r1r2(name, path=""):
    sample_ids = random.sample(id_dict.keys(), 50)
    with open(path + name + "_R1.fastq", "x") as r1:
        for id in sample_ids:
            r1.write(id_dict[id].r1())
    with open(path + name + "_R2.fastq", "x") as r2:
        for id in sample_ids:
            r2.write(id_dict[id].r2())


# Empty Directory
os.mkdir("dir_00")

# Shallow + Single File
os.mkdir("dir_01")
generate_new_r1r2("test", "dir_01/")

# Shallow + Multiple Files
os.mkdir("dir_02")
generate_new_r1r2("test_00", "dir_02/")
generate_new_r1r2("test_01", "dir_02/")
generate_new_r1r2("test_02", "dir_02/")

# Deep + Single File
os.mkdir("dir_03")
os.mkdir("dir_03/dir_00")
generate_new_r1r2("test", "dir_03/dir_00/")

# Deep + Multiple Files
os.mkdir("dir_04")
generate_new_r1r2("test_00", "dir_04/")
generate_new_r1r2("test_01", "dir_04/")
os.mkdir("dir_04/dir_00")
generate_new_r1r2("test_00", "dir_04/dir_00/")
generate_new_r1r2("test_01", "dir_04/dir_00/")
os.mkdir("dir_04/dir_01")
generate_new_r1r2("test_00", "dir_04/dir_01/")
generate_new_r1r2("test_01", "dir_04/dir_01/")