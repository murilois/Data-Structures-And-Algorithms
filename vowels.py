#Desafio envolvendo contagem de vogais, só um teste mesmo
string = str(input("Insira uma string: "))
def vowelCount(string):
    count = 0
    vogais = ["a","á","ã","â","e","é","ê","i","í","o","ó","ô","õ","u","ú","û"]
    hash = {"a":0, "e":0,"i":0,"o":0,"u":0}
    for i in string:
        if i in vogais.lower():
            count += 1
        if i == "a" or i == "á":
            hash["a"] += 1
        if i == "e" or i == "é":
            hash["e"] += 1
        if i == "i" or i == "í":
            hash["i"] += 1
        if i == "o" or i == "ó":
            hash["o"] += 1
        if i == "u" or i == "ú":
            hash["u"] += 1
    print(count)
    print(hash)
vowelCount(string)