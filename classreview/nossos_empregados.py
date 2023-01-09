from Empregado import Empregados

e1 = Empregados('Jão', 'Vendas', 'Diretor', 100000, 20)
e2 = Empregados('Linda', 'Executiva', 'CIO', 150000, 10)

print(e1.name)
print(e2.role)

print(e1.eligeble_for_retirement())
print(e2.eligeble_for_retirement())