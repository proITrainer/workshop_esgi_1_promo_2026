"""
_preview.py - Aperçu LOCAL du site (sans Ruby/Jekyll).

Ce script émule le rendu Jekyll : il lit les fiches de _promo/, applique la même
structure HTML que _layouts/default.html + index.html et la même feuille de style,
puis écrit _preview.html (ouvrable directement dans un navigateur).

C'est UNIQUEMENT un outil de vérification visuelle. Le vrai site est construit
par GitHub Pages. _preview.html et ce script sont exclus de la publication.

    python _preview.py
"""
from pathlib import Path

HERE = Path(__file__).parent


def lire_fiche(chemin: Path):
    texte = chemin.read_text(encoding="utf-8")
    meta, corps = {}, ""
    if texte.startswith("---"):
        _, fm, corps = texte.split("---", 2)
        for ligne in fm.splitlines():
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or ":" not in ligne:
                continue
            cle, val = ligne.split(":", 1)
            meta[cle.strip()] = val.strip().strip('"').strip("'")
    return meta, corps.strip()


def carte(meta, corps):
    prenom = meta.get("prenom", "")
    nom = meta.get("nom", "")
    photo = meta.get("photo", "")
    objectif = meta.get("objectif", "")
    fun = meta.get("fun_fact", "")
    github = meta.get("github", "")
    if photo:
        avatar = f'<img src="photos/{photo}" alt="{prenom} {nom}">'
    else:
        initiales = (prenom[:1] + nom[:1]).upper()
        avatar = f'<span class="initiales">{initiales}</span>'
    html = ['<article class="carte">',
            '<div class="carte-entete"></div>',
            f'<div class="avatar">{avatar}</div>',
            '<div class="carte-corps">',
            f'<h3>{prenom} {nom}</h3>']
    if objectif:
        html.append(f'<p class="objectif">{objectif}</p>')
    if corps:
        html.append(f'<p class="bio">{corps}</p>')
    if fun:
        html.append(f'<p class="fun"><span>Fun fact</span> {fun}</p>')
    if github:
        html.append(f'<a class="lien" href="https://github.com/{github}">GitHub &rarr; {github}</a>')
    html.append('</div></article>')
    return "\n".join(html)


def main():
    fiches = sorted(p for p in (HERE / "_promo").glob("*.md")
                    if "TEMPLATE" not in p.name)
    cartes = []
    for f in sorted(fiches, key=lambda p: lire_fiche(p)[0].get("nom", "")):
        meta, corps = lire_fiche(f)
        cartes.append(carte(meta, corps))

    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Aperçu - Trombinoscope</title>
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="bandeau">
  <div class="logos">
    <img class="logo" src="assets/img/skolae-rouen.png" alt="Campus Skolae Rouen">
    <img class="logo" src="assets/img/esgi.jpg" alt="ESGI">
  </div>
  <div class="titres">
    <h1>Promo 2025 - 1re année Cybersécurité</h1>
    <p>Semaine d'intégration &middot; Détection de phishing par IA</p>
  </div>
</header>
<main class="conteneur">
  <section class="intro">
    <h2>Notre promo</h2>
    <p>Chaque étudiant a créé sa fiche pendant la semaine d'intégration.</p>
  </section>
  <section class="grille">
    {''.join(cartes)}
  </section>
</main>
<footer class="pied">
  <div class="logos-pied">
    <img class="logo-pied" src="assets/img/skolae-rouen.png" alt="Campus Skolae Rouen">
    <img class="logo-pied" src="assets/img/esgi.jpg" alt="ESGI">
  </div>
  <p>ESGI &middot; Campus Skolae Rouen &middot; Semaine d'intégration</p>
</footer>
</body>
</html>"""
    out = HERE / "_preview.html"
    out.write_text(page, encoding="utf-8")
    print("Aperçu écrit :", out.name, "(", len(fiches), "fiches )")


if __name__ == "__main__":
    main()
