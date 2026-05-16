
# https://www.w3schools.com/python/python_json.asp
# https://www.geeksforgeeks.org/read-json-file-using-python/

import json

def ReadJson():
    json_file = open('Material/universities.json')
    
    universities = json.load(json_file)
    
    for uni in universities:
        if 'University of Arizona' in uni['name']:
            for key, value in uni.items():
                print(key, '-', value)

    print('\n----------------------------------------------------\n')

def WriteJson():

    vals = { "name": "John",
             "age": 30,
             "city": "New York" }

    # convert to JSON:
    json_vals = json.dumps(vals)

    # convert to JSON with formats
    json_formatted = json.dumps(vals, indent=4, separators=(". ", " = "))

    print(json_vals)

    print('\n----------------------------------------------------\n')

    print(json_formatted)

    print('\n----------------------------------------------------\n')

    with open('Material/json_output.json', 'w') as outfile:
        json.dump(json_formatted, outfile)

if __name__ == '__main__':
    ReadJson()
    WriteJson()