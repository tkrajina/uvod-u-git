#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys as mod_sys

mod_sys.path.append( 'submodules/vcgraphtex' )

import vcgraphtex as mod_graph

def graph_primjer_s_klijentom():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = [ '0.1', '0.2', '...', '0.8', '0.9', '1.0', '1.1' ] ) )

	graph.add_branch( mod_graph.Branch(
			branch_from = graph.find_node( '1.0' ),
			color = ( .5, .5, .5 ),
			row = 1,
			nodes = [ '1.1\'' ] ) )

	return graph

def graph_linearni_model():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch( nodes = 'abcdefgh' ) )

	return graph

def graph_primjer_s_granama_i_spajanjima():
	graph = mod_graph.Graph( column = 4 )

	graph.add_branch( mod_graph.Branch(
			label = 'master',
			nodes = 'abcdefgh' ) )

	graph.add_branch( mod_graph.Branch(
			label = 'zadatak-1',
			row = 2,
			nodes = 'xyzqw',
			color = ( 0, 0, 1 ),
			branch_from = graph.find_node( 'b' ) ) )

	graph.add_branch( mod_graph.Branch(
			label = 'eksperiment',
			row = 1,
			nodes = '1234',
			color = ( 1, 0, 0 ),
			branch_from = graph.find_node( 'g' ) ) )

	graph.add_arrow( 'd', 'z', color = ( 0, 1, 0 ) )
	graph.add_arrow( 'q', 'g' )

	return graph

for v in vars().keys():
	if v.startswith( 'graph_' ):
		method = vars()[ v ]
		file_name = 'graphs/' + v.replace( 'graph_', '' ) + '.tex'

		graph = method()

		with file( file_name, 'w' ) as f:
			f.write( graph.get_latex_string() )
			print file_name, ' OK'
		
