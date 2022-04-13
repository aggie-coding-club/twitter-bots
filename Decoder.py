def get_key(input):
    keys = {}
    start = input.find("[['") + 3;
    if(start == -1):
        raise Exception("could not find [['")
    end = input.find("']]")
    if(end == -1):
        raise Exception("could not find ']]")
    ary = input[start:end];
    i = 0
    while(i < len(ary)):
        key_start = i + 5
        j = key_start;
        code = "";
        while(j < len(ary) and ary[j] != "'"):
            code += ary[j];
            j += 1
        keys[code] = ary[i]
        i = j + 6;
    
    return keys

def decode(input):
    keys = {}
    keys = get_key(input);
    output = ""
    paragraphs = input.split(" ")
    for val in paragraphs:
        if(len(val) != 0 and (val[0] == "0" or val[0] == "1")):
            input = val
            break
    i = 0;
    curr = "";
    while(i < len(input)):
        curr += input[i];
        if(curr in keys.keys()):
            output += keys[curr]
            curr = ""
        i += 1
    if(curr != ""):
        raise Exception("Wasn't able to decode message :(")
    return output