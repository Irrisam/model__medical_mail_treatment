#  curl -X POST "http://localhost:8888/classify" \
# -H "Content-Type: application/json" \
# -d "{\"subject\":\"RE: URGENT TR: stage 5.3 amendment 1\",\"body\":\"Hello Lauriane,\r\n\r\n \r\n\r\nN/R�f. : MQ.G2M.010.FR - Demande d'enregistrement de marque semi-figurative fran�aise \"LAGO\" d�pos�e le 8 avril 2025 sous le n�5137082 en classes 10 et 12 - Avis de publication\",\"body\":\"Bonjour Monsieur Lainard,\r\n\r\n \r\n\r\nDans le cadre de la proc�dure d�enregistrement de la marque en r�f�rence, nous vous informons que celle-ci a �t� publi�e par l�INPI en date du 2 mai 2025. Vous trouverez, ci-joint, copie de cette publication.\r\n\r\n \r\n\r\nCette date de publication ouvre un d�lai de deux mois � l�int�rieur duquel tout tiers peut engager une proc�dure d�opposition � l�encontre de l�enregistrement de votre marque. Pass� ce d�lai, si aucune opposition n�est d�pos�e, le certificat d�enregistrement de la marque sera �mis.\r\n\r\n \r\n\r\nNous reviendrons prochainement sur ce dossier pour vous tenir inform� de son �volution. \r\n\r\n \r\n\r\nBien cordialement.\r\n\r\n \r\n\r\nP.J. : avis de publication\r\n\r\n\r\n \r\n\r\nPascale Comm�re\r\n\r\nService Paral�gal Marques\r\n\r\n \r\n\r\n <http://www.aquinov.fr/> \r\n\r\n \r\n\r\n12 cours Xavier Arnozan\r\n\r\n33000 Bordeaux\r\n\r\nT�l : (33) 05.57.54.47.19\r\n\r\nE-mail : p.commere@aquinov.fr <mailto:p.commere@aquinov.fr>  \r\n\r\nSite : www.aquinov.fr <http://www.aquinov.fr/> \r\n\r\nLien de paiement en ligne : PAIEMENT EN LIGNE <https://paiement-aquinov.fr/RRx2M> \r\n\r\n <https://www.facebook.com/pages/AQUINOV/115108781903706> \r\n\r\n--------------------------------------------------------------\r\n\r\nCe message et toutes les pi�ces jointes (ci-apr�s le � message) sont confidentiels et �tablis � l�intention exclusive de ses destinataires. Toute utilisation ou diffusion non autoris�e est interdite. Tout message �lectronique est susceptible d�alt�ration. AQUINOV d�cline toute responsabilit� au titre de "}"

import os

folder = "mails_json"  # 📌 chemin du dossier racine

for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith(".txt"):
            old_path = os.path.join(root, filename)
            new_path = os.path.join(root, filename[:-4] + ".json")
            os.rename(old_path, new_path)

print("Renommage récursif terminé ✅")