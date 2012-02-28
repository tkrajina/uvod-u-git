#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node:
	
	text = None

	def __init__( self, text ):
		self.text = text

	def to_latex_string( self ):
		pass

class Branch:

	text = None

	__nodes = None

	def __init__( self, text ):
		self.text = text
		self.__nodes = []

	def to_latex_string( self ):
		pass

class Graph:

	__branches = None

	def __init__( self ):
		self.__branches = []

	def add_branch( self ):
		# Detect position

	def to_latex_string( self ):
		pass

if __name__ == '__main__':
	graph = Graph()

	branch1 = Branch()

"""
\setlength{\unitlength}{4144sp}%
\begingroup\makeatletter\ifx\SetFigFont\undefined%
\gdef\SetFigFont#1#2#3#4#5{%
  \reset@font\fontsize{#1}{#2pt}%
  \fontfamily{#3}\fontseries{#4}\fontshape{#5}%
  \selectfont}%
\fi\endgroup%
\begin{picture}(2455,634)(0,0)

\put(-50,140){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\textit{a}}}}}}
{\color[rgb]{0,0,0}\put(0,0){\circle*{150}}}
\thicklines {\color[rgb]{0,0,0}\put(50,0){\vector(1,0){340}}}
\put(450,140){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\textit{b}}}}}}
{\color[rgb]{0,0,0}\put(500,0){\circle*{150}}}
\thicklines {\color[rgb]{0,0,0}\put(550,0){\vector(1,0){340}}}
\put(950,140){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\textit{c}}}}}}
{\color[rgb]{0,0,0}\put(1000,0){\circle*{150}}}
\thicklines {\color[rgb]{0,0,0}\put(1050,0){\vector(1,0){340}}}
\put(1450,140){\makebox(0,0)[lb]{\smash{{\SetFigFont{12}{14.4}{\rmdefault}{\mddefault}{\updefault}{\textit{d}}}}}}
{\color[rgb]{0,0,0}\put(1500,0){\circle*{150}}}

\end{picture}

"""
