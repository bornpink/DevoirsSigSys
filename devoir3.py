def systemeDiscret(A,B,C,D,ts,x=None):
    """
    Calcule la réponse d'un système discret en fonction d'une entrée x optionnelle.
    Si x n'est pas fourni, la fonction renvoie la réponse impulsionnelle du système.

    Le système est décrit par un temps d'échantillonnage ts > 0 en secondes,
    ainsi que par les matrices A,B,C,D telles que :
    q[n+1] = A*q[n] + B*x[n],
    y[n] = C*q[n] + D*x[n].
    
    Arguments
    ---------
    TODO
    
    Retourne
    --------
    TODO
    """
    
    # Représentation du système
    sys = sg.StateSpace(A,B,C,D, dt=ts)

    if x is None:
        # Renvoie la réponse impulsionnelle
        ty, y = sg.dimpulse(sys)
    
    else:
        # Calcule la réponse du système avec x comme entrée
        ty, y, xout = sg.dlsim(sys, x)
    
    # Formate y dans les bonnes dimensions
    y = np.array(y).squeeze()
    
    return (ty, y)
  
  
  
  
  
  
def computeMatrices(alpha,beta):
    
    A = 0 #TODO
    B = 0 #TODO
    C = 0 #TODO
    D = 0 #TODO
    
    return (A,B,C,D)
