from timeit import default_timer as timer
import random 

def get_index(l):



    for i in range(100000):
        r = random.randint(0, len(l) - 1)
        l[r]
    
def get_time(f):
    start = timer()
    f
    end = timer()
    return end - start

def get_item(d):
    
    for i in range(100000):
        d[d.get(random.randint(0,100))] = 1

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


main()