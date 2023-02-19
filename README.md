# Sentence recovery
 
Simple web scraping algorithm that recovers the sentences of a text.

## In depth explanation:

The algorithm should transform a set of 5 websites, on the topic of natural language processing
into a set of five distinct lists of sentences. That is, you will make a function that, using the Beautifull Soap library, 
requests a url and extracts all the sentences from the url. 

Two conditions are important:

a) The web page (url) must point to an English web page containing no less than
1000 words.

b) The text from this page should be transformed into an array of sentences.
To separate sentences you can use punctuation marks or the functions inside the Spacy library.

