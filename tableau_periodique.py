# premiere liste pour les symboles des éléments
symbole = ["", "H", "He", "Li","Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",  "Si", "P", "S", "Cl", "Ar",
           "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
           "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
           "Cs", "Ba","La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
           "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
           "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
           "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut", "Fl", "Uup", "Lv", "Uus", "Uuo"]
 
# seconde liste pour les masse molaires
masseMol = [0, 1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40,
            39, 40, 45, 48, 51, 52, 55, 56, 59, 59, 64, 65, 70, 73, 75, 79, 80, 84,
            85, 88, 89, 91, 93, 96, 98, 101, 103, 106, 108, 112, 115, 119, 122, 128, 127, 131,
            133, 137, 139, 140, 141, 144, 145, 150, 152, 157, 159, 162, 165, 167, 169, 173, 175,
            178, 181, 184, 186, 190, 192, 195, 197, 201, 204, 207, 209, 209, 210, 222,
            223, 226, 227, 232, 231, 238, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 262,
            267, 268, 271, 272, 277, 276, 281, 280, 285, 284, 289, 288, 293, 291, 294]

# troisième liste pour le nom des elements
nomElem = ["", "Hydrogene", "Helium", "Lithium", "Beryllium", "Bore", "Carbone", "Azote", "Oxygene", "Fluor", "Neon", "Sodium", "Magnesium",
"Aluminium", "Silicium", "Phosphore", "Soufre", "Chlore", "Aragon", "Potassium", "Calcium", "Scandium", "Titane", "Vanadium", "Chrome",
 "Manganese", "Fer", "Cobalt", "Nickel", "Cuivre", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Brome", "Krypton","Rubidium", 
 "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdene", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Argent", "Cadmium", "Indium", 
 "Etain", "Antimoine", "Tellure", "Iode", "Xenon", "Cesium", "Baryum", "Lanthane", "Cerium", "Praseodyme", "Neodyme", "Promethium", "Samarium", "Europium", 
 "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutecium", "Hafnium", "Tantale", "Tungstene", "Rhenium", "Osmium",
  "Iridium", "Platine", "Or", "Mercure", "Thallium", "Plomb", "Bismuth", "Polonium", "Astate", "Radon", "Francium", "Radium", "Actinium", "Thorium",
   "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", 
   "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", 
   "Roentgenium", "Copernicium", "Ununtrium/Nihomium", "Flerovium", "Ununpentium/Moscovium", "Livermorium", "Ununseptium/Tennesse", "Ununoctium/Oganesson"]

# Quatrième liste pour la catégorie des elements 
catElem = ["", "Non-métaux", "Gaz noble(non-métaux)", "Metaux alcalino-terreux", "Lanthanide (métaux)", "Métalloïde (non-métaux)", "Non-Métaux", "Non-Métaux", "Non-métaux",
"Halogène (non-métaux)", "Gaz noble(non-métaux)", "Metaux alcalino-terreux", "Lanthanide (métaux)", "Métaux pauvre", "Métalloïde (non-métaux)", "Non-métaux", "Non-métaux",
"Halogène (non-métaux)", "Gaz noble(non-métaux)", "Metaux alcalino-terreux", "Lanthanide (métaux)", "Métaux de transition", "Métaux de transition", "Métaux de transition",
"Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", 
"Métaux pauvre", "Métalloïde (non-métaux)", "Métalloïde (non-métaux)", "Non-métaux", "Halogène (non-métaux)", "Gaz noble(non-métaux)", "Metaux alcalino-terreux", 
"Lanthanide (métaux)", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", 
"Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux pauvre", "Métaux pauvre", "Métalloïde (non-métaux)", "Métalloïde (non-métaux)", 
"Halogène (non-métaux)", "Gaz noble(non-métaux)", "Metaux alcalino-terreux", "Lanthanide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", 
"Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", 
"Actinide (métaux)", "Actinide (métaux)", "Actinide (métaux)", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", 
"Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux pauvre", "Métaux pauvre", "Métaux pauvre", "Métalloïde (non-métaux)", 
"Halogène (non-métaux)", "Gaz noble(non-métaux)", "Metaux alcalino-terreux", "Lanthanide (métaux)", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", 
"Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", "Métaux alcalins", 
"Métaux alcalins", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", "Métaux de transition", 
"Métaux de transition", "Métaux de transition", "Métaux pauvre", "Métaux pauvre", "Métaux pauvre", "Métaux pauvre", "Halogène (non-métaux)", "Gaz noble(non-métaux)"]
#Nous avons ensuite créé plusieurs petits programmes qui effectues les différentes tâches possibles comme : chercher un symbole dans la liste grâce à son numéro atomique, chercher une masse molaire d'un élément grâce à son symbole puis deux calculs pour chercher une quantité de matière avec soit le symbole de l'élément soit son numéro atomique.
def table():
  print("1: Calcul avec donnée")
  print("2: Tableau périodique")
  envie = input("Quel programme: ")
  if envie == "1":
    prechoix()
  elif envie == "2":
    period()
  else:
    print("Choix impossible")
    table()
    
def prechoix():
  selec = input("Quel programme: ")
  choix(selec)
def choix(selec):
  if selec=="1":
    num_symb()
  elif selec == "2":
    nummas_quant()
  elif selec == "3":
    symb_masmol()
  elif selec == "4":
    symb_quant()
  elif selec == "5":
    infoelem()
  else:
    print("fonction inconnu")
# définition de chaque fonction pour le menu
 
def num_symb() : #permet de trouver le symbole d'un élément grâce à son numéro atomique
    numero = int(input("Numero atomique ?: "))
    print("Symbole de l'élément ?", symbole[numero],".")
    print("Nom : "+nomElem[numero])
 
def nummas_quant() : #permet de calculer une quantité de matière grâce au numéro atomique
    numero2 = int(input("Numero atomique : "))
    masse = int(input("Masse (en g) : "))
    mol = masse/masseMol[numero2]
    print("Il y a", mol,"mol.")
 
 
def symb_masmol() :  #permet de trouver une masse molaire grâce au symbole de l'élément
    symb1 = input("Symbole de l'élément:")
    i = 0  
    while i < 119 :
        if symbole[i] == symb1 :
            print("Masse molaire: ", masseMol[i],"g.mol-1.")
            break
        i = i + 1
 
 
def symb_quant() : #permet de calculer une quantité de matière grâce au symbole de l'élément
    masse2 = float(input("Masse en gramme : "))
    symb2 = input("Symbole de l'élément : ")
    i = 0  
    while i < 200 :
        if symbole[i] == symb2 :
            mol2 = masse2/masseMol[i]
            print("Il y a", mol2,"mol.")
            break
        i = i + 1
def infoelem():
    elem=input("Quel élém: ")
    z = 0
    reponse = False
    while z < 119 :
        if nomElem[z] == elem :
            numElem=z
            #print(symbole[z])
            reponse = True
            break
        elif symbole[z] == elem:
            numElem = z
            #print(nomElem[z])
            reponse = True
            break
        #else :
            #print("L'élément est introuvable")            
        z = z+1
    if reponse == True:
        print("Nom: "+nomElem[z])
        print("Symbole : "+symbole[z])
        print("Numéro atomique: "+str(z))
        print("Masse moleculaire: "+str(masseMol[z])+ " mol")
        print("Type: "+ catElem[z])
    else :
        print("L'élément "+ str(elem)+ " est introuvable")
def period():
  print("Pas terminer")
table()