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
# para nao retornar espaços e pontos, podemos adicionar os mesmos junto as vogais
consonantRegex = re.compile(r'[^aeiouAEIOU .]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))
# circunflexo (^) e cifrão ($)
'''o circunflexo tbm pode ser usado no inicio para indicar que uma corresp deve ocorrer no inicio de um texto
pesquisado. da msm maneira, podemos colocar um cifrão no final para indicar que a string deve terminar com esse padrão
de regex.
podemos tbm usá-los juntos para indicar que a string toda deve corresponder à regex'''

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello World'))
print(beginsWithHello.search('He said hello.') is None)
# a string r'\d$' de expressão regular corresponde a strings que terminem com um caractere numerico de 0 a 9
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two') is None)
# a string r'^\d+$' corresponde a strings que comecem e terminem com um ou mais caracteres numéricos
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') is None)
print(wholeStringIsNum.search('12 34567890') is None)

# Caractere-curinga . (ponto)
'''Corresponde a qualquer caractere, exceto quebras de linha'''
atRegex = re.compile(r'.at')  # o ponto corresponde a um caractere. na string abaixo, flat retorna como lat por exemplo
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# correspondendo a tudo usando o ponto-asterisco
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name:Isaias Last Name:Ramos')
print(mo.group(1))
print(mo.group(2))

# correspondencias sem diferenciar letras maiusculas de minusculas
robocop = re.compile(r'robocop', re.IGNORECASE)  # re.IGNORECASE pode ser usado como re.I
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

# substituindo strings com metodo sub()
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# administrando regexes complexas
# exemplo: podemos solicitar que uma função re.compile() ignore espaços em branco e comentarios na string de regex
# esse modo pode ser habilitado com a variavel re.VERBOSE como segundo argumento
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # codigo de área
(\s|-|\.)? # separador
\d{3} # primeiros 3 dígitos
(\s|-|\.) # separador
\d{4} # últimos 4 dígitos
(\s*(ext|x|ext.)\s*\d{2,5})? # extensão
)''', re.VERBOSE)
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# observe que tudo o que está após o # na linha é ignorado
