# -*- utf_8 -*-
import pandas as pa
import json
import os
import sys

def main():
    if len(sys.argv) < 1:
        print("Please input a json file.")
        return

    file_name = sys.argv[1]
    df = pa.read_json(file_name)

    json_data = json.loads(df.to_json(orient="records"))
    dfdf = pa.json_normalize(json_data, record_path="param", meta="id")
    print(dfdf)
    
    df.to_csv("test.csv", index=False)


if __name__ == "__main__":
    main()
