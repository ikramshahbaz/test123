######################
import xlrd
xls_path = "C:\\Users\\hp\\Desktop\\excel.xls"
empty_dict ={}
sheet = xlrd.open_workbook(xls_path)
new_sheet = sheet.sheet_by_index(0)
for i in range (1,new_sheet.nrows):
    row = new_sheet.row_values(i)
    empty_dict[row[0]]=row[1:new_sheet.ncols]
print(empty_dict)
############################
############################