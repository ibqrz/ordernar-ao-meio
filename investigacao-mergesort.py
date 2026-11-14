"""
Investigação — como ordenar dividindo ao meio
Aula 13 (sala invertida) · Análise e Complexidade de Algoritmos

Este arquivo acompanha o roteiro. Faça as etapas NA ORDEM: cada uma usa a anterior.
O programa se autoverifica — quando uma etapa estiver certa, ele avisa.

Complete os trechos marcados com  # COMPLETE
Rode com:  python3 investigacao-mergesort.py
"""
import math
import random

# ==========================================================
# ETAPA 1 — A intercalação
# ==========================================================
# Recebe DUAS listas que já estão ordenadas e devolve UMA lista ordenada
# com todos os elementos. Conte as comparações entre elementos.

def intercalar(a, b, cont):
    """a e b já vêm ordenadas. Devolve a junção ordenada."""
    saida = []
    i = j = 0
    while i < len(a) and j < len(b):
        cont[0] += 1   

        if (a[i] <= b[j]) :
            saida.append(a[i])
            i += 1
        else:
            saida.append(b[j])
            j += 1

    saida += a[i:]
    saida += b[j:]

    return saida

def etapa_1():
    print("=" * 70)
    print("ETAPA 1 — intercalar duas listas já ordenadas")
    print("=" * 70)
    casos = [("alternados",            [1, 3, 5], [2, 4, 6]),
             ("um todo antes do outro",[1, 2, 3], [4, 5, 6]),
             ("um todo depois",        [4, 5, 6], [1, 2, 3]),
             ("tamanhos diferentes",   [1, 5, 9], [2, 3, 4, 6, 7, 8])]
    print(f"{'caso':<24} {'resultado':<28} {'comparações':>12} {'p+q−1':>7}")
    tudo_ok = True
    for nome, a, b in casos:
        c = [0]
        r = intercalar(a, b, c)
        ok = (r == sorted(a + b))
        tudo_ok &= ok
        print(f"{nome:<24} {str(r):<28} {c[0]:>12} {len(a)+len(b)-1:>7}"
              f"{'' if ok else '   <- INCOMPLETO'}")
    if tudo_ok:
        print("\n  Etapa 1 OK. Agora responda no roteiro:")
        print("  (a) qual foi o MAIOR número de comparações, e em que caso?")
        print("  (b) qual foi o MENOR, e em que caso?")
        print("  (c) intercalar duas listas de tamanho n/2 custa no máximo quanto, em função de n?") 

# ==========================================================
# ETAPA 3 — O algoritmo
# ==========================================================
# Leia a ETAPA 2 do roteiro ANTES de escrever este trecho.


def merge_sort(v, cont):
    if len(v) <= 1:
        return v
    meio = len(v) // 2
    esquerda = merge_sort(v[:meio], cont)
    direita = merge_sort(v[meio:], cont)
    return intercalar(esquerda, direita, cont)


def etapa_3():
    print("\n" + "=" * 70)
    print("ETAPA 3 — o algoritmo completo")
    print("=" * 70)
    random.seed(7)
    tudo_ok = True
    for n in (1, 2, 5, 17, 100):
        v = random.sample(range(n * 10), n)
        c = [0]
        r = merge_sort(v, c)
        ok = (r == sorted(v))
        tudo_ok &= ok
        print(f"  n = {n:>4}  ordenou corretamente? {'sim' if ok else 'NÃO'}"
              f"   ({c[0]} comparações)")
    if tudo_ok:
        print("\n  Etapa 3 OK. Siga para a medição.")


    else:
        print("\n  Ainda não ordena. Confira a ETAPA 2 do roteiro.")


# ==========================================================
# ETAPA 4 — Medir (não precisa alterar)
# ==========================================================

def etapa_4():
    print("\n" + "=" * 70)
    print("ETAPA 4 — três tipos de entrada")
    print("=" * 70)
    random.seed(42)
    print(f"{'n':>7} {'aleatório':>11} {'já ordenado':>12} {'invertido':>11} "
          f"{'n·log₂n':>10} {'(n/2)·log₂n':>13}")
    for n in (8, 64, 256, 1024, 4096):
        al = random.sample(range(n * 10), n)
        c1 = [0]; merge_sort(al, c1)
        c2 = [0]; merge_sort(list(range(n)), c2)
        c3 = [0]; merge_sort(list(range(n, 0, -1)), c3)
        k = int(math.log2(n))
        print(f"{n:>7} {c1[0]:>11,} {c2[0]:>12,} {c3[0]:>11,} "
              f"{n*k:>10,} {(n//2)*k:>13,}")
    print("\n  No roteiro: as colunas 'já ordenado' e 'invertido' deram o MESMO valor.")
    print("  Isso surpreende? E por que as duas ficaram ABAIXO da coluna 'aleatório'?")


