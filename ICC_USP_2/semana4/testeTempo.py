import time
import opcional1
import opcional2

inicioContagemTempo = time.time()


lista = opcional1.lista_grande(10000)


opcional2.ordena(lista)


finalContagemTempo = time.time()

print("Tempo decorrido = %f segundos" %(finalContagemTempo - inicioContagemTempo))