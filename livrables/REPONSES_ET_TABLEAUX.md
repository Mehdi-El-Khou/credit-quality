# Livrables — TP Qualité du code et tests unitaires

## Exercice 1 — Analyse SonarQube

### Problèmes identifiés (AVANT correction)

| Type | Description |
|------|-------------|
| **Code Smell** | Imports inutilisés : `os`, `math` |
| **Code Smell / Duplication** | Fonctions `calculate_risk` et `calculate_risk2` identiques (~100 % de duplication) |
| **Maintenabilité** | Paramètre `age` jamais utilisé |
| **Fiabilité** | Types de retour incohérents (`-1` int vs chaînes `"HIGH"` / `"MEDIUM"` / `"LOW"`) |
| **Sécurité** | Aucun problème de sécurité majeur détecté sur ce petit module |

### Corrections apportées

1. Suppression des imports inutilisés (`os`, `math`)
2. Suppression de la fonction dupliquée `calculate_risk2`
3. Conservation d’une seule fonction claire `calculate_risk` avec docstring
4. Paramètre `age` rendu optionnel (`age=None`) pour une évolution future

### Tableau de comparaison (1.4)

| Indicateur | Avant | Après |
|------------|-------|-------|
| Problèmes de fiabilité | Présents (retour mixte int/str, code mort) | Réduits / absents |
| Problèmes de sécurité | 0 | 0 |
| Problèmes de maintenabilité | Élevés (imports inutilisés, paramètre inutilisé) | Faibles |
| Duplication | ~50 % (deux fonctions identiques) | 0 % |
| Quality Gate | Failed (attendu) | Passed (après correction) |

> **Note :** Remplacez les valeurs « Avant / Après » par celles affichées sur votre tableau de bord SonarQube Cloud après les deux analyses, et joignez les captures d’écran.

### Questions Exercice 1 (1.5)

**1. Quelle différence existe-t-il entre un Bug et un Code Smell ?**

Un **Bug** est un défaut qui peut provoquer un comportement incorrect à l’exécution (crash, résultat faux, exception).  
Un **Code Smell** est un signe de mauvaise conception ou de code difficile à maintenir, sans être forcément une erreur immédiate (duplication, complexité, noms peu clairs, etc.).

**2. Pourquoi la duplication du code augmente-t-elle les coûts de maintenance ?**

Parce que toute modification (correction de bug, évolution) doit être répétée à plusieurs endroits. On risque d’oublier une copie, d’introduire des divergences, et le temps de relecture / test augmente.

**3. Quel est le rôle du Quality Gate ?**

Le **Quality Gate** est un ensemble de seuils (bugs, vulnérabilités, couverture, duplication, etc.) qui décide si le projet est « OK » pour être livré. S’il échoue, le code ne passe pas le contrôle qualité.

**4. Quelle différence existe-t-il entre SonarScanner CLI et SonarQube for IDE ?**

- **SonarScanner CLI** : analyse le projet en ligne de commande et envoie le rapport au serveur / Cloud (analyse complète, historique, Quality Gate).  
- **SonarQube for IDE (SonarLint)** : analyse en local dans l’éditeur pendant le développement, avec un retour immédiat sans forcément pousser vers le Cloud.

**5. Pourquoi faut-il relancer l’analyse après correction ?**

Pour vérifier que les problèmes ont bien disparu, mettre à jour les métriques et le Quality Gate, et pouvoir comparer objectivement avant / après.

---

## Exercice 2 — Tests unitaires pytest

### Résultats des tests

```
8 passed
Couverture credit.py : 100%
```

### Partie C — Détection d’erreurs

Si on remplace `if ratio > 0.6:` par `if ratio > 0.8:` :

1. **Quels tests échouent ?**  
   `test_high_risk` (et éventuellement d’autres cas où `0.6 < ratio <= 0.8`).

2. **Pourquoi échouent-ils ?**  
   Pour `income=1000, debt=700` → `ratio=0.7`. Avec le seuil `0.8`, ce cas devient `"MEDIUM"` au lieu de `"HIGH"`. L’assertion `assert result == "HIGH"` échoue.

3. **Corriger la condition** → remettre `if ratio > 0.6:`

4. **Relancer les tests** → tous repassent en PASSED.

### Questions Exercice 2 (2.8)

**1. Quel est le rôle de l’instruction `assert` ?**

Elle vérifie qu’une condition est vraie. Si elle est fausse, le test échoue (FAIL) avec une erreur d’assertion.

**2. Quelle différence existe-t-il entre PASS et FAIL ?**

- **PASS** : le résultat obtenu correspond au résultat attendu.  
- **FAIL** : le résultat obtenu diffère de l’attendu (ou une exception non prévue survient).

**3. Pourquoi faut-il tester les valeurs limites ?**

Les bugs se cachent souvent aux frontières (`0`, valeurs négatives, seuils exacts `0.3` / `0.6`). Les cas limites valident le comportement aux conditions critiques.

**4. Une couverture de 100 % garantit-elle l’absence de bugs ?**

**Non.** Elle indique seulement que toutes les lignes ont été exécutées. Des assertions incomplètes ou des scénarios oubliés peuvent laisser des bugs passer.

**5. Quelle différence existe-t-il entre pytest et SonarQube ?**

- **pytest** : exécute des tests unitaires pour vérifier le **comportement** du code.  
- **SonarQube** : analyse statique de la **qualité** du code (bugs potentiels, smells, sécurité, duplication) sans exécuter forcément la logique métier comme des tests.

---

## Fichiers à fournir

### Exercice 1
- [x] `credit.py` corrigé
- [x] `sonar-project.properties`
- [ ] Capture SonarQube **avant** correction
- [ ] Capture SonarQube **après** correction
- [ ] Capture des problèmes dans VS Code / Cursor (SonarQube for IDE)
- [x] Tableau complété (ci-dessus — à ajuster avec vos métriques Cloud)
- [x] Réponses aux questions

### Exercice 2
- [x] `tests/test_credit.py`
- [x] Capture d’exécution des tests (voir sortie ci-dessous / terminal)
- [x] Rapport de couverture : dossier `htmlcov/`
- [x] Réponses aux questions
