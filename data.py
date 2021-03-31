"""
Cleaning the data
"""

import os, json, numpy

DATA_DIR = "./.data/"

def jsonFiles(data_dir):
    json_files = []
    for root, dirs, files in os.walk(data_dir):
        for name in files:
            if name.endswith(".json"):
                json_files.append(os.path.join(root, name))
    return json_files

def getStylesUsed(json_file):
    with open(json_file, 'r') as f:
        data = json.loads(f.read())
        if "styles_used" in data:
            return set(data["styles_used"])
        else:
            return None

def getBooleans(styles_used, all_styles_ordered):
    a = [1 if s in styles_used else 0 for s in all_styles_ordered]
    return a

def getBooleanAttributeRows():
    json_files = jsonFiles(DATA_DIR)
    styles_used = [getStylesUsed(json_file) for json_file in json_files]
    all_styles_set = set()
    [all_styles_set.update(row_styles) for row_styles in styles_used]
    all_styles_ordered = list(all_styles_set)
    all_styles_ordered.sort()
    data_booleans = [getBooleans(row_styles, all_styles_ordered) for row_styles in styles_used]
    return data_booleans, all_styles_ordered

if __name__ == "__main__":
    data = getBooleanAttributeRows()
    print(len(data))
    print(data[0])

