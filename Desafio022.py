nome = str(input('Informe O Seu Nome Completo: ')).strip()
print('\nAnalise:')
print ('Seu Nome Em Letra Minúscula É: {}'.format(nome.lower()))
print ('Seu Nome Em Letra Maiúscula É: {}'.format(nome.upper()))
total = len(nome)
lista_de_nomes =  nome.split()
total_de_nomes = len(lista_de_nomes)
primeiro_nome = len(lista_de_nomes[0])
print('Seu Nome Completo Tem: {} Letras.'.format(total - total_de_nomes+1))
print('Seu Primeiro Nome É: {} E Tem: {} Letras.'.format(lista_de_nomes[0],primeiro_nome))