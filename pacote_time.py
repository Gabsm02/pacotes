import time

# sleep - pausa a execução do programa por um determinado tempo
    # print('Inicio')
    # time.sleep(5)
    # print('Fim')
    
Agora = time.localtime() # time.struct_time(tm_year=2024, tm_mon=5, tm_mday=1, tm_hour=16, tm_min=23, tm_sec=20, tm_wday=2, tm_yday=122, tm_isdst=0)

Formatado = time.strftime('%d/%m/%Y %H:%M:%S', Agora) # 01/05/2024 16:23:20

#Ajustadno data
Time_Texto = "21 June, 2024"
time.strptime(Time_Texto, '%d %B, %Y')