# ==========================================================
# ETAPA 5 — O teste da duplicação (não precisa alterar)
# ==========================================================

def etapa_5():
    print("\n" + "=" * 70)
    print("ETAPA 5 — dobrar n e ver o que acontece")
    print("=" * 70)
    random.seed(3)
    anterior = None
    print(f"{'n':>7} {'comparações':>13} {'T(2n)/T(n)':>12} {'2 + 2/log₂n':>13}")
    for n in (512, 1024, 2048, 4096, 8192):
        c = [0]; merge_sort(random.sample(range(n * 10), n), c)
        razao = f"{c[0]/anterior:>12.3f}" if anterior else f"{'—':>12}"
        print(f"{n:>7} {c[0]:>13,} {razao} {2 + 2/math.log2(n):>13.3f}")
        anterior = c[0]
    print("\n  No roteiro: a razão bate com a última coluna? De que classe isso é sinal?")


# ==========================================================
# ETAPA 6 — Contra o insertion sort (não precisa alterar)
# ==========================================================

def insertion_sort(v, cont):
    v = list(v)
    for i in range(1, len(v)):
        chave = v[i]; j = i - 1
        while j >= 0:
            cont[0] += 1
            if v[j] > chave:
                v[j+1] = v[j]; j -= 1
            else:
                break
        v[j+1] = chave
    return v


def etapa_6():
    print("\n" + "=" * 70)
    print("ETAPA 6 — mergesort contra insertion sort (vetor aleatório)")
    print("=" * 70)
    random.seed(11)
    print(f"{'n':>7} {'mergesort':>12} {'insertion':>13} {'quantas vezes mais':>20}")
    for n in (100, 500, 1000, 2000):
        al = random.sample(range(n * 10), n)
        cm = [0]; merge_sort(al, cm)
        ci = [0]; insertion_sort(al, ci)
        razao = f"{ci[0]/cm[0]:>19.1f}×" if cm[0] else f"{'—':>20}"
        print(f"{n:>7} {cm[0]:>12,} {ci[0]:>13,} {razao}")
    print("\n  No roteiro: a vantagem do mergesort cresce ou estabiliza conforme n aumenta?")


# ==========================================================
# ETAPA 7 — Um experimento sobre estabilidade
# ==========================================================
# Pares (nota, nome). Ordenar pela NOTA. O que acontece com quem empata?

def intercalar_variante(a, b, cont, usar_menor_igual):
    saida = []; i = j = 0
    while i < len(a) and j < len(b):
        cont[0] += 1
        leva_de_a = (a[i][0] <= b[j][0]) if usar_menor_igual else (a[i][0] < b[j][0])
        if leva_de_a:
            saida.append(a[i]); i += 1
        else:
            saida.append(b[j]); j += 1
    return saida + a[i:] + b[j:]


def merge_sort_variante(v, cont, usar_menor_igual):
    if len(v) <= 1:
        return v
    m = len(v) // 2
    return intercalar_variante(merge_sort_variante(v[:m], cont, usar_menor_igual),
                               merge_sort_variante(v[m:], cont, usar_menor_igual),
                               cont, usar_menor_igual)


def etapa_7():
    print("\n" + "=" * 70)
    print("ETAPA 7 — o que muda trocando <= por <")
    print("=" * 70)
    turma = [(7, "Ana"), (5, "Bruno"), (7, "Carla"), (6, "Davi"),
             (5, "Elisa"), (7, "Felipe"), (6, "Gabi"), (5, "Hugo")]
    print(f"  entrada (ordem da chamada):")
    print(f"     {[f'{n}-{x}' for n, x in turma]}")
    for usar in (True, False):
        c = [0]
        r = merge_sort_variante(turma, c, usar)
        print(f"\n  merge usando  {'<=' if usar else '< '}  :")
        print(f"     {[f'{n}-{x}' for n, x in r]}")
    print("\n  No roteiro: olhe só para quem tirou 5. A ordem entre eles mudou?")
    print("  Um único caractere do código decidiu isso. Que propriedade é essa?\n")


if __name__ == "__main__":
    etapa_1()
    etapa_3()
    etapa_4()
    etapa_5()
    etapa_6()
    etapa_7()
