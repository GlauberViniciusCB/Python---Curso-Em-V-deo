algo= input("Digite Algo:")
print('O Contéudo Digitado É Do Tipo {}'.format(type(algo)))
print('É Um Número ?',algo.isnumeric())
print('É Alfabético ? ',algo.isalpha())
print('É Alfanúmerico ? {}'.format(algo.isalnum()))
print('É Decimal ? {}'.format(algo.isdecimal()))
print('É Composta Só Por Espaços ? {}'.format(algo.isspace()))
print('Está Escrita em Minúsculo ? {}'.format(algo.islower()))
print('Está Escrito Em Maiúsculo ? {}'.format(algo.isupper()))
print('Está Capitalizada Significa Inicia Com Letra Maiúscula ? {}'.format(algo.istitle()))