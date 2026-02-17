import sqlite3
conn=sqlite3.connect('livre.db')
curseur=conn.cursor()
curseur.execute("PRAGMA foreign_keys=ON")
curseur.execute("CREATE TABLE IF NOT EXISTS livre(id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT NOT NULL, auteur TEXT NOT NULL, annee INTEGER NOT NULL CHECK (typeof(annee)='integer'))")
curseur.execute("CREATE TABLE IF NOT EXISTS emprunts(id INTEGER PRIMARY KEY AUTOINCREMENT,id_livre INTEGER,date_emprunt DATETIME,date_retour DATETIME, FOREIGN KEY(id_livre) REFERENCES livre(id) )")
curseur.execute("SELECT name FROM sqlite_master WHERE type='table';")
conn.commit()
tables=curseur.fetchall()
# print(tables)
# try:
#     titre = input("entrer le titre du livre: ")
#     auteur = input("entrer l'auteur du livre: ")
#     annee = int(input("entrer l'annee du livre: "))
#     curseur.execute("INSERT INTO livre(titre, auteur, annee) VALUES(?,?,?)",(titre,auteur,annee))
#     conn.commit()
# except Exception as e:
#     print(f"l'erreur est : {e}")
#     conn.rollback()
# curseur.execute("SELECT * FROM livre")
# print(curseur.fetchall())
curseur.execute("INSERT INTO emprunts(date_emprunt, date_retour) VALUES(?,?)",("2-14-2026 13:00:00","2-15-2026 14:05:00"))
curseur.execute("INSERT INTO emprunts(date_emprunt, date_retour) VALUES(?,?)",("1-14-2026 13:00:00","2-15-2026 14:05:00"))
curseur.execute("INSERT INTO emprunts(date_emprunt, date_retour) VALUES(?,?)",("2-14-2026 13:00:00",None))
curseur.execute("SELECT livre.titre,livre.auteur FROM livre JOIN emprunts ON livre.id=emprunts.id_livre WHERE emprunts.id_livre IS NOT NULL")
# nom=input("entrer le nom du livre: ")
# curseur.execute("SELECT id FROM livre WHERE titre=?",(nom,))
# n=curseur.fetchone()
# if n is None:
#     print("Livre n'existe pas")
# else:
#     id_livre=n[0]
#     curseur.execute("SELECT * FROM emprunts WHERE id_livre=? AND date_retour IS NULL",(id_livre,))
#     test=curseur.fetchone()
#     if test is None:
#         curseur.execute("INSERT INTO emprunts(id_livre, date_emprunt) VALUES(?,CURRENT_TIMESTAMP)",(id_livre,))
#         conn.commit()
#         print("livre emprunte")
#     else:
#         print("livre deja emprunte")
# id=int(input("entrer l'id du livre: "))
# nom=input("entrer le nom du livre que vous souhaitez rendre: ")
# curseur.execute("SELECT id FROM livre WHERE titre=?", (nom,))
# id_livre = curseur.fetchone()
# id_li=id_livre[0]
# curseur.execute("UPDATE emprunts SET date_retour=CURRENT_TIMESTAMP WHERE id_livre=? AND date_retour IS NULL",(id_li,))
# conn.commit()
# curseur.execute("SELECT id_livre FROM emprunts WHERE date_retour IS NULL")
# ids=curseur.fetchall()
# j=0
# for i in ids:
#     curseur.execute("SELECT titre FROM livre WHERE id=?",(i[j], ))
#     d=curseur.fetchone()
#     if d is not None:
#         print(d)
# curseur.execute("SELECT * from livre JOIN emprunts ON livre.id= emprunts.id_livre WHERE date_retour IS NULL ")
# conn.commit()
# d=curseur.fetchall()
# if d is None:
#     print("aucun livre emprunte")
# else:
#     print("les livres empruntes sont: ", d)
# auteur=input("entrer le nom du livre auteur: ")
# curseur.execute("SELECT * FROM livre WHERE auteur=?",(auteur, ))
# i=curseur.fetchall()
# if i:
#     for l in i:
#         print(l)
# else:
#     print("Aucun ecrit par cet auteur cet auteur")
conn.close()