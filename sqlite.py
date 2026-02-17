import sqlite3
conn=sqlite3.connect('livre.db')
curseur=conn.cursor()
curseur.execute("CREATE TABLE IF NOT EXISTS livre(id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT NOT NULL, auteur TEXT NOT NULL, annee INTEGER NOT NULL CHECK (typeof(annee)='integer'))")
curseur.execute("CREATE TABLE IF NOT EXISTS emprunts(id INTEGER PRIMARY KEY AUTOINCREMENT,id_livre INTEGER,date_emprunt DATETIME NOT NULL DEFAULT CURRENT_TIME,date_retour DATETIME, FOREIGN KEY(id_livre) REFERENCES livre(id) )")
curseur.execute("PRAGMA foreign_keys=ON")
conn.commit()
def menue():
    print("1-Ajouter un livre"
          "\n2-Emprunter un livre"
          "\n3-retourner un livre"
          "\n4-liste des livres empruntes"
          "\n5-lister les auteurs d'un livre"
          "\n6-sortir le la base")
def ajouter_livre():
    try:
        titre = input("entrer le titre du livre: ")
        auteur = input("entrer l'auteur du livre: ")
        annee = int(input("entrer l'annee du livre: "))
        curseur.execute("INSERT INTO livre(titre, auteur, annee) VALUES(?,?,?)",(titre,auteur,annee))
        conn.commit()
        print("livre ajoute")
    except Exception as e:
        print(f"l'erreur est : {e}")
        conn.rollback()
def emprunt_livre():
    nom = input("entrer le nom du livre: ")
    curseur.execute("SELECT id FROM livre WHERE titre=?", (nom,))
    n = curseur.fetchone()
    if n is None:
        print("Livre n'existe pas")
    else:
        id_livre = n[0]
        curseur.execute("SELECT * FROM emprunts WHERE id_livre=? AND date_retour IS NULL", (id_livre,))
        test = curseur.fetchone()
        if test is None:
            curseur.execute("INSERT INTO emprunts(id_livre, date_emprunt) VALUES(?,CURRENT_TIMESTAMP)", (id_livre,))
            conn.commit()
            print("operation reussie")
        else:
            print("livre deja emprunte")
def retourner_livre():
    nom=input("entrer le nom du livre que vous souhaitez rendre: ")
    curseur.execute("SELECT id FROM livre WHERE titre=?", (nom,))
    id_livre = curseur.fetchone()
    id_li=id_livre[0]
    curseur.execute("UPDATE emprunts SET date_retour=CURRENT_TIMESTAMP WHERE id_livre=? AND date_retour IS NULL", (id_li,))
    conn.commit()
    print("operation reussie")
def livre_emprunte():
    curseur.execute("SELECT titre FROM livre JOIN emprunts ON livre.id=emprunts.id_livre WHERE date_retour IS NULL")
    d=curseur.fetchall()
    if d is None:
        print("aucun livre n'est emprunte")
    else:
        print("les livres empruntes sont: ")
        for livre in d:
            print(livre[0])
def liste_auteurs():
    auteur=input("entrer le nom de l'auteur: ")
    curseur.execute("SELECT titre from livre WHERE auteur=? ", (auteur,))
    d=curseur.fetchall()
    if d is None:
        print("auteur n'existe pas")
    else:
        print("l'auteur ", auteur, "a les livres suivants: ")
        for livre in d:
            print(livre[0])
while True:
    menue()
    choix=int(input("entrer votre choix : "))
    match choix:
        case 1:
            ajouter_livre()
        case 2:
            emprunt_livre()
        case 3:
            retourner_livre()
        case 4:
            livre_emprunte()
        case 5:
            liste_auteurs()
        case 6:
            print("vous avez quittez la base")
            break

