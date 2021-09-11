# premiere liste pour les symboles des éléments
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

# troisième liste pour le nom des elements
nomElem = ["", "Hydrogène", "Hélium", "Lithium", "Béryllium", "Bore", "Carbone", "Azote", "Oxygène", "Fer", "Néon", "Sodium", "Magnésium",
"Aluminium", "Silicium", "Phosphore", "Souffre", "Chlore", "Aragon", "Potassium", "Calcium", "scandium", "Titane", "Vanadium", "Chrome",
 "Manganèse", "Fer", "Cobalt", "Nickel", "Cuivre", "Zinc", "Gallium", "Germanium", "Arsenic", "Sélénium", "Brome", "Krypton","Rubidium", 
 "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdène", "Technétium", "Ruthénium", "Rhodium", "Palladium", "Argent", "Cadmium", "Indium", 
 "Étain", "Antimoine", "Tellure", "Iode", "Xénon", "Césium", "Baryum", "Lanthane", "Cérium", "Praséodyme", "Néodyme", "Prométhium", "Samarium", "Europium", 
 "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutécium", "Hafnium", "Tantale", "Tungstène", "Rhénium", "Osmium",
  "Iridium", "Platine", "Or", "Mercure", "Thallium", "Plomb", "Bismuth", "Polonium", "Astate", "Radon", "Francium", "Radium", "Actinium", "Thorium",
   "Protactinium", "Uranium", "Neptunium", "Plutonium", "Américium", "Curium", "Berkélium", "Californium", "Einsteinium", "Fermium", 
   "Mendélévium", "Nobélium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnérium", "Darmstadtium", 
   "Roentgenium", "Copernicium", "Ununtrium", "Flérovium", "Ununpentium", "Livermorium", "Ununseptium", "Ununoctium"]

#Nous avons ensuite créé plusieurs petits programmes qui effectues les différentes tâches possibles comme : chercher un symbole dans la liste grâce à son numéro atomique, chercher une masse molaire d'un élément grâce à son symbole puis deux calculs pour chercher une quantité de matière avec soit le symbole de l'élément soit son numéro atomique.

# définition de chaque fonction pour le menu
 
def fonction1() : #permet de trouver le symbole d'un élément grâce à son numéro atomique
    numero = int(input("Entrez le numero atomique : "))
    print("Le symbole de l'élément est", symbole[numero],".")
 
def fonction2() : #permet de calculer une quantité de matière grâce au numéro atomique
    numero2 = int(input("Entrez le numero atomique : "))
    masse = int(input("Entrez la masse en gramme : "))
    mol = masse/masseMol[numero2]
    print("Il y a", mol,"mol.")
 
 
def fonction3() :  #permet de trouver une masse molaire grâce au symbole de l'élément
    symb1 = input("Entrez le symbole de l'élément:")
    i = 0  
    while i < 113 :
        if symbole[i] == symb1 :
            print("La masse molaire est", masseMol[i],"g.mol-1.")
            break
        i = i + 1
 
 
def fonction4() : #permet de calculer une quantité de matière grâce au symbole de l'élément
    masse2 = float(input("Entrez la masse en gramme : "))
    symb2 = input("Entrez le symbole de l'élément : ")
    i = 0  
    while i < 200 :
        if symbole[i] == symb2 :
            mol2 = masse2/masseMol[i]
            print("Il y a", mol2,"mol.")
            break
        i = i + 1
#print("nomElem "+str(len(nomElem)))
#print("symbole "+str(len(symbole)))
#z=0
#while z<119 :
#    print(symbole[z]+"    "+nomElem[z]+"    "+str(masseMol[z]) )
#    z =z+1
    