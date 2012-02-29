#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging as mod_logging
import math as mod_math

NODE_RADIUS = 150

def distance( x1, y1, x2, y2 ):
	return mod_math.sqrt( ( x2 - x1 ) ** 2 + ( y2 - y1 ) ** 2 )

def get_latex_arrow( node1, node2 ):
	x1 = node1.x
	y1 = node1.y
	x2 = node2.x
	y2 = node2.y
	node_distance = distance( x1, y1, x2, y2 )
	length = node_distance - NODE_RADIUS - 50
	return '\\thicklines {\\color[rgb]{0,0,0}\\put(' + str( x1 + 50 ) + ',' + str( y1 ) + '){\\vector(1,0){' + str( length ) + '}}}%\n'

class Node:
	
	text = None

	# x and y will be set only at the moment the LaTeX string is built:
	x = None
	y = None

	def __init__( self, text ):
		self.text = text
		self.x = None
		self.y = None

	def to_latex_string( self, x, y ):
		self.x = x
		self.y = y

		mod_logging.debug( 'Node at {0}, {0}'.format( x, y ) )

		result = '\\put(' + str( x - 50 ) + ',' + str( y + 140 ) + '){\\makebox(0,0)[lb]{\\smash{{\\SetFigFont{12}{14.4}{\\rmdefault}{\\mddefault}{\\updefault}{\\textit{' + self.text + '}}}}}}%\n'
		result += '{\\color[rgb]{0,0,0}\\put(' + str( x ) + ',' + str( y ) + '){\\circle*{' + str( NODE_RADIUS ) + '}}}%\n'

		return result

class Branch:

	title = None

	__nodes = None

	start_node = None

	def __init__( self, title = None, start_node = None ):
		self.title = title
		self.__nodes = []
		self.start_node = start_node

	def add_node( self, node ):
		self.__nodes.append( node )

	def get_node( self, index ):
		return self.__nodes[ index ]

	def to_latex_string( self, y ):
		result = ''

		mod_logging.debug( 'Branch starting at {0}'.format( y ) )

		if self.start_node:
			start_x = self.start_node.x
		else:
			start_x = 0
		start_y = y

		# Nodes:
		for index, node in enumerate( self.__nodes ):
			result += node.to_latex_string( x = start_x + index * 500, y = start_y )

		#Arrows
		for index, node in enumerate( self.__nodes ):
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
		width = 2000
		height = len( self.__branches ) * 500

		result = '\\setlength{\\unitlength}{4144sp}%\n'
		result += '\\begingroup\\makeatletter\\ifx\\SetFigFont\\undefined%\n'
		result += '\\gdef\\SetFigFont#1#2#3#4#5{%\n'
		result += '  \\reset@font\\fontsize{#1}{#2pt}%\n'
		result += '  \\fontfamily{#3}\\fontseries{#4}\\fontshape{#5}%\n'
		result += '  \\selectfont}%\n'
		result += '\\fi\\endgroup%\n'
		result += '\\begin{picture}(' + str( width ) + ',' + str( height ) + ')(0,0)%\n'

		start_y = height

		for index, branch in enumerate( self.__branches ):
			result += branch.to_latex_string( y = start_y - index * 500 )

		result += '\\end{picture}\n'

		return result

if __name__ == '__main__':
	mod_logging.basicConfig( level = mod_logging.DEBUG, format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s' )

	graph = Graph()

	master_branch = Branch( title = 'master' )
	master_branch.add_node( Node( 'a' ) )
	master_branch.add_node( Node( 'b' ) )
	master_branch.add_node( Node( 'c' ) )
	master_branch.add_node( Node( 'd' ) )
	graph.add_branch( master_branch )

	branch1 = Branch( title = 'experiment', start_node = master_branch.get_node( 1 ) )
	branch1.add_node( Node( 'x' ) )
	branch1.add_node( Node( 'y' ) )
	branch1.add_node( Node( 'z' ) )
	graph.add_branch( branch1 )

	branch2 = Branch( title = 'experiment', start_node = branch1.get_node( 2 ) )
	branch2.add_node( Node( 'š' ) )
	branch2.add_node( Node( 'č' ) )
	branch2.add_node( Node( 'ć' ) )
	graph.add_branch( branch2 )

	print """\\documentclass[11pt,oneside,a4paper]{report}

\\linespread{1.2}

\\title{test fig}

\\usepackage[dvips]{color}
\\usepackage[croatian]{babel}
\\usepackage[utf8]{inputenc}
\\usepackage{epsfig}
\\usepackage{makeidx}

\\addtolength{\\hoffset}{-1cm}
\\addtolength{\\voffset}{-3cm}
\\addtolength{\\textwidth}{3cm}
\\addtolength{\\textheight}{4cm}
\\pagestyle{empty}

\\begin{document}
"""

	print graph.to_latex_string()

	print 'OK'

	print "\\end{document}"


"""
\setlength{\unitlength}{4144sp}%
\begingroup\makeatletter\ifx\SetFigFont\undefined%
\gdef\SetFigFont#1#2#3#4#5{%
  \reset@font\fontsize{#1}{#2pt}%
  \fontfamily{#3}\fontseries{#4}\fontshape{#5}%
  \selectfont}%
\fi\endgroup%
\begin{picture}(2000,2000)(0,0)

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
