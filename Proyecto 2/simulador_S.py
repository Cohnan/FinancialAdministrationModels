import numpy as np
import matplotlib.pyplot as plt
import time

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
