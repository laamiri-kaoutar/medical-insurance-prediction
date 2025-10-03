# Projet : Prédiction des Charges d'Assurance Maladie

## Description du Projet

Ce projet développe un modèle de régression pour prédire les charges à payer à l'assurance maladie avec une haute précision. L’objectif est de fournir une solution rapide, fiable et accessible aux utilisateurs afin de les aider à anticiper leurs dépenses de santé et à mieux planifier leur budget.

Le modèle final sélectionné est le **XGBoost Regressor optimisé**, choisi pour ses performances supérieures ($R^2$, RMSE) et sa bonne robustesse (MAE).

Les critères utilisés pour la prédiction incluent : l'âge, le sexe, l'indice de masse corporelle (BMI), le nombre d’enfants à charge, l'habitude tabagique, et la région géographique.

## Structure des Fichiers

| Fichier/Dossier | Description |
| :--- | :--- |
| `assurance_maladie.csv` | Le jeu de données initial du projet. |
| `data_traitement.ipynb` | **Notebook principal.** Contient toutes les étapes d'analyse des données (EDA), de prétraitement, d'entraînement des modèles, d'optimisation (GridSearch), d'évaluation, et de sélection du modèle final. |
| `xgb_model_joblib` | Le modèle de **XGBRegressor optimisé** et entraîné, exporté au format `joblib` pour la réutilisation et la prédiction. |
| `app.py` | Fichier Python pour l'exécution du modèle chargé (`xgb_model_joblib`) et la saisie des données utilisateur pour la prédiction. |
| `README.md` | Ce fichier de documentation du projet. |

## Instructions pour l’Exécuter

Pour reproduire l'analyse ou exécuter le modèle de prédiction.

### 1. Prérequis (Installation)

Installez les bibliothèques Python requises, y compris Scikit-learn, XGBoost, Pandas et NumPy :

```bash
pip install pandas numpy scikit-learn xgboost joblib matplotlib
````

### 2\. Analyse et Entraînement

Pour reproduire l'analyse complète (EDA, prétraitement, entraînement et optimisation des modèles) :

1.  Ouvrez le fichier `data_traitement.ipynb` (idéalement dans VS Code, Jupyter ou Colab).
2.  Exécutez toutes les cellules du notebook séquentiellement. Le notebook générera et sauvegardera le modèle final dans le fichier `xgb_model_joblib`.

### 3\. Exécution de la Prédiction

Pour effectuer une prédiction avec le modèle final :

1.  Assurez-vous que le modèle entraîné (`xgb_model_joblib`) est présent dans le même répertoire que `app.py`.

2.  Exécutez le script `app.py` dans votre terminal :

    ```bash
    python app.py
    ```

3.  Le programme vous demandera d'entrer les six variables requises (âge, BMI, nombre d'enfants, sexe, fumeur, région) et affichera la charge d'assurance maladie estimée.


```
```