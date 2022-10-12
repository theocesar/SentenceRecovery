"""
// Théo César Zanotto da Silva

ENUNCIADO

Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de
linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função
que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta
url. Duas condições são importantes:

a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que
1000 palavras.

b) O texto desta página deverá ser transformado em um array de senteças.

Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca
Spacy.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


urls = ('https://hbr.org/2022/04/the-power-of-natural-language-processing',
        'https://monkeylearn.com/natural-language-processing/',
        'https://aliz.ai/en/blog/natural-language-processing-a-short-introduction-to-get-you-started/',
        'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/',
        'https://en.wikipedia.org/wiki/Natural_language_processing')


def webs():
    html_page = urlopen(url).read()
    scrap = BeautifulSoup(html_page, 'html.parser')

    for uw in scrap(["script", "style"]):
        uw.decompose()

    end_r = list(scrap.stripped_strings)

    return end_r


if __name__ == "__main__":

    for element in range(len(urls)):
        url = urls[0 + element]
        print(repr(webs()))
