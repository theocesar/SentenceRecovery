"""
// Théo César Zanotto da Silva

O algoritmo deverá transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta
url. Duas condições são importantes:

a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que
1000 palavras.

b) O texto desta página deverá ser transformado em um array de sentenças.

Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca
Spacy.
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


array = []

# chosen urls
urls = ('https://hbr.org/2022/04/the-power-of-natural-language-processing',
        'https://monkeylearn.com/natural-language-processing/',
        'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html',
        'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/',
        'https://en.wikipedia.org/wiki/Natural_language_processing')


def corpus(link):
    # obtaining the content of the page
    page = urlopen(link).read()
    soup = BeautifulSoup(page, 'html.parser')

    # removing the unnecessary tags
    for script in soup(["script", "style", "footer", "header"]):
        script.decompose()

    # compacting all the data
    textof = ' '.join(soup.stripped_strings)

    # splitting the text in sentences
    textof = re.split("[!?:;.]", textof)

    return textof


# printing the resulting array.
for url in urls:
    print(corpus(url))
