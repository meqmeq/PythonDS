from timeit import default_timer as timer
import random 

def get_index(l):

    for i in range(100000):
        r = random.randint(0, len(l) - 2)
        l[r]

def del_list(l):

    for i in range(100):
        if i >= len(l) - 10:
            return
        else:
            r = random.randint(0,5)

            del l[0]
    
def get_time(f):
    start = timer()
    f
    end = timer()
    return end - start

def get_item(d):
    
    for i in range(100):
        d[d.get(random.randint(0,100))] = 1

def del_dict(d):
    for i in range(100):
        if i >= len(d):
            return
        else:
            del d[i]

def main():

#Check time of indexing random numbers of random ranges of list
    print("For indexing list: ")
    for i in range(5):
        l = [random.randint(0, 1000) for i in range(random.randint(0, 1000))]
        print(f"List is lenght {len(l)}")
        print(f"Time fo index  is {get_time(get_index(l))}")
    
    print("For get and set item")

    for i in range(5):
        # Let's initialise dictionaries
        dict_len = range(random.randint(0,100))
        keys = [random.randint(0,100) for i in range(len(dict_len))]
        values = [random.randint(0,100) for i in range(len(dict_len))]
        d = dict(zip(keys,values))
        print(f"Dictionary length {len(d)}")
        print(f"Time to get() and set() in a dictionnary: {get_time(get_item(d))}")

    print("List del() time")

    for i in range(5):
        l = [random.randint(0, 1000) for i in range(1000)]
        print(f"List is lenght {len(l)}")
        print(f"Time fo delete is {get_time(del_list(l))}")
    ### Deleting Dictionnaries
    for i in range(5):
        # Let's initialise dictionaries
        dict_len = range(1000)
        keys = [random.randint(0,100) for i in range(len(dict_len))]
        values = [random.randint(0,100) for i in range(len(dict_len))]
        d = dict(zip(keys,values))
        print(f"Dictionary length {len(d)}")
        print(f"Time to del in a dictionnary: {get_time(del_dict(d))}")
main()