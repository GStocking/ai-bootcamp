from excel_reader import read_excel
from json_writer import write_json


excel_file = "info.xlsx"
json_file = "output.json"


data = read_excel(excel_file)
write_json(data, json_file)

print(f"共有{len(data)}条数据")
print(f"已保存 {json_file}")