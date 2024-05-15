# import xlsxwriter
# import openpyxl

# workbook = xlsxwriter.Workbook("my-excel.xlsx")

# worksheet = workbook.add_worksheet()
# names = ['D','A','E','R','T','W']
# ls = [23,56,78,90,45,67]

# worksheet.write("A1","90")
# worksheet.write("B2","40")
# workbook.close()

import pandas as pd

data = {
    "Name":["Deepu",'Shiv','Arfiya','Chandan','Ansh'],
    "Marks":[23,78,79,46,78]
}

df = pd.DataFrame(data)
df.to_excel("mynewexcel.xlsx",index=False)
