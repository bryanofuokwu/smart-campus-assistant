import pandas as pd
import json
import os

def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV file not found: {path}")
    return pd.read_csv(path)

def load_json(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"JSON file not found: {path}")
    with open(path, 'r') as f:
        return json.load(f)

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    # Example usage
    dummy_data = {"message": "hello", "value": 42}
    save_json(dummy_data, "temp.json")
    print("Loaded JSON:", load_json("temp.json"))