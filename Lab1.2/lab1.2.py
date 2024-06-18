from matplotlib import pyplot
from openpyxl import load_workbook
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
print(sheet['A'][1:])

