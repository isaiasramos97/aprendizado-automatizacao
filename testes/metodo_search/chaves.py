import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHaHaHaHa')    # mo1 recebe apenas HaHaHa
print(mo1.group())
print(mo1)
mo2 = haRegex.search('Ha')
print(mo2 is None)      # como não há correspondência em 'Ha', search retorna None == True

# correspondências greedy (gulosas) e nongreedy
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
# podemos verificar que o ponto de interrogação pode ter dois significados em regex:
# declarar uma correspondência nongreedy ou indicar um grupo opcional
