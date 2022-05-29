# annotate-subject-categories
Adds a categorical column to input file using a user provided category file.

## USAGE
```
python ./categorize.py --datafile <DATAFILE> --categories <CATEGORIES>  --outfile <OUTFILE> 
```
DATAFILE is a csv file with the column headings "percent_terms","terms","negations","subjects", "predicates".  This file was found to be in "utf-8-sig" encoding, so the code specifies that thios coding is expected.

CATEGORIES file is a csv file with no column headings.  The first column value is the category name and all other columns in that row are "subject" values that will be assigned to that category.  There is currently no check to determine if the same subject is assigned to more than one category.

OUTFILE is the name of the output file where results will be stored.  This file's contents are identical to DATAFILE's except an additional column "subject_categories" is added.  If that subject is assigned to a category, the category value will appear here, otherwise the column will be blank.
