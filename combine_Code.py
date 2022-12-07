import json, os

path = 'C:/Users/USER/Desktop/quantigo_Ai/sampleJson'
files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
# print(files)

def merge_json(filename):
    result = list()
    for fl in filename:
        with open(fl,'r') as infile:
            result.append(json.load(infile))

    with open('merged_jsn.png.json', 'w') as output_file:
        json.dump(result, output_file, indent = 4)

merge_json(files)   ##for merging json files##

with open('C:/Users/USER/Desktop/quantigo_Ai/merged_jsn.png.json', 'r') as f:
    data = json.load(f)



for i in range(len(data[0]['objects'])):

    for item in data[i]['objects']:
        item['classTitle'] = item['classTitle'].replace('Vehicle' , 'car')
        item['classTitle'] = item['classTitle'].replace('License Plate' , 'number')
    
with open('merged_replaced.png.json', 'w') as n:
    json.dump(data, n, indent = 4)


    