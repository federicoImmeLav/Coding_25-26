# 🐢 Esercizi Python con Turtle
## Come aprire ed eseguire gli esercizi

---

### ✅ Cosa ti serve
- Python 3 installato (scaricabile da python.org)
- La libreria `turtle` è già inclusa in Python, non serve installare nulla!

---

### ▶️ Come eseguire un esercizio

**Modo 1 – Da terminale/prompt:**
```
python esercizio_01_forme_base.py
```

**Modo 2 – Da IDLE (editor incluso in Python):**
1. Fai doppio click sul file `.py`
2. Premi F5 oppure vai su Run → Run Module

**Modo 3 – Da VS Code:**
1. Apri la cartella in VS Code
2. Apri il file `.py`
3. Premi il triangolino verde ▶ in alto a destra

---

### 📋 Elenco esercizi

| File | Titolo | Livello | Concetto |
|------|--------|---------|----------|
| esercizio_01_forme_base.py     | Le prime forme       | ⭐       | forward, right, pencolor |
| esercizio_02_cicli_poligoni.py | Cicli e poligoni     | ⭐⭐      | for range, 360/N |
| esercizio_03_fill_colori.py    | Fill e colori        | ⭐⭐      | begin_fill, end_fill, circle |
| esercizio_04_mandala.py        | Mandala colorato     | ⭐⭐⭐     | cicli + rotazioni + home() |
| esercizio_05_arte_generativa.py| Arte generativa      | ⭐⭐⭐     | cicli annidati, random |
| esercizio_06_clicca_cerchio.py | Clicca il cerchio!   | ⭐⭐⭐     | onclick, distance, global |
| esercizio_07_acchiappa_mela.py | Acchiappa la Mela!   | ⭐⭐⭐⭐    | onkey, ontimer, game loop |
| esercizio_08_evita_bombe.py    | Evita le Bombe!      | ⭐⭐⭐⭐    | liste, collisioni, restart |

---

### 💡 Consigli
- Leggi sempre tutti i commenti nel file prima di iniziare
- Cerca i commenti `# TODO` → sono quelli i punti dove scrivere!
- Apri il browser mentre lavori per cercare la documentazione
  di turtle: https://docs.python.org/3/library/turtle.html
- Se qualcosa non funziona, controlla i due punti `:` e l'indentazione

---

### 🔧 Errori comuni

| Errore | Causa probabile |
|--------|-----------------|
| `IndentationError` | Rientro (spazi) sbagliato |
| `NameError: name 'x' is not defined` | Hai dimenticato `global x` |
| La finestra si chiude subito | Manca `schermo.mainloop()` in fondo |
| Il disegno non compare | Hai `tracer(0)` ma manca `schermo.update()` |
