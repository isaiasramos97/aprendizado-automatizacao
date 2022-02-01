import re

'''batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())'''
# Batman: zero ocorrência de wo
# batwoman: uma
# batwowowowom: quatro

'''batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 is None)'''
# a regex bat(wo)+man não identificará uma correspondência na string 'The Adventures of Batman',
# pois pelo menos um wo é exigido pelo sinal de adição
