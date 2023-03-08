## LE CONTENU DE CETTE CELLLULE EST A SOUMETTRE SUR INGINIOUS
def systemeDiscret(A,B,C,D,ts,x=None):
    """
    Calcule la réponse d'un système discret en fonction d'une entrée x optionnelle.
    Si x n'est pas fourni, la fonction renvoie la réponse impulsionnelle du système.

    Le système est décrit par un temps d'échantillonnage ts > 0 en secondes,
    et par les matrices A,B,C,D qui sont telles que :
        q[n+1] = A*q[n] + B*x[n],
        y[n] = C*q[n] + D*x[n].
    
    Arguments
    ---------
    A (np.ndarray): matrice d'état du système (cf. définition ci-dessus)
    B (np.ndarray): matrice de commande du système (cf. définition ci-dessus)
    C (np.ndarray): matrice d'observation du système (cf. définition ci-dessus)
    D (np.ndarray): matrice d'action directe du système (cf. définition ci-dessus)
    ts (float): temps d'échantillonnage en secondes, doit être >0
    x (np.ndarray)(optionnel): entrée du système, qui commence en t=0

    Retourne
    --------
    ty (np.ndarray): vecteur temps associé au signal y
    y (np.ndarray): réponse du système y pour l'entrée x, ou réponse impulsionnelle si x n'est pas fourni

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












## LE CONTENU DE CETTE CELLLULE EST A SOUMETTRE SUR INGINIOUS
def computeMatrices(alpha,beta):
    """
    Renvoie la représentation d'état du système y[n] = alpha*x[n] + beta*y[n-1].
    Pour rappel, les matrices A,B,C,D sont telles que :
        q[n+1] = A*q[n] + B*x[n], 
        y[n] = C*q[n] + D*x[n].
    
    Arguments
    ---------
    alpha (float): paramètre du système
    beta (float): paramètre du système

    Retourne
    ---------
    A (np.ndarray): matrice d'état du système (cf. définition ci-dessus)
    B (np.ndarray): matrice de commande du système (cf. définition ci-dessus)
    C (np.ndarray): matrice d'observation du système (cf. définition ci-dessus)
    D (np.ndarray): matrice d'action directe du système (cf. définition ci-dessus)
    """
    
    # q[n+1] = beta*q[n] + alpha*x[n]
    # y[n]   = beta*q[n] + alpha*x[n]

    A = np.array(beta)
    B = np.array(alpha)
    C = np.array(beta)
    D = np.array(alpha)
    
    return (A,B,C,D)
