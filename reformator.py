"""
Postman Collection reformatter

This script will find all file uploads used in Postman Collections and replace file paths with the contents of the description field when using the delimiters

Usage:
- In Postman, when requests require a file upload, put the contents of the desired path in the description field enclosed within ${ & }$ (eg: ${subfolder/datafile.csv}$)
- Set the desired input file (the collection to be reformatted) and output file (destination file)
- Run:$ python pm-reformator.py inputfilename.json outputfilename.json
(Note if no output file is specificed it will default to 'reformatted_inputfilename.json')
"""
import json
import sys

try:
    input_file = open(sys.argv[1], "r+")
    jdata = json.loads(input_file.read())
    delimiters = ["${", "}$"]

except IndexError:
    print("Run in the following format: python reformator.py inputfilename.json [outputfilename.json]")


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


def format_export(jdata, delimiters):
    new_file_data = jdata
    for _ in item_generator(jdata, "formdata"):
        try:
            data = dict(_[0])
            if (
                data["description"][0:2] == delimiters[0]
                and data["description"][-2:] == delimiters[1]
            ):
                file_path = data["description"][2:-2]
                data.update(src = file_path)
        except (IndexError, KeyError):
            # Index/Key error depending on whether it was a list or a dict
            pass
    return(new_file_data)


def write_to_file(formatted_data):
    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        output_file = "reformatted_" + str(sys.argv[1])

    with open(output_file, "w") as outfile:
        json.dump(formatted_data, outfile)
    print("Written new data to " + output_file)


if __name__ == "__main__":
    formatted_data = format_export(jdata, delimiters)
    write_to_file(formatted_data)
