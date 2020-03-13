# Postman Collection reformatter

This script will find all file uploads used in Postman Collections and replace file paths with the contents of the description field when using the delimiters

## Usage:
- In Postman, when requests require a file upload, put the contents of the desired path in the description field enclosed within ```${ & }$ # eg: ${subfolder/datafile.csv}$```
- Export the Postman Collection 
- Set the desired input file (the collection to be reformatted) and output file (destination file)
- Run: ```$ python pm-reformator.py input/file/path.json outputfilename.json```
(Note if no output file is specificed it will default to 'reformatted_inputfilename.json')


## Running Tests:
```Coming shortly!```