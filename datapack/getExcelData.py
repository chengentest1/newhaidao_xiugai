import xlrd
import os
import csv
path=os.path.dirname(os.path.dirname(__file__))
loginList=[]
def getData(index):

    wb=xlrd.open_workbook(path+'/data/data_list.xlsx')
    sheet=wb.sheet_by_index(index)
    nrows=sheet.nrows
    for i in range(1,nrows):
        value=sheet.row_values(i)
        loginList.append(value)
    return loginList

if __name__=="__main__":
    t=getData(1)
    print(t)