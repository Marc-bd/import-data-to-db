import json
import os


def write_json(file, data):

    new_file = open(f"uploads/{file}.json", "x")

    try:
        with open(new_file.name, "w") as json_Data:  # open file with Write
            json.dump(data, json_Data, indent=2)  # overwrite the file

        return file

    except:
        return f"Internal Error"
