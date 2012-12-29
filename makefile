build: init
	git log -1 --format=\\verb+%H+ > current_commit.tex
	
	mkdir -p graphs
	mkdir -p git_output
	
	python create_graphs.py
	python create_git_outputs.py
	
	# 2 puta da bi sadržaj bio ažuran:
	pdflatex git.tex
	pdflatex git.tex
	
	echo "git.pdf created"
init:
	# Za svaki slučaj, ako submodul nije inicijaliziran:
	git submodule init
	git submodule update
edit:
	gvim -U etc/vimrc &
clean:
	rm -f *.dvi *.log *.aux *.swp *.swo *.toc *.idx *.pdf
	rm -f graphs/*
random-page: build
	evince -p `python -c "import random as r;print r.randint(1,140)"` git.pdf
github-page: build
	cp git.pdf /tmp
	git checkout gh-pages
	cp /tmp/git.pdf .
	git add git.pdf
	git commit --amend -m "git.pdf"
	echo Now:       git push -f origin gh-pages
	echo And then:  git checkout master
