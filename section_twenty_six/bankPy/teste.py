from models.cliente import Cliente
from models.conta import Conta


felicity: Cliente = Cliente('Felicity Jones', 'felicity@email.com', '123.456.789-01', '02/09/1987')
angelina: Cliente = Cliente('Angelina Wheeler', 'angelina@email.com', '234.567.890-02', '08/07/1978')

#print(felicity)
#print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

#print(contaf)
#print(contaa)
