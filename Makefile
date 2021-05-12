# Use this makefile to produce the main pdf document of the paper. 
# Either "make" or "make all" will compile the document properly.
# "make view" will try to open the $(NAME).pdf with the default viewer
# "make clean" will clean up by-products.

NAME = polpars
BIBLIO = refs.bib

TEXFILES = $(NAME).tex

# Force latexmk to run always:
.PHONY: $(NAME).pdf all view clean

# make is make all by default (first rule in Makefile)
all: $(NAME).pdf

LATEXMK = latexmk -pdf -pdflatex
# LATEXMK = latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode"

view: $(NAME).pdf
	open $(NAME).pdf

$(NAME).pdf: $(TEXFILES) $(BIBLIO)
	$(LATEXMK) $(NAME).tex

nocomments: $(NAME).pdf
	pdflatex -shell-escape -halt-on-error -interaction=batchmode "\def\nocomments{1} \input{$(NAME).tex}"

clean: 
	latexmk -CA
	rm -f arxiv.tar prl.tar $(NAME).tar.gz $(NAME)Notes.bib $(NAME).auxlock subdirs submission-files
	rm -rf submission

arxiv: $(NAME).pdf 
	bash make-submission.sh

prl: $(NAME).pdf
	bash make-submission.sh
	cd submission && tar czvf prl.tar *.tex *.bbl -C fig . && cd .. && mv submission/prl.tar .

