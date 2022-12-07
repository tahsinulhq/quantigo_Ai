import json
from pathlib import Path

l =[]

l2 = []
l3 = []
l4 = []
l_lp = []
l_lp2= []

dictionary = {}
dictionary1 = {}
dictionary2 = {}
dictionaryf = {}
dictionary4 = {}
dictionarylp = {}

with open('C:/Users/USER/Desktop/quantigo_Ai/sampleJson/pos_0.png.json', 'r') as f:
    data = json.load(f)
    p = (Path('C:/Users/USER/Desktop/quantigo_Ai/sampleJson/pos_0.png.json').stem)
# print(data)
    # print(data['objects'][0]['tags'][3]['name'])

    for i in range(len(data['objects'][0]['tags'])):
        l.append(data['objects'][0]['tags'][i]['name'])
    
    for i in range(len(data['objects'][0]['tags'])):
        l2.append(data['objects'][0]['tags'][i]['value'])

    # print(l)
    # print(l2)

    dictionary = dict(zip(l, l2))
    # print(dictionary)

    for i in range(len(data['objects'][1]['tags'])):
        l_lp.append(data['objects'][1]['tags'][i]['name'])

    for i in range(len(data['objects'][1]['tags'])):
        l_lp2.append(data['objects'][1]['tags'][i]['value'])

    dictionarylp = dict(zip(l_lp, l_lp2))
    dictionarylp['occlusion'] = data['objects'][1]['tags'][0]['value']
    # print(dictionarylp)
        
    if (data['objects'][0]['classTitle']) == 'Vehicle':
        for i in range(len(data['objects'][0]['points']['exterior'])):    
            l3.append(data['objects'][0]['points']['exterior'][i])
    else:
        l3 == None
        
    if (data['objects'][1]['classTitle']) == 'License Plate':
        for i in range(len(data['objects'][0]['points']['exterior'])): 
            l4.append(data['objects'][1]['points']['exterior'][i])
    else:
        l4 == None
    # print(data['objects'][0]['points']['exterior'][0])
    # print(data['objects'][1]['classTitle'])
    
    fl = sum(l3,[])
    fl2 = sum(l4,[])
    # print(l4)
    
    dictionary1['presence'] = len(data['objects'][0]['points']['exterior'])-1
    
    dictionary1['bbox'] = fl
    dictionary2['presence'] = len(data['objects'][0]['points']['exterior'])-1
    dictionary2['bbox'] = fl2
    # print(dictionary1)
    # print(dictionary2)


    dictionaryf = {
        "dataset_name": p,
        "image_link": "",
        "annotation_type": "image",
        
    }
    dictionaryf['annotation_objects'] = {'Vehicle': dictionary1 , 'license_plate': dictionary2}
    dictionaryf['annotation_attributes'] = {'Vehicle':dictionary, 'license_plate':dictionarylp}

##reformatted json file##
with open('test_formatted_pos_0.png.json', 'w') as json_file:
  json.dump(dictionaryf, json_file, indent= 4)

