"""
Crie uma classe denominada Elevador para armazenar as informacoes de um elevador
dentro de um predio. A classe deve armazenar o andar atual (terreo = 0), total de
andares no predio, excluido o terreo, capacidade do elevador, e quantas pessoas estao
presentes nele.

A classe deve tambem disponibilizar os seguintes metodos:
    <> Inicializa: que deve receber como parametros a capacidade do elevador e o
       total de andares no predio (os elevadores sempre comecam no terreo e vazio);
    <> Entra: para acrescentar uma pessoa no elevador (so deve acrescentar se ainda
       houver espaco);
    <> Sai: para remover uma pessoa do elevador (so deve remover se houver alguem
       dentro dele);
    <> Sobe: para subir um andar (nao deve subir se ja estiver no ultimo andar);
    <> Desce: para descer um andar (nao deve descer se ja estiver no terreo);
    <> Encapsular todos os atributos da classe (criar os metodos set e get).
"""
from classes.Elevator import Elevator, goes_into

name = 'Alisson Nelson'

el1 = Elevator(10, 3, name, 19, 1.73)

goes_into(name, 19, 1.73)

el1.leaves(name, 19, 1.73)

el1.rise(5)

el1.go_down(2)

print(el1.get_capacity(), el1.get_floors(), el1.get_name(), el1.get_age(), el1.get_height())
