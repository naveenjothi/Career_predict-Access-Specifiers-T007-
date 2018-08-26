import xlrd
import csv
f=xlrd.open_workbook('students_dataSet.xls')
s=f.sheet_by_name('students_details_guvi')
with open('students_dataSet.csv','w') as csv1:
    fw=csv.writer(csv1,quoting=csv.QUOTE_ALL)
    for row in range(s.nrows):
        fw.writerow(s.row_values(row))
csv1.close()
