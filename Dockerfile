# Build:
#    docker build -t latex .
# Run latex:
#   docker run -v $(pwd):/latex -it latex pdflatex git.tex
#   docker run -v $(pwd):/latex -it /bin/bash
FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get -y install texlive-latex-base texlive-lang-european
WORKDIR /latex
CMD ["/bin/bash"]
