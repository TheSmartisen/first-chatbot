# 🤖 Chatbot IA avec Gradio & Hugging Face

[Chatbot CI/CD](https://github.com/TheSmartisen/first-chatbot/actions)

🚀 **Chatbot IA** interactif utilisant **Gradio** pour l'interface et **Hugging Face Transformers** pour la traduction et la génération de texte. Ce projet intègre également des tests automatisés avec **GitHub Actions**.

---

## 🛠️ **Technologies Utilisées**
- **Python 3.10+**
- **Hugging Face Transformers** (modèles de traduction et chatbot)
- **Gradio** (interface utilisateur)
- **Pytest** (tests unitaires)
- **GitHub Actions** (CI/CD)

---

## ⚙️ **Installation**
### 1️⃣ **Cloner le dépôt**
```bash
git clone https://github.com/TON-UTILISATEUR/first-chatbot.git
cd first-chatbot
```

### 2️⃣ **Créer et activer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Configurer le Token Hugging Face**
1. **Créer un compte** sur [Hugging Face](https://huggingface.co/).
2. **Générer un Token API** sur [Settings > Tokens](https://huggingface.co/settings/tokens).
3. **Créer un fichier `.env` et ajouter :**
```ini
HF_TOKEN_KEY=hf_xxxxxxxxxxxxxxxxx
```

---

## 🚀 **Lancer le Chatbot**
```bash
python app.py
```
L'interface sera accessible sur **`http://127.0.0.1:7860/`**.

---

## ✅ **Exécuter les tests unitaires**
```bash
pytest tests/
```

---

## 🔧 **Structure du Projet**
```
first-chatbot/
│── .github/workflows/chatbot.yml  # CI/CD avec GitHub Actions
│── app.py                          # Interface Gradio
│── config.py                        # Configuration (Token, etc.)
│── models.py                        # Chargement des modèles IA
│── utils.py                         # Fonctions utilitaires (traduction)
│── requirements.txt                  # Dépendances
│── tests/                           # Dossier des tests unitaires
│   ├── test_config.py                # Test de la configuration
│── README.md                         # Documentation du projet
```

---

## 🛠️ **Contribuer au Projet**
Tu veux **ajouter une fonctionnalité** ou **corriger un bug** ?  
1. **Fork** le projet 🍴  
2. **Crée une branche** : `git checkout -b feature/ma-feature`  
3. **Ajoute tes modifications** : `git commit -m "Ajout de ma feature"`  
4. **Pousse la branche** : `git push origin feature/ma-feature`  
5. **Crée une Pull Request** 🛠️  

---

## 📄 **Licence**
Projet sous licence **MIT** – Fais-en bon usage ! 🎉
