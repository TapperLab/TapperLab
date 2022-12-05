import sys
import pickle
sys.path.append(sys.argv[3])
from signal_udfs import unpickle

file_handle = sys.argv[1]
save_handle = sys.argv[2]

extracted_data = unpickle([sys.argv[4]])[0]

for name in extracted_data.keys()

print(dict_keys)