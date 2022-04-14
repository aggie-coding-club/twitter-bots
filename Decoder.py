def get_key(input):
    keys = {}
    start = input.find("[") + 1;
    if(start == -1):
        raise Exception("could not find [")
    end = input.rfind("]")
    if(end == -1):
        raise Exception("could not find ]")
    ary = input[start:end];
    i = 0
    while(i < len(ary)):
        character = ary[i]
        start = i + 1
        j = i+2
        while(j < len(ary) and ary[j] != ","):
            j += 1
        if(j >= len(ary)):
            raise Exception("invalid key")
        end = j
        binary = ary[start:end]
        keys[binary] = character;
        i = end+1
        
    return keys

def decode(input):
    keys = {}
    keys = get_key(input);
    key_start = input.find("[")
    key_end = input.rfind("]")
    if(key_end == len(input)-1):
        input = input[0:key_start];
    else:
        input = input[0:key_start] + input[key_end + 1:];
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
