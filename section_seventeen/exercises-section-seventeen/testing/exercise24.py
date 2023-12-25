"""
Baseando-se no exercicio 23 adicione os metodos canalAcima e canalAbaixo,
sendo que o metodo canalAcima deve sintonizar sempre o proximo canal em
relacao ao canal atual, onde ao chegar ao maior canal possivel devera voltar ao
canal 1. O metodo canalAbaixo deve sintonizar sempre o canal anterior em
relacao ao canal atual, onde ao chegar ao canal 1 devera voltar ao maior canal
possivel, simulando desta forma o funcionamento de um televisor.
"""
from classes.house import Television

t1 = Television(True, 50, 20, 50, 100)

t1.channel_above()
print(t1.print())

t2 = Television(True, 1, 20, 50, 100)

t2.channel_below()
print(t2.print())
