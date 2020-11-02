import pymorphy2
import string

morph = pymorphy2.MorphAnalyzer()
text = '- Что, Петр, не видать еще? - спрашивал 20-го мая 1859 года, выходя без шапки на низкое крылечко постоялого двора на *** шоссе, барин лет сорока с небольшим, в запыленном пальто и клетчатых панталонах, у своего слуги, молодого и щекастого малого с беловатым пухом на подбородке и маленькими тусклыми глазенками.'

tsplit = text.split()

table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tsplit]
print(stripped)
for i in stripped:
    word = morph.parse(i)[0]
    print(i, ' - ',word.tag)

for i in stripped:
    word = morph.parse(i)[0]
    print(i, ' - ',word.normal_form)
