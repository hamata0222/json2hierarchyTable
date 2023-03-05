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
    json_data = json.load(open(file_name))

    # オブジェクトのメンバーをフラット化する。
    slip_head = pa.json_normalize(json_data)
    print(slip_head)

    print('----------------------------------------')

    # 配列型のデータを抽出する。
    slip_detail = pa.json_normalize(json_data, record_path='details', meta='slip_no')
    print(slip_detail )

    print('----------------------------------------')
    # 列を追加する。
    slip_detail = slip_detail.reindex(columns=['slip_no', 'item_cd', 'item_name', 'price', 'count', 'updated_by', 'updated_date'])
    print(slip_detail )

    # CSVファイルに出力する。
    slip_head.to_csv('slip_head', index=False)
    slip_detail.to_csv('slip_detail', index=False)

    # file_name = sys.argv[1]
    # json_data = json.load(open(file_name))

    # slip_head = pa.json_normalize(json_data)
    # slip_detail = pa.json_normalize(json_data, record_path="details", meta="slip_no")

    # print(slip_head)
    # print('----------------------------------------')
    # print(slip_detail)

    # json_data = json.loads(df.to_json(orient="records"))
    # dfdf = pa.json_normalize(json_data, record_path="param", meta="id")
    # print(dfdf)
    
    # df.to_csv("test.csv", index=False)


if __name__ == "__main__":
    main()
