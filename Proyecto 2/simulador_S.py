import numpy as np
import matplotlib.pyplot as plt
import time

# Función que simula y grafica el precio de un activo S modelado mediante la ecuación diferencial estocástica dS = mu*S*dt + sigma*S*dW, 
# donde W es un proceso de Wiener
#
# 	Parámetros
# S0: precio en el tiempo 0 del activo
# mu: rentabilidad promedio del activo
# sig: volatilidad del activo
# dt: cambio "infinitesimal" de tiempo. Afecta la precision de las aproximaciones.
# Dt: periodo de gran escala de tiempo, correspondiente a 1 unidad de tiempo
# N: numero de periodos o tiempos a graficar
# graficar: booleano indicando si se quiere o no graficar los datos hallados
# pts: número de parejas (t, Ss) subconjunto del total calculado que se desean retornar y graficar (i.e. resolución de los datos retornados)
# txtad: texto adicional a imprimir en el gráfico
def grafico_valor_activo(S0 = 100, mu = 0.02, sig = 0.07, dt = 0.001, Dt = 1, N = 10, graficar = True, pts = 0, txtad = ""):
    tf = N*Dt + dt
    ts = np.arange(0, tf, dt)
    dws = np.array([np.random.normal(0, np.sqrt(dt)) for t in ts])
    
    Ss = np.zeros(len(ts))
    Ss[0] = S0
    
    # Calculo del valor de S para los tiempos t en ts
    for i in range(1, len(ts)):
        S = Ss[i-1]
        ti = ts[i]
        dS = S*(mu*dt + sig*dws[i-1])
        Ss[i] = S + dS 
    
    if pts == 0:
        plotTs = ts
        plotSs = Ss
    else:
        plotis = np.arange(0, pts)*(len(ts) - 1)//(pts - 1)
        plotTs = np.zeros(len(plotis))
        plotSs = np.zeros(len(plotis))
        
        for j in range(len(plotis)):
            i = plotis[j]
            plotTs[j] = ts[i]
            plotSs[j] = Ss[i]
    
    if not graficar:
        return plotTs, plotSs
    
    figura = plt.figure(figsize = (8,5))
    plt.title("Valor Simulado del precio del Activo (S) con \n\
               $\mu=$" + str(mu) + ", $\sigma=$" + str(sig) + "\n" + txtad)

    plt.xlabel("Tiempo $t$")
    plt.ylabel("Precio $S$/$\n % de incremento respecto al precio inicial $S_0 = 100$")
    
    plt.plot(plotTs, plotSs)
    plt.show()
    
    return ts, Ss
