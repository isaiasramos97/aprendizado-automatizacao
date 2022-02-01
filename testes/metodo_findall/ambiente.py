import re

# enquanto search retorna um objeto match do primeiro texto correspondente na string pesquisada,
# o metodo findall() retorna as strings todas as correspondencias na string pesquisada.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

# findall nao retorna um objeto match, mas uma lista de strings - desde que nao haja grupos na expressão regular.
# cada string da lista é uma parte do texto pesquisado que correspondeu à expressão regular

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # nao tem nenhum grupo
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# se houver grupos na expressão regular, findall() retornará uma lista de tuplas.
# Cada tupla representa uma correspondência identificada,
# e seus itens serão as strings correspondentes a cada grupo da regex.

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # tem grupos
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# exemplos de classes de caracteres:

xmasRegex = re.compile(r'\d+\s\w+')  # \d+: um ou mais digitos; \s: espaço em branco; \w+: um ou mais caracteres
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens,'
                  '2 doves, 1 partridge')   # findall retorna todas as strings que correspondam ao padrao em uma lista


# criando suas proprias classes de caracteres
'''Haverá ocasiões em que as classes abreviadas serão amplas demais. Podemos definir uma classe própria
Por exemplo:'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
'''Também é possível incluir intervalos de letras ou de números usando um hífen. Por exemplo, a classe de caracteres
[a-zA-ZO-9] corresponderá a todas as letras minúsculas, maiúsculas e a números.
Ao inserir um acento circunflexo logo depois do colchete de abertura da classe de caracteres, podemos criar uma classe
negativa de caracteres'''
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))     # mostra não-vogais. espaços inclusos
