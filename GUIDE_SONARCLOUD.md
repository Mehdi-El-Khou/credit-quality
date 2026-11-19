# Guide SonarQube Cloud — étapes à faire sur votre compte

Ces étapes nécessitent **votre compte GitHub**. Une fois faites, on pourra lancer l’analyse.

## 1. Créer le dépôt GitHub

1. Aller sur https://github.com/new
2. Nom du dépôt : `credit-quality`
3. Créer le dépôt (Public ou Private)

## 2. Créer / connecter le projet sur SonarQube Cloud

1. Aller sur https://sonarcloud.io
2. Se connecter avec GitHub
3. Créer ou sélectionner une organisation
4. Importer le dépôt `credit-quality`
5. Noter :
   - **Project Key**
   - **Organization Key**
   - **Token d’analyse** (générer un token si demandé)

## 3. Remplir `sonar-project.properties`

Remplacer dans le fichier :

```properties
sonar.projectKey=VOTRE_PROJECT_KEY
sonar.organization=VOTRE_ORGANIZATION_KEY
```

## 4. Lancer l’analyse (PowerShell)

```powershell
cd "c:\Users\mehdi\OneDrive\Desktop\TP deploiement\credit_quality"

$env:SONAR_TOKEN = "VOTRE_TOKEN"
$env:Path += ";C:\outils\sonarscanner\bin"

# Analyse AVEC le code défectueux (avant) :
# 1) remplacez temporairement credit.py par credit_avant_correction.py
# 2) lancez :
sonar-scanner -Dsonar.host.url=https://sonarcloud.io

# Puis après correction (credit.py actuel) :
sonar-scanner -Dsonar.host.url=https://sonarcloud.io
```

## 5. Captures d’écran à prendre

1. Dashboard SonarQube **avant** correction  
2. Dashboard SonarQube **après** correction  
3. Panneau Problems / SonarQube for IDE dans l’éditeur  

Placez-les dans le dossier `livrables/captures/`.

## 6. Extension SonarQube for IDE

1. Extensions → chercher **SonarQube for IDE** (SonarSource)  
2. Installer  
3. Ouvrir `credit.py` / `credit_avant_correction.py`  
4. Voir les problèmes dans Problems  
5. (Optionnel) Connecter au projet Cloud  
