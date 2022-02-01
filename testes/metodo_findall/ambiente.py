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

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # tem grupos
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
