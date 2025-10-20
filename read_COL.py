import openpyxl

wb = openpyxl.load_workbook('book1.xlsx')

ws = wb.active

for col in ws.iter_cols(min_col=1,max_col=1):
    print(col)
    for data in col:
        print(data.value)


wb.close
