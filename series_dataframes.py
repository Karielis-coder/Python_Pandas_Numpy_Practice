from re import purge
import numpy as np
import pandas as pd


psg_players =pd.Series(['Navas','Mbappe','Neymar','Messi'],index=[1,7,5,10])
print(psg_players)

#otra forma de definir una serie es con diccionario

psg_dict = {1:'Navas',7:'Mbapper',5:'Neymar',10:'Messi'}
print(pd.Series(psg_dict))

#podemos acceder a los datos por el indice en este caso no inicia en 0 si no en 1 de navas ya si
print(psg_players[7])
print(psg_players[0:3])
psg_inf={'Jugador':['Navas','Mbappe','Neymar','Messi'],
'Altura': [183.0,170.0,175.0,165.0],
'Goles':[2,125,135,200]}

print(pd.DataFrame(psg_inf, index=[1,7,5,10])) 
df_Players = pd.DataFrame(psg_inf)
print(df_Players.columns)
print(df_Players.index)