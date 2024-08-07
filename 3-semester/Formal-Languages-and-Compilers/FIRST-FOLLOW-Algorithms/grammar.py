class grammar():

    def __init__(self, nonterminals, terminals, productions, start):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start = start

    
def read_grammar():
    nonterminals = input("Enter the nonterminals: ").split()
    terminals = input("Enter the terminals: ").split()
    productions = {}
    for i in range(len(nonterminals)):
        production = input("Enter a production:")
        productions[production.split('-')[0]] = production.split("->", 1)[1]
        productions[production.split('-')[0]] = productions[production.split('-')[0]].split("|")

    start = input("Enter the start symbol: ")
    
    return nonterminals, terminals, productions, start


def FIRST(G, symbol, P, FIRST_SET):
    for production in P:
        counter = 0
        for element in production:
            if element in G.terminals:
                FIRST_SET[symbol].append(element)
                break
            if element in G.nonterminals:
                counter += 1
                if FIRST(G, element, G.productions[element], FIRST_SET):
                    FIRST_SET[symbol].extend(FIRST_SET[element])
                    FIRST_SET[symbol].remove('Ɛ')
                else:
                    FIRST_SET[symbol].extend(FIRST_SET[element])
                    break

                if counter == len(production):
                    if 'Ɛ' in FIRST_SET[element]:
                        FIRST_SET[symbol].append('Ɛ')

    if 'Ɛ' in P:
        return True
    else:
        return False
                        


def main():
    nonterminals, terminals, productions, start = read_grammar()
    print(productions)
    G = grammar(nonterminals, terminals, productions, start)
    FIRST_SET = {}
    for i in nonterminals:
        FIRST_SET[i] = []

    print(FIRST_SET)
    FIRST(G, start, productions[start], FIRST_SET)
    print(FIRST_SET)


if __name__ == "__main__":
    main()