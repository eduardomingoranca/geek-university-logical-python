"""
As tarifas de certo parque de estacionamento sao as seguintes:
    <> 1ª e 2ª hora - R$ 1.00 cada
    <> 3ª e 4ª hora - R$ 1.40 cada
    <> 5ª hora e seguintes - R$ 2.00 cada
O numero de horas a pagar eh sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagara por duas horas, que eh o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
sao apresentados na forma de pares de inteiros, representando horas e minutos. Por
exemplo, o par 12 50 representara "dez para a uma da tarde". Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preco cobrado pelo estacionamento. Admite-se que a chegada e a partida se dao com
intervalo nao superior a 24 horas. Portanto, se uma dada hora de chegada for superior
a da partida, isso nao eh uma situacao de erro, antes significara que a partida ocorreu
no dia seguinte ao da chegada.
"""
try:
    print('Informe a hora e minuto de entrada: ')
    horaEntrada = int(input())
    minutoEntrada = int(input())

    print('Informe a hora e minuto de saida: ')
    horaSaida = int(input())
    minutoSaida = int(input())

    horaFinal = 0
    minutoFinal = 0

    if horaEntrada > horaSaida:
        horaFinal = (horaSaida + 24) - horaEntrada
    else:
        horaFinal = horaSaida - horaEntrada

    if minutoEntrada > minutoSaida:
        minutoFinal = (minutoSaida + 60) - minutoEntrada
    else:
        minutoFinal = minutoSaida - minutoEntrada

    print(f'A permanencia no estacionamento foi de: {horaFinal} horas e {minutoFinal} minutos.')

    tempoMinutos = horaFinal * 60 + minutoFinal
    preco = 0.0

    if 1 <= tempoMinutos <= 60:
        preco = 1.0
        print(f'O valor a ser pago sera de R$ {preco:.2f}')
    elif 60 < tempoMinutos <= 120:
        preco = 2.0
        print(f'O valor a ser pago sera de R$ {preco:.2f}')
    elif 120 < tempoMinutos <= 180:
        preco = 4.2
        print(f'O valor a ser pago sera de R$ {preco:.2f}')
    elif 180 < tempoMinutos <= 240:
        preco = 5.6
        print(f'O valor a ser pago sera de R$ {preco:.2f}')
    elif tempoMinutos > 240:
        preco = horaFinal * 2.0
        print(f'O valor a ser pago sera de R$ {preco:.2f}')
    else:
        print('Tempo de permanencia minimo, nao sera necessario pagar!')

except ValueError:
    print('O formado do dado informado esta invalido!')
