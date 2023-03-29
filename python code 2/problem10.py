"""
Represent a small bilingual (English-Swedish) glossary given below as a
Python dictionary
("merry":"god", "christmas":"Jul", "and":"och", "happy":"gott" "new":"nytt","year":"ar")

and use it to translate your Christmas wishes from English into Swedish.

That is, write a python function translate() that accepts the bilingual dictionary and a
list of English words (your Christmas wish) and returns a list of equivalent Swedish words.
"""
def translate(bilingual,english):
    swedish= []
    for x in english:
        swedish.append(bilingual[x])

    return swedish

bilingual= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english=["happy","new","year"]
print("The bilingual dict is:",bilingual)
print("The english words are:",english)
swedish=translate(bilingual, english)
print("The equivalent swedish words are:",swedish)

