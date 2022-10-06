from threading import Thread
import time
import requests

URL = "https://dummyjson.com/products"
cenarios = [10, 100, 200, 500, 1000]
resultados = open("resultados-concorrente.csv", "a")
resultados.write("Executions,TimeMillis,Category,Scenery\n")

class httpThread(Thread):
    def run(self):
        request = requests.get(URL)

for cenario in cenarios:
    for teste in range(20):
        threads = []
        startTime = int(time.time() * 1000)
        for t in range(cenario):
            thread = httpThread()
            threads.append(thread)
            thread.start()
        for t in threads:
            t.join()
        endTime = int(time.time() * 1000)
        duration = endTime - startTime
        print("cenario: "+ str(cenario) + " teste: " + str(teste) + " duraçao: " + str(duration))
        resultados.write(str(cenario) + ',' + str(duration) + "," + "concurrent" + "," + str(cenarios.index(cenario)) + "\n")


resultados.close()