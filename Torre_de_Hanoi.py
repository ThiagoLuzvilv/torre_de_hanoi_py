class Torres:
  def __init__(auto, disco=3):
    auto.disco = disco
    auto.torres = [[]] * 3
    auto.torres[0] = [i for i in range(auto.disco, 0, -1)]
    auto.torres[1] = []
    auto.torres[2] = []

  def __str__(auto):
    saida = ""
    for i in range(auto.disco, -1, -1):
      for j in range(3):
        if len(auto.torres[j]) > i:
          saida += " " + str(auto.torres[j][i])
        else:
          saida += " "
      saida += "\n"
    return saida + "-----"

  def mover(auto, da_torre, desti_torre):
    disco = auto.torres[da_torre].pop()
    auto.torres[desti_torre].append(disco)


def resolve_a_torre(torres, n, inicio_torre, desti_torre, torre_aux):
  #Caso Base
  if n == 0:
    return

  resolve_a_torre(torres, n - 1, inicio_torre, torre_aux, desti_torre)

  #Move o disco N para desti_torre.
  torres.mover(inicio_torre, desti_torre)
  print(torres)

  #Move os subproblemas do n - 1 disco da torre_aux para desti_torre
  resolve_a_torre(torres, n - 1, torre_aux, desti_torre, inicio_torre)


t = Torres(3)
print(t)
resolve_a_torre(t, t.disco, 0, 2, 1)
