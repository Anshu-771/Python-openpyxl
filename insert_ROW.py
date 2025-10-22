import openpyxl

wb = openpyxl.load_workbook(filename='book1.xlsx')

ws = wb.active

insert_new_row = 9
new_row_data = ['God','1']

ws.insert_rows(insert_new_row)

for col,data in enumerate(new_row_data,start=1):
    ws.cell(row=insert_new_row,column=col,value=data)

wb.save('book1.xlsx')
wb.close()