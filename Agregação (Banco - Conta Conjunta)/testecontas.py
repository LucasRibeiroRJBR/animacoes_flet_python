from contas import Conta
from clientes import Cliente

cliente1 = Cliente(123,'João','Rua 1')
cliente2 = Cliente(345,'Maria','Rua 2')

conta1 = Conta([cliente1,cliente2],1,0)

conta1.gerarSaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarSaldo()

#print(f'{conta1.clientes[1].nome}')
for i in conta1.clientes:
    print(f'{i.nome}')

