import openpyxl
from openpyxl.chart import PieChart,Reference

wb = openpyxl.load_workbook(filename='marks.xlsx')

ws = wb.worksheets[0]

pc = PieChart()

ac = Reference(ws,min_col=4,max_col=4,min_row=2,max_row=4)
l = Reference(ws,min_col=1,max_col=1,min_row=2,max_row=4)

pc.add_data(ac,titles_from_data=True)
pc.set_categories(l)

ws.add_chart(pc,'I1')

wb.save('marks.xlsx')
wb.close()


