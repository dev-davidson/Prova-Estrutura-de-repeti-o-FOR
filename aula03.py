def gerar_tabuada(numero):
    print(f'Tabuada de {numero}:\n')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')


num_usuario = int(input('Informe um número para gerar a tabuada (entre 1 e 10): '))

if 1 <= num_usuario <= 10:
  
    gerar_tabuada(num_usuario)
else:
    print('Por favor, informe um número válido entre 1 e 10.')
