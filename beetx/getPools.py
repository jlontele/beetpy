# import graph
import sys
import balpy.graph.graph as balGraph

def main():
	
	batch_size = 5;
	print();

	verbose = True;
	bg = balGraph.TheGraph(customUrl="https://graph.beethovenx.io/subgraphs/name/beethovenx")
	pools = bg.getV2Pools(batch_size, verbose=verbose)
	bg.printJson(pools)

if __name__ == '__main__':
	main();
