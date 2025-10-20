import openpyxl

wb = openpyxl.load_workbook(filename='book1.xlsx')

ws = wb.active

for CD in ws.iter_rows():
    print(CD)
    for data in CD:
        print(data.value)

wb.close()