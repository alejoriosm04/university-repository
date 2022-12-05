def nota(m, n, m_words, n_words):
    diccionario = dict()
    counter = 0
    for i in range(len(m_words)):
        diccionario[m_words[i]] = 1

    for i in range(len(n_words)):
        if n_words[i] in diccionario:
            diccionario[n_words[i]] = 2
        else:
            diccionario[n_words[i]] = 1
    
    for value in diccionario.values():
        if value == 2:
            counter+=1
    
    if counter == len(n_words):
        return "Si"
    else:
        return "No"


def main():
    m, n = map(int, input().split())
    m_words = input().split(" ")
    n_words = input().split(" ")

    print(nota(m, n, m_words, n_words))


if __name__ == '__main__':
    main()