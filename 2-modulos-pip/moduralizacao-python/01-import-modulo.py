import moduloCalc #Uma maneira de importar todas as funções dentro do módulo
from moduloCalc import sum #Uma maneira de importar somente a função necessária do módulo
# from moduloCalc import sub
from moduloCalc import div
# from moduloCalc import mul

print(f"O valor da soma de 5 e 10 importada do módulo é de {sum(5, 10)}")
print(f"O valor da subtração entre 10 e 5 importada do módulo é de {moduloCalc.sub(10, 5)}")
print(f"O valor da divisão entre 10 e 5 importada do módulo é de {div(10, 5):.2f}")
print(f"O valor da multiplicação entre 10 e 5 importada do módulo é de {moduloCalc.mul(10, 5)}")