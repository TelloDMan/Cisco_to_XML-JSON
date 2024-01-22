import confparser
import json 
import xmltodict 



def create_xml_json(filename):
    #takes the raw input from the router config and converts it into json
    dissector = confparser.Dissector.from_file('ios.yaml')
    string = dissector.parse_file(f'{filename}.txt')

    #saves the json file
    with open(f"{filename}.json","w") as f:
        f.write(str(string))

    #reopens the json file
    with open(f"{filename}.json", "r") as f: 
        json_data = json.load(f) 

    #add a root header to json
    json_data = {"Configuration" : json_data}

    #converts json to XML
    xml_data = xmltodict.unparse(json_data, pretty=True) 

    #writes the contents into it
    with open(f"{filename}.xml", "w") as f: 
        f.write(xml_data) 
