import openpyxl

wb = openpyxl.load_workbook(filename='book2.xlsx')

ws = wb.active

col_data = ['i am add 1', 'i am add 2']
col_no = 1

for row,data in enumerate(col_data,start=1):
    ws.cell(row=row,column=col_no,value=data)


wb.save('book2.xlsx')
wb.close()