#loads and queries my model with livestream input and returns prediction

import sys, json
import pickle
import numpy as np



#Read data from stdin
def read_in():
    input = sys.argv[1]
    return input

def main():
	filename = 'mindreadingmodel.sav'
	loaded_model = pickle.load(open(filename, 'rb'))
	input = read_in()
	data = json.loads(input) # this is input array
	result = loaded_model.predict(data)


	print(result[0])


# Start process
main()