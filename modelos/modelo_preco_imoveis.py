import pickle

modelo = open('modelo_preco_imoveis','rb')
lm_new = pickle.load(modelo)
modelo.close()

area = 38
garagem = 2
banheiros = 4
lareira = 4
marmore = 0
andares = 1

entrada = [[area, garagem, banheiros, lareira, marmore, andares]]

print(f'Area: {area} m²')
print(f'Garagem: {lareira} vagas')
print('Banheiros: ', banheiros)
print('Lareiras: ', lareira)
print('Tem acabamento em mármore?',("Sim" if marmore == 0 else "Não"))
print('Andares: ', andares)

print('Valor previsto de R$ {0:.2f}'.format(lm_new.predict(entrada)[0]))

