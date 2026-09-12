# Site de promo - Semaine d'intégration (ESGI / Campus Skolae Rouen)

Ce dossier contient un petit site web qui affiche la **fiche de chaque étudiant**
de la promo (un trombinoscope). C'est l'**activité brise-glace du Jour 1** : chacun
crée sa fiche, et le site rassemble tout le monde.

> **Bonne nouvelle : pas besoin de Git ni de ligne de commande pour le Jour 1.**
> Tout se fait **depuis le navigateur**, sur le site github.com. On verra Git plus
> tard dans la semaine.

---

## Pour l'enseignant : mettre le site en ligne (une seule fois)

1. Créer un compte / une organisation GitHub pour la promo.
2. Créer un dépôt (par ex. `workshop-esgi`) et y déposer le contenu de ce dossier `website/`.
   - Le plus simple pour publier sur `https://<compte>.github.io` : nommer le dépôt
     `<compte>.github.io` et laisser `baseurl: ""` dans `_config.yml`.
   - Pour un dépôt classique `workshop-esgi`, mettre `baseurl: "/workshop-esgi"` dans `_config.yml`.
3. Dans le dépôt : **Settings > Pages > Build and deployment > Source : "Deploy from a branch"**,
   choisir la branche `main` et le dossier `/ (root)`. Enregistrer.
4. Au bout d'une minute, le site est en ligne. Partager l'adresse aux étudiants.
5. Ajouter les étudiants comme **collaborateurs** (Settings > Collaborators) OU
   leur faire proposer leur fiche (voir plus bas).
6. Supprimer les fiches d'exemple (`_promo/exemple-*.md`) quand vous voulez.

---

## Ajouter ma fiche (étudiant) - 100 % dans le navigateur

1. Se connecter (ou créer un compte) sur [github.com](https://github.com).
2. Aller sur le dépôt du site (lien donné par l'enseignant).
3. Ouvrir le dossier **`_promo/`**, puis cliquer sur le fichier **`TEMPLATE.md`**.
4. Cliquer sur l'icône **crayon** (Edit), puis copier tout le contenu.
5. Revenir dans `_promo/`, cliquer sur **`Add file` > `Create new file`**.
6. Nommer le fichier avec **votre prénom et nom**, par exemple `marie-durand.md`.
7. Coller le contenu copié, puis **remplir vos informations** (prénom, nom,
   objectif, fun fact, petite présentation...).
8. En bas de la page, cliquer sur **`Commit changes`** (bouton vert).
9. C'est fait ! Votre fiche apparaîtra sur le site en une minute environ.

### (Facultatif) Ajouter une photo

1. Ouvrir le dossier **`photos/`** dans le dépôt.
2. **`Add file` > `Upload files`**, puis glisser votre photo (`prenom-nom.jpg`).
3. Dans votre fiche, mettre le nom du fichier dans le champ `photo:`
   (ex. `photo: "marie-durand.jpg"`).

> Si vous n'avez pas les droits d'écriture sur le dépôt, GitHub vous proposera
> automatiquement de créer une **"branche + Pull Request"** : validez, c'est normal,
> l'enseignant acceptera votre fiche. (On reparlera des Pull Requests plus tard !)

---

## Structure du site

| Fichier / dossier | Rôle |
| --- | --- |
| `_config.yml` | Réglages (nom de la promo, `baseurl`). |
| `index.html` | Page d'accueil : affiche la grille des fiches. |
| `_layouts/default.html` | Gabarit commun (en-tête co-brandé + pied de page). |
| `_promo/` | Une fiche `.md` par étudiant (+ `TEMPLATE.md`). |
| `photos/` | Les photos (facultatif). |
| `assets/css/style.css` | La charte graphique (couleurs ESGI + Skolae). |
| `assets/img/` | Les logos ESGI et Campus Skolae Rouen. |

## Aperçu local (facultatif, pour les curieux)

```bash
gem install bundler jekyll
jekyll serve
```

Puis ouvrir http://localhost:4000 . (Non nécessaire : GitHub Pages construit le
site tout seul.)
