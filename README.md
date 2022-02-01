#Projet 12 OC

##Comment tester le projet ?
1. Clonez ce repo en local
2. Démarrez un environnement virtuel puis installer les dépendances du projet Django
```bash
#Activation de l'environnement virtuel
python3 -m venv env
source env/bin/activate

# Installation des dépendances
pip install -r requirements.txt
```bash
3. Renommez le fichier `edit.env` en `.env` afin que les variables d'environnement soient chargées sur votre machine grâce au module Python Dotenv. Vous pouvez en profiter pour personnaliser le nom de la db, de l'username ou du password postgreSQL à utiliser.
```

3. Lancez en local Postgresql sur votre machine.
```bash
sudo -i -u postgres
```
Vous devriez voir apparaitre la commande suivante à l'écran : 
```bash
postgres@your-devid-name: $ ...
```
Il ne vous reste plus qu'à créer la db correspondant au nom dans le fichier .env : (par défaut : proj12oc)
```bash
postgres@your-devid-name: $ `createdb proj12oc`
```

4. Lancez le serveur Django
```bash
python manage.py runserver
```

