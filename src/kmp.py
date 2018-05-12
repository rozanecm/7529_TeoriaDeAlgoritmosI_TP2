#!coding=utf8
import sys


def make_table(word):
    """Arma la tabla de saltos para KMP del string 'word'"""
    table = [0] * len(word)

    table[0] = -1
    candidate = 0
    for i, character in enumerate(word[1:], 1):
        if character == word[candidate]:
            table[i] = table[candidate]
        else:
            table[i] = candidate
            candidate = table[candidate]
            while candidate >= 0 and character != word[candidate]:
                candidate = table[candidate]

        candidate += 1

    return table

def kmp(text, word):
    table = make_table(word)
    k = 0
    for i in range(len(text)):
        if word[k] == text[i]:
            k += 1
            if k == len(word):
                return i - k + 1
        else:
            k = table[k]
            if k < 0:
                k = 0

    return -1


def cycle(text, candidate):
    """Primera implementación: va rotando el string 'candidate' char por char
    y corriendo KMP entre el y un texto fuente. Devuelve true si KMP devuelve un match
    para alguna rotación
    """

    original_candidate = candidate

    candidate = candidate[-1] + candidate[:-1]
    while candidate != original_candidate:
        if kmp(text, candidate) >= 0:
            return True
        candidate = candidate[-1] + candidate[:-1]

    return False

def cycle_improved(text, candidate):
    """Optimización: Corre KMP sobre el texto fuente copiado dos veces,
    y el candidato. Si el candidato es una rotación cíclica del fuente,
    entonces KMP dará un match si se busca dentro del texto duplicado.
    """

    return kmp(text * 2, candidate) >= 0

def bruteforce(text, candidate):
    """Solución por fuerza bruta. Va rotando el string 'candidate' y
    comparando si es igual al texto fuente hasta que de True, o se rote
    hasta llegar al ciclo completo.
    """
    original_candidate = candidate

    candidate = candidate[-1] + candidate[:-1]
    while candidate != original_candidate:
        # Implementación lineal de igualdad de strings. Python optimiza el uso de '==' a O(1)
        strings_equal = True
        for i in range(len(text)):
            if text[i] != candidate[i]:
                strings_equal = False
                break

        if strings_equal:
            return True
        candidate = candidate[-1] + candidate[:-1]

    return False


def run():
    assert len(sys.argv) == 3

    chars = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    method = sys.argv[2]

    text = 'A' * chars + 'B'
    word = 'B' + 'A' * chars
    if method == '--kmp-optimize':
        print cycle_improved(text, word)
    elif method  == '--bruteforce':
        print bruteforce(text, word)
    elif method == '--kmp':
        print cycle(text, word)
    else:
        print "Metodo no reconocido:", method
if __name__ == '__main__':
    run()
