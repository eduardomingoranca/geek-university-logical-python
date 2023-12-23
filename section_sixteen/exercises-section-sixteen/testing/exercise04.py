"""
Crie uma classe Televisao e uma classe ControleRemoto que pode controlar o volume
e trocar os canais da televisao.
    <> O controle de volume permite aumentar ou diminuir a potencia do volume de
       som em uma unidade de cada vez.
    <> O controle de canal tambem permite aumentar e diminuir o numero do canal
       em uma unidade, porem, tambem possibilita trocar para um canal indicado;
    <> Tambem devem existir metodos para consultar o valor do volume de som e o
       canal selecionado.
"""
from classes.RemoteControl import RemoteControl
from classes.Television import Television

cr1 = RemoteControl(4, 5)
t1 = Television(cr1.get_sound(), cr1.get_channel())

t1.volume_up(5)

t1.volume_down(1)

t1.channel_up(1)

t1.channel_down(2)

print(t1.get_sound(), t1.get_channel())
