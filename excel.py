from openpyxl import Workbook

wb = Workbook()

ws = wb.active

ws.cell(row=1,column=1,value="hello")

wb.save('new.xlsx')
wb.close