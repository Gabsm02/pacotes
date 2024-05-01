import datetime

Dia_Hoje = datetime.datetime.today()  # 2024-05-01 16:23:20.316095


Data = datetime.datetime.today().date()  #2024-05-01

Ano = Data.year  # 2024
Mes = Data.month #5
Dia = Data.day #1

Data_Antiga = datetime.date(2022, 1, 1)  # 2022-01-01

#Calculando datas
Difrenca = Data - Data_Antiga  # 851 days, 0:00:00 

# Formatando datas
Format = Data.strftime('%d/%m/%Y')  # 01/05/2024

#Adicionando dias
Proxima_Semana = Data + datetime.timedelta(days=7)  # 2024-05-08

