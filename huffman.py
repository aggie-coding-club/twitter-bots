
class node:
    def __init__(self, frequency, symbol, left = None, right = None):
        self.frequency = frequency;
        self.symbol = symbol;
        self.left = left;
        self.right = right;
        self.code = "";
def get_delim(ary):
    for tup in ary:
        if(tup[0] == "01"):
            return tup[1]
def encode_text(keys, text):
    new_text = ""
    for char in text:
        for key in keys:
            if(key[0] == char):
                new_text += key[1]

    return new_text;

def make_key(ary, delim):
    output = delim;
    for tup in ary:
        if(tup[0] != "01"):
            temp = format(ord(tup[0]),"b")
            print(temp)
            extra = "0" * (8-len(temp));
            temp = extra + temp;
            output += temp + delim + tup[1];
    output += delim;
    return output;
        

def get_codes(rootNode, ary):
    if(rootNode.left == None or rootNode.right == None):
        ary.append([rootNode.symbol,rootNode.code]);
        
    else:
        get_codes(rootNode.left, ary) 
        get_codes(rootNode.right, ary)
 

def insert(list_of_nodes, node):
    i = 0;
    while(i < len(list_of_nodes) and list_of_nodes[i].frequency < node.frequency ):
        i += 1;
    if(i == len(list_of_nodes) -1 and list_of_nodes[i].frequency < node.frequency):
        list_of_nodes.append(node);
    else:
        list_of_nodes.insert(i, node);
    
#Recursive method which assigns all of the left paths with 0s and the right paths
#with 1s, adds the codes as it goes
def encode(rootNode):
    if(rootNode.left == None and rootNode.right == None):
        return rootNode.code;
    rootNode.left.code =  rootNode.code + "0";
    rootNode.right.code = rootNode.code + "1";
    encode(rootNode.left)
    encode(rootNode.right)
def huffman(input):        
    

    frequency_dict = {};
    
    #get all of the characters and their respective frequencies
    
    for char in input:
        if(frequency_dict.get(char)):
            frequency_dict[char] += 1;
        else:
            frequency_dict[char] = 1;

    
    
    #move everything into tuples in a list to make it easier to sort
    list_of_tuples = [];
    for key in frequency_dict.keys():
        list_of_tuples.append((frequency_dict[key], key));

    #sort all of the characters based on frequency
    list_of_tuples = sorted(list_of_tuples);

    #turn all of these values into nodes, and put them into a list
    list_of_nodes = [];
    for tuple in list_of_tuples:
        list_of_nodes.append(node(tuple[0], tuple[1]));
        #print(tuple[0], ":", tuple[1], "    ");

    #construct the binary tree!!!!
    while(len(list_of_nodes) > 1):
        #Find the first smallest node and remove it from the list
        leftNode = list_of_nodes[0];
        list_of_nodes.pop(0);
        
        #Find the next smallest node and remove it from the list
        rightNode = list_of_nodes[0];
        list_of_nodes.pop(0);
        
        #Create the new node with the left node being the smallest node and the
        #right node being the second smallest value. Insert this node into the 
        #correct spot in the list. 
        new_node = node(leftNode.frequency + rightNode.frequency, None,leftNode, rightNode);
        insert(list_of_nodes, new_node);
    #print(len(list_of_nodes));

    papa_node = list_of_nodes[0];
    encode(papa_node);
    ary = [];
    get_codes(papa_node, ary)
    output = encode_text(ary, input)
    return "Key: " + str(ary)[:-1] + " " + output + " Original size was " + str(8 * len(input)) + " bits New size is " + str(len(output)) + " bits";

    

