init:
	# Za svaki slučaj, ako submodul nije inicijaliziran:
	git submodule init
	git submodule update
build:
	git log -1 --format=\\verb+%H+ > current_commit.tex
	
	mkdir -p graphs
	mkdir -p git_output
	
	python create_graphs.py
	python create_git_outputs.py
	
	# 2 puta da bi sadržaj bio ažuran:
	pdflatex git.tex
	pdflatex git.tex
	
	echo "git.pdf created"
edit:
	gvim -U etc/vimrc $@ &
clean:
	rm -f *.dvi *.log *.aux *.swp *.swo *.toc *.idx *.pdf
	rm -f graphs/*
