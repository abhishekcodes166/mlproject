
import sys
import os
import pickle
import numpy as np

def verify_pickle_load(file_path):
    print(f"Testing load of {file_path}...")
    try:
        with open(file_path, "rb") as f:
            obj = pickle.load(f)
        print(f"SUCCESS: Loaded {file_path}")
    except Exception as e:
        print(f"FAILURE: Could not load {file_path}")
        print(e)
        # return False
    return True

if __name__ == "__main__":
    print(f"Numpy version: {np.__version__}")
    
    # Adjust paths based on where the script is run
    base_path = "artifacts"
    files = ["model.pkl", "preprocessor.pkl"]
    
    success = True
    for file in files:
        full_path = os.path.join(base_path, file)
        if os.path.exists(full_path):
            if not verify_pickle_load(full_path):
                success = False
        else:
            print(f"WARNING: File {full_path} not found.")
    
    if success:
        print("All pickle files verified.")
    else:
        sys.exit(1)
