#loads and queries my model with livestream input and returns prediction

import sys, json
import pickle

#Read data from stdin
def read_in():
    input = sys.argv[1]
    return input

def main():
    lines = read_in()
    data = json.loads(lines) # this is input array


    total_sum_inArray = 0
    for item in data:
        total_sum_inArray += 1

    #return the sum to the output stream
    print (total_sum_inArray)

# Start process
main()