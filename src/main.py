# -*- utf_8 -*-
import pandas as pa
import os
import sys

def main():
    print("Hello World.")
    if len(sys.argv) < 1:
        print("Please input a json file.")
        return

    file_name = sys.argv[1]
    df = pa.read_json(file_name)
    
    id = df.at[0, df.columns[0]]
    print(type(id))
    for col in df.columns:
        print(col + ": ", type(df.at[0, col]))
        if type(df.at[0, col]) is list:
            df2 = df[col]
            print(df2)
    
    df2_array = []
    for parent_id, dd in zip(df[df.columns[0]], df2):
        dd = list(map(lambda x: {**x, "parent_id": parent_id}, dd))
        df2_array.extend(dd)
    dfdf = pa.DataFrame(df2_array)
    
    dfdf.to_csv("test_2.csv", index=False)
    df.to_csv("test.csv", index=False)


if __name__ == "__main__":
    main()
