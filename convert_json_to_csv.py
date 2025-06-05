
import json

if __name__ == "__main__":
    with open("input.json", 'r') as f:
        dict_data = json.load(f)
    
    # first_keys = dict_data[0].keys()
    # print(list(first_keys))

    output = ",".join([*dict_data[0]])

    with open("output.csv", 'w') as f:
        f.write("," + output + '\n')
        for i, item in enumerate(dict_data):
            f.write(f"{i + 1},{item['name']},{item['type']}\n")


    





