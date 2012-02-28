#!/usr/bin/python
# -*- coding: utf-8 -*-

def get_latex_arrow( node1, node2 ):
	return '\\thicklines {\\color[rgb]{0,0,0}\\put(50,0){\\vector(1,0){340}}}\n'

class Node:
	
	text = None

	def __init__( self, text ):
		self.text = text

	def to_latex_string( self ):
		result = '\\put(-50,140){\\makebox(0,0)[lb]{\\smash{{\\SetFigFont{12}{14.4}{\\rmdefault}{\\mddefault}{\\updefault}{\\textit{a}}}}}}\n'
		result += '{\\color[rgb]{0,0,0}\\put(0,0){\\circle*{150}}}\n'

		return result

class Branch:

	title = None

	__nodes = None

	def __init__( self, title = None, start_node = None ):
		self.title = title
		self.__nodes = []

	def add_node( self, node ):
		self.__nodes.append( node )

	def get_node( self, index ):
		return self.__nodes[ index ]

	def to_latex_string( self ):
		result = ''

		for index, node in enumerate( self.__nodes ):
			result += node.to_latex_string()
			if index < len( self.__nodes ) - 1:
				next_node = self.__nodes[ index + 1 ]
				result += get_latex_arrow( node, next_node )

		return result

class Graph:

	__branches = None

	def __init__( self ):
		self.__branches = []

	def add_branch( self, branch ):
		self.__branches.append( branch )

	def get_branch( self, index ):
		return self.__branches[ index ]

	def to_latex_string( self ):
		result = '\\setlength{\\unitlength}{4144sp}%\n'
		result += '\\begingroup\\makeatletter\\ifx\\SetFigFont\\undefined%\n'
		result += '\\gdef\\SetFigFont#1#2#3#4#5{%\n'
		result += '  \\reset@font\\fontsize{#1}{#2pt}%\n'
		result += '  \\fontfamily{#3}\\fontseries{#4}\\fontshape{#5}%\n'
		result += '  \\selectfont}%\n'
		result += '\\fi\\endgroup%\n'
		result += '\\begin{picture}(2455,634)(0,0)\n'

		for branch in self.__branches:
			result += branch.to_latex_string()

		return result

if __name__ == '__main__':
	graph = Graph()

	master_branch = Branch( title = 'master' )
	master_branch.add_node( Node( 'a' ) )
	master_branch.add_node( Node( 'b' ) )
	master_branch.add_node( Node( 'c' ) )
	graph.add_branch( master_branch )

	branch1 = Branch( title = 'experiment', start_node = master_branch.get_node( 1 ) )
	master_branch.add_node( Node( 'x' ) )
	master_branch.add_node( Node( 'y' ) )
	master_branch.add_node( Node( 'z' ) )
	graph.add_branch( branch1 )

	print graph.to_latex_string()

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
