import openpyxl

wb = openpyxl.Workbook()

ws = wb.active

ws.append(["Name","Math","Science","Total"])
ws.append(["Anshu",56,78])
ws.append(["Aman",89,65])
ws.append(["Satya",56,89])


fixed_col = 4

for row_f in range(2,5):
    ws.cell(row=row_f,column=fixed_col,value=f'=SUM(b{row_f},C{row_f})')

# auto size in columns So it Cluster with another columns.

for col in ws.columns:
    max_length = max(len(str(cell.value)) if cell.value else 0 for cell in col)
    ws.column_dimensions[col[0].column_letter].width = max_length + 2

wb.save('marks.xlsx')
wb.close()
