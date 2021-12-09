import json

def get_type(filename:str)->str:
    sub = filename.split('.')[1]
    if sub == 'json':
        return 'json'
    elif sub == 'csv':
        return 'csv'



def decode_json(filename:str)->list:
    """
    :param filename: file name of json
    :return: dataset_list
    The so call json file here is actually a series of json str stores in a single file.
    The attribute inside json can also be a list, label can both be done for tweets
    inside the list and user which is the json object.
    format example:
    -----begin of file-----
    {name: "jsonfile1", attribute1: "aa", attribute2: 11, tweets: [tweet1,tweet2,tweet3,tweet4]}\n
    {name: "jsonfile2", attribute1: "aa", attribute2: 11, tweets: [tweet1,tweet2,tweet3,tweet4]}\n
    {name: "jsonfile3", attribute1: "aa", attribute2: 11, tweets: [tweet1,tweet2,tweet3,tweet4]}\n
    {name: "jsonfile4", attribute1: "aa", attribute2: 11, tweets: [tweet1,tweet2,tweet3,tweet4]}\n
    {name: "jsonfile5", attribute1: "aa", attribute2: 11, tweets: [tweet1,tweet2,tweet3,tweet4]}\n
    .....
    -----end of file-----
    """
    ds = []
    f = open(filename,'r',encoding='utf-8')
    for i in f:
        try:
            u = json.loads(i)
            ds.append(u)
        except BaseException as e:
            print(e)
    return ds
