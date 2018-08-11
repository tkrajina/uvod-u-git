pdf_pages=$(shell pdfinfo "git.pdf" | grep "Pages" | sed -e "s/[^0-9]*//")
# Uz docker image s: https://gist.github.com/tkrajina/1b12fcc6c48fb3e582ac803a9f517146
pdflatex_cmd=docker run -v $(shell pwd):/latex -it latex pdflatex
#pdflatex_cmd=pdflatex

build: init
	git log -1 --format=\\verb+%H+ > current_commit.tex
	
	mkdir -p graphs
	mkdir -p git_output
	
	python create_graphs.py
	python create_git_outputs.py
	
	# 2 puta da bi sadržaj bio ažuran:
	$(pdflatex_cmd) git.tex
	$(pdflatex_cmd) git.tex
	
	echo "git.pdf created"
init:
	# Za svaki slučaj, ako submodul nije inicijaliziran:
	git submodule init
	git submodule update
clean:
	rm -f *.dvi *.log *.aux *.swp *.swo *.toc *.idx *.pdf
	rm -f graphs/*
show: build
	evince git.pdf &
random-page: build
	evince -p `python -c "import random as r;print r.randint(1,$(pdf_pages))"` git.pdf &
github-page: build
	cp git.pdf /tmp
	git checkout gh-pages
	cp /tmp/git.pdf .
	git add git.pdf
	git commit --amend -m "git.pdf"
	git push -f origin gh-pages
	git checkout master
