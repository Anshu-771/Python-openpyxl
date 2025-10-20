import openpyxl

wb = openpyxl.load_workbook(filename='book1.xlsx')

ws = wb.active

for row in ws.iter_rows(min_row=2,max_row=2):    # it will create tuple
    print(row)
    for data in row:
        print(data.value)


wb.close()