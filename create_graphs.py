#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys as mod_sys

mod_sys.path.append( 'submodules/vcgraphtex' )

import vcgraphtex as mod_graph

RED = ( 1, 0, 0 )
GREEN = ( 0, 1, 0 )
BLUE = ( 0, 0, 1 )
GRAY = ( .6, .6, .6 )

def graph_primjer_s_klijentom():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = [ '0.1', '0.2', '...', '0.8', '0.9', '1.0', '1.1' ] ) )

	graph.add_branch( mod_graph.Branch(
			branch_from = graph.find_node( '1.0' ),
			color = GRAY,
			row = 1,
			nodes = [ '1.1\'', '1.2\'' ] ) )

	return graph

def graph_linearni_model():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = [ 'a', 'b', 'c', 'd', 'e', '1.0', 'f', 'g', 'h', 'i', '2.0', '...' ] ) )

	return graph

def graph_linearni_model_2():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = [ 'a', 'b', 'c', 'd', 'e', '1.0', 'f', 'g', 'h', 'i', '2.0', '...' ] ) )

	graph.add_branch(
		mod_graph.Branch(
			row = 1,
			nodes = [ 'x', 'y', '1.1' ],
			color = GRAY,
			branch_from = graph.find_node( '1.0' ) ) )

	graph.add_branch(
		mod_graph.Branch(
			row = 1,
			nodes = [ 'q', '2.1' ],
			color = GRAY,
			branch_from = graph.find_node( '2.0' ) ) )

	return graph

def graph_primjer_s_granama_i_spajanjima():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abcdefgh' ) )

	graph.add_branch( mod_graph.Branch(
			row = 2,
			nodes = 'xyzqw',
			branch_from = graph.find_node( 'b' ) ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = '1234',
			branch_from = graph.find_node( 'g' ) ) )

	graph.add_arrow( 'd', 'z', color = GRAY )
	graph.add_arrow( 'q', 'g', color = GRAY )

	return graph

def graph_primjer_s_granama_i_spajanjima_1():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abc' ) )

	return graph

def graph_primjer_s_granama_i_spajanjima_2():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abc' ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = 'xy',
			branch_from = graph.find_node( 'b' ) ) )

	return graph

def graph_primjer_s_granama_i_spajanjima_3():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abcd' ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = 'xy',
			branch_from = graph.find_node( 'b' ) ) )

	return graph

def graph_primjer_s_granama_i_spajanjima_4():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abcdefgh' ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = 'xyz',
			branch_from = graph.find_node( 'b' ) ) )

	graph.add_arrow( 'd', 'z', color = GRAY )

	return graph

def graph_primjer_s_granama_i_spajanjima_5():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abcdef' ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = 'xyzq',
			branch_from = graph.find_node( 'b' ) ) )

	graph.add_arrow( 'd', 'z', color = GRAY )

	return graph

def graph_primjer_s_dugotrajnom_granom():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abcdefghijklmnopq' ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = '1234567890xyz',
			branch_from = graph.find_node( 'b' ) ) )

	graph.add_arrow( 'e', '4', color = GRAY )
	graph.add_arrow( 'h', '7', color = GRAY )
	graph.add_arrow( 'i', '8', color = GRAY )
	graph.add_arrow( 'l', 'x', color = GRAY )
	graph.add_arrow( 'n', 'z', color = GRAY )
	graph.add_arrow( 'z', 'p', color = RED )

	return graph

def graph_primjer_s_granama_i_spajanjima_6():
	graph = mod_graph.Graph()

	graph.add_branch( mod_graph.Branch(
			nodes = 'abcdefg' ) )

	graph.add_branch( mod_graph.Branch(
			row = 1,
			nodes = 'xyzq',
			branch_from = graph.find_node( 'b' ) ) )

	graph.add_arrow( 'd', 'z', color = GRAY )
	graph.add_arrow( 'q', 'g', color = GRAY )

	return graph

for v in vars().keys():
	if v.startswith( 'graph_' ):
		method = vars()[ v ]
		file_name = 'graphs/' + v.replace( 'graph_', '' ) + '.tex'

		graph = method()

		with file( file_name, 'w' ) as f:
			f.write( graph.get_latex_string() )
			print file_name, ' OK'
		
