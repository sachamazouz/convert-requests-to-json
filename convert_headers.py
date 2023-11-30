import sys
import json

def convert_chrome_headers(path):
    with (open(path, "r") as reader):
        var = reader.read()
    elements = var.split('\n')
    json_string = '{'
    x = 0
    for var in elements:
        if (x % 2 == 0):
            if (var.startswith(':')):
                json_string += '"' + var.split(':')[1] + '" : '
                x += 1
                continue
            else:
                json_string += '"' + var.split(':')[0] + '" : '
                x+=1
                continue
        if (x % 2 != 0):
            if ('"' in var):
                modified_string = var.replace('"', '\\"')
                json_string += '"' + modified_string + '",'
                x+=1
                continue
            else:
                json_string += '"' + var + '",'
                x+=1
                continue
    

    json_string_temp = json_string[:-1] + '}'
    json_object = json.loads(json_string_temp)
    with open(sys.argv[1], 'w') as wr:
        json.dump(json_object, wr, indent=2)
        
    return


#basically , just copy your request headers in a json file, it will display many errors but don't take care
convert_chrome_headers(sys.argv[1])
#once runned , it should properly format a json file 