from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font  # Para formatar celulas
from openpyxl.comments import Comment # Para comentarios
from openpyxl.chart import BarChart, Series, Reference # para graficos
wb = Workbook()

# Ativando biblioteca
ws = wb.active

# formatando tamanho de celula
ws.column_dimensions['A'].width = 20
ws.row_dimensions[1].height = 40

# formatando cor de celula
COR_A1 = ws['A1']
COR_A1.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
COR_B1 = ws['B1']
COR_B1.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
COR_C1 = ws['C1']
COR_C1.fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

# escrevendo na shit principal
ws['A1'] = 'DATA'
ws['b1'] = 'segundo'
ws['C1'] = 'TERCEIRO'

# formatando tabalho de texto
COMENT_A1 = ws.cell(row=1,column=1).font = Font(size = 24 )

# criando comentário em celula
autor = 'eu'
comentario = 'teste'
comment = Comment(comentario,autor,300,200)
COMENT_A1.comment = comment





# Carregando data atual
import datetime
ws['A2'] = datetime.datetime.now()
# Adicionando valores a colunas na última linha trabalhada
ws.append([1, 2, 3])


# criando novo shit
ws1 = wb.create_sheet("DADOS")
ws2 = wb.create_sheet("GRAFICO")
d = ws1.cell(row=2, column=1, value="DADOS")




# montando graficos
rows = [
    ('Número', 'Quant', 'Perc'),
    (2, 10, 30),
    (3, 40, 60),
    (4, 50, 70),
    (5, 20, 10),
    (6, 10, 40),
    (7, 50, 30),
]


for row in rows:
    ws1.append(row)


chart1 = BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "Turmas do EaD"
chart1.y_axis.title = 'Inadimplência'
chart1.x_axis.title = 'Janeiro'


ws1.cell(row=4, column=4, value="JAN")
ws1.cell(row=5, column=4, value="FEV")
ws1.cell(row=6, column=4, value="MAR")
ws1.cell(row=7, column=4, value="ABR")
ws1.cell(row=8, column=4, value="MAI")
ws1.cell(row=9, column=4, value="JUN")


data = Reference(ws1, min_col=2, min_row=3, max_row=9, max_col=3)
cats = Reference(ws1, min_col=4, min_row=4, max_row=9)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
chart1.shape = 4
ws2.add_chart(chart1, "A5")



# Save the file
wb.save("teste.xlsx")
wb.close()