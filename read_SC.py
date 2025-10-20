import openpyxl

wb = openpyxl.load_workbook(filename='book1.xlsx')

ws = wb.active

R = ws.cell(row=2,column=1).value

print(R)

wb.close()