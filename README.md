# Bioinformatics_Coding_Task

  Solutions to the bioinformatics take-home coding task.


  About the author:


  Collin Barraugh


  Ph.D. Candidate | National Renewable Energy Laboratory Biosciences Center


  Colorado School of Mines Advanced Energy Systems AES Doctoral Program


  C: (858) 213 - 4014


  E: collinbarraugh@gmail.com


  LinkedIn: https://www.linkedin.com/in/collin-barraugh-4200b1100

## Install

  To install the dependencies in the .yml file:

  `conda env create`

  `conda activate bioinformatics_task`
  
  `python setup.py develop`

  Or install with pip:

  `pip install --editable=git+https://github.com/collinbarraugh/bioinformatics_coding_task.git`

  If you edit the .yml file with new packages to install, just use:

  `conda env update`

## Testing

  For tests to run you will need to add the `sample_files` directory containing the sample .fasta, .fastq, coordinates to annotate .tsv, and gene annotations .gtf files.

  `/bioinformatics_coding_task/sample_files`

  Then verify your installation is correct by running the entire test suite:

  `pytest -s -v tests/`

  You can also run individual tests for each of the problems:

  Problem 1: `pytest -s -v tests/problem1`

  Problem 2: `pytest -s -v tests/problem2`

  Problem 3: `pytest -s -v tests/problem3`

## Usage

  If you would like to use these programs from the command line, let me know and I will implement.


## Organization

  1. **sample_files**: Not included; you need to add this in order to run tests.
  

  2. **src/programs**: Folder of solutions to the problems.


    - *problem1.py*:


    - *problem2.py*:


    - *problem3.py*:


  3. **tests**: Test solutions to problems, inputs, outputs, and edge cases.


    - *problem1*:


      - *test_problem1.py*: Runs test over additional subdirectories created by *test_case_generator.py*.


      - **expanded_fastq**: Folder populated by *test_case_generator.py* with additional directories over which to perform file search.


    - *problem2*:


      - *test_problem2.py*: Runs test over sample fasta.


    - *problem3*:


      - *test_problem3.py*: Runs test over .tsv of genetic coordinates and .gtf of annotations.


  4. *annotated_coordinates.tsv*: Annotated coordinates answer key created by *problem3.py*


  5. *test_case_generator.py*: Populates new directories with .fastq files created by randomly sampling from the orginal files provided

