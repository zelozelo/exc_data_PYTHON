import pickle

modelo = open('modelo_consumo_cerveja','rb')
lm_new = pickle.load(modelo)
modelo.close()

temp_max = 30.5
chuva = 12.2
fds = 0
entrada = [[temp_max, chuva, fds]]

print(f'Temperatura Máxima: {temp_max} ºC')
print(f'Chuva: {chuva} mm ' )
print(f'É Final de Semana: ', ('Não' if fds == 0 else 'Sim'))
print('{0:.2f} litros previstos'.format(lm_new.predict(entrada)[0]))