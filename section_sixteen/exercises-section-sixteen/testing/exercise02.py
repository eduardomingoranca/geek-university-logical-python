"""
Crie uma classe Agenda que pode armazenar 10 pessoas e seja capas de realizar as
seguintes operacoes:
    <> void armazenaPessoa(String nome, int idade, float altura);
    <> void removePessoa(String nome);
    <> int buscaPessoa(String nome); // informa em que posicao da agenda esta a pessoa
    <> void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
    <> void imprimePessoa(int index); // imprime os dados da pessoa que esta na posicao
    'i' da agenda.
"""
from classes.Schedule import Schedule

s1 = Schedule('Noah Calhoun', 25, 1.80)

s1.search_person('Noah Calhoun')

s1.print_schedule()

s1.print_schedule()
