import json
import hashlib
from csv import writer
from csv import reader

csvfile = 'file.csv'

fileInput = open (csvfile, 'r')

lines = fileInput.readlines()
x= lines[0].split(",")
# print(x)

hashed_list = ["HASH"]

for i in range(1, len(lines)):
    y= lines[i].split(",")
    attribute_pair = y[6].split(";")
    # avalue = attribute_pair.split(":")
    # print(y)
    data = ({
            "format": "CHIP 0007",
            "name": y[3],
            "filename": y[2],
            "description": y[4],
            "minting tool": " ",
            "sensitive_content": False,
            "series_number": y[0],
            "series_total": 420,
            "attributes": [
                {
                "trait_type": "Species",
                "value": "Mouse"
                },
                {
                "trait_type": "Color",
                "value": "Yellow"
                },
                {
                "trait_type": "Friendship",
                "value": 50,
                "min_value": 0,
                "max_value": 255
                }
            ],
            "collection": {
                "name": "Example Pokémon Collection",
                "id": "e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57",
                "attributes": [
                {
                    "type": "description",
                    "value": "Example Pokémon Collection is the best Pokémon collection. Get yours today!"
                },
                {
                    "type": "icon",
                    "value": "https://examplepokemoncollection.com/image/icon.png"
                },
                {
                    "type": "banner",
                    "value": "https://examplepokemoncollection.com/image/banner.png"
                },
                {
                    "type": "twitter",
                    "value": "ExamplePokemonCollection"
                },
                {
                    "type": "website",
                    "value": "https://examplepokemoncollection.com/"
                }
                ]
            },
            "data": {
                "example_data": "VGhpcyBpcyBhbiBleGFtcGxlIG9mIGRhdGEgdGhhdCB5b3UgbWlnaHQgd2FudCB0byBzdG9yZSBpbiB0aGUgZGF0YSBvYmplY3QuIE5GVCBhdHRyaWJ1dGVzIHdoaWNoIGFyZSBub3QgaHVtYW4gcmVhZGFibGUgc2hvdWxkIGJlIHBsYWNlZCB3aXRoaW4gdGhpcyBvYmplY3QsIGFuZCB0aGUgYXR0cmlidXRlcyBhcnJheSB1c2VkIG9ubHkgZm9yIGluZm9ybWF0aW9uIHdoaWNoIGlzIGludGVuZGVkIHRvIGJlIHJlYWQgYnkgdGhlIHVzZXIu"
            }
        })

    out = json.dumps(data, indent= 4)
    jsonoutput = open(str(y[1]) + '.json', "w")
    jsonoutput.write(out)
    jsonoutput.close()

    
    # print(hashed_list)
    sha256_hash = hashlib.sha256()
    
    with open(str(y[1]) + '.json', "rb") as f:
    
        #Read and Update hashstring value
        for byte_lock in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_lock)
            hashed_value = (sha256_hash.hexdigest())
            hashed_list.append(hashed_value)
        f.close()
        

# print(hashed_list)

fileInput.close()


def add_column_in_csv(input_file, output_file, transform_row):
    # """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

add_column_in_csv(csvfile, 'filename.output.csv', lambda row, line_num: row.append(hashed_list[line_num - 1]))

