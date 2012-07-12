Uvod u git
==========

Kako pokrenuti cijelu skalameriju?
==================================

Potrebno je instalirati LaTeX i python.

Varijanta1 s vim editorom. Pokrenuti bin/edit, kliknuti redom F3 (reload git output latex fajlova), F2 (reload latex grafova), F1 (LaTeX compile) i F4 (Pokreće viewer).

Varijanta2 iz komandne linije:

    python create_git_outputs.py
    python create_graphs.py
    pdflatex git.tex
    evince git.pdf &
    # ...ili bilo koji drugi pdf viewer

Nakon toga je dovoljno samo:

    # Ako su izmijenjeni git_output txt fajlovi u git_output/
    python create_git_outputs.py
    # Ako su izmijenjene skripte za grafove u graphs/
    python create_graphs.py
    pdflatex git.tex

...i viewer bi se sam treba osvježiti (ako se koristi evince).
