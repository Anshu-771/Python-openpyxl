import openpyxl

wb = openpyxl.load_workbook(filename='book1.xlsx')

ws = wb.active

row_data = ['Anshu-ji', 349043959]
row_no = 10

for col,data in enumerate(row_data,start=1):
    ws.cell(row=row_no,column=col,value=data)


wb.save('book1.xlsx')
wb.close()