# TrustCheck

**TrustCheck – Modération intelligente de contenus Internet**

TrustCheck est une application web légère qui utilise l'intelligence artificielle pour la **modération de contenus** sur Internet. Elle détecte automatiquement les **textes haineux ou offensants** et les **images à caractère sexuel ou inapproprié** afin de garantir des environnements numériques plus sûrs.

---

## 🛠️ Fonctionnalités

### Modules IA

* **trustTest** : Analyse les textes et détecte les contenus haineux, offensants ou inappropriés.
* **trustVision** : Analyse les images et identifie les contenus à caractère sexuel ou explicite.

### Application Web

* Interface web simple avec **Flask**.
* Permet de tester directement vos textes et images.
* Résultats avec score de confiance et classification instantanée.

---

## 💻 Installation

1. **Cloner le dépôt**

```bash
git clone https://github.com/<votre-utilisateur>/TrustCheck.git
cd TrustCheck
```

2. **Créer un environnement virtuel et installer les dépendances**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **Lancer l’application**

```bash
python app.py
```

4. **Accéder à l’interface**
   Ouvrir votre navigateur à l’adresse : `http://127.0.0.1:5000`

---





## ⚡ Exemple d’utilisation

**Pour trustTest (texte)**

```python
from models.trustTest import predict_text
result = predict_text("Ton texte ici")
print(result)  # Retourne : {'label': 'haineux', 'score': 0.92}
```

**Pour trustVision (image)**

```python
from models.trustVision import predict_image
result = predict_image("chemin/vers/image.jpg")
print(result)  # Retourne : {'label': 'inapproprié', 'score': 0.88}
```

---

## 📝 Contribution

Les contributions sont les bienvenues !

* Fork le projet
* Crée ta branche (`git checkout -b feature/nom`)
* Commit tes changements (`git commit -m 'Ajout d'une fonctionnalité'`)
* Push ta branche (`git push origin feature/nom`)
* Ouvre une Pull Request

---


## 🔗 Liens utiles

* [Documentation Flask](https://flask.palletsprojects.com/)
* [GitHub](https://github.com/hkdebendo/trust-check)
