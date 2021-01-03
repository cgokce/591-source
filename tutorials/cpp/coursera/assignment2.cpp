//
// Monte Carlo simulation on Undirected Graphs using Djkstra's Shortest Path Algorithm
// Graph uses the connectivity matrix representations
//
// Cagri Gokce
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

const bool verbose = false;

int greedy_calc(vector <int> current_array, vector <int> processed_nodes){

	// Go to the closest node in this greedy function
	int min_dist = 999999;
	int min_node;

	for(int i =0 ; i<current_array.size(); i++){
		// Skip the already processed nodes
		if (find (processed_nodes.begin(), processed_nodes.end(), i) != processed_nodes.end())
			continue;

		if (current_array[i] < min_dist){
			min_dist = current_array[i];
			min_node = i;
		}
	}


	if (min_dist == 99999) //Exception, there is no connection there, skip this node.
		return -1;
	else
		return min_node;
}



vector<int> shortest_path(vector <vector<int> > matrix){

	// Calculate the distance matrix
	// Placeholder for the final distances.
	vector <int> processed_nodes;
	vector <int> distances;
	vector <int> current_array;
	bool end = 0;

	int current_node = 0;
	int next_node;
	processed_nodes.push_back(current_node);

	// Traverse until all nodes are reached
	while(!end)
	{

		// TODO: Check if all nodes are processed, set the end
		if (processed_nodes.size() == matrix.size())
			end = 1;
		else{

			// Find the next minimum node
			current_array = matrix[current_node];
			next_node = greedy_calc(current_array, processed_nodes);

			// Use the next minimum node.
			processed_nodes.push_back(next_node);
			distances.push_back(current_array[next_node]);
			current_node = next_node;
		}
	}

	if (verbose) cout << "Processed_node" << "\t" << "Distance" << endl;
	for(int i=1; i<processed_nodes.size(); i++){
	    if (processed_nodes[i] == -1)
	        processed_nodes = -1;
	        if(verbose) cout << "No path error";

        if(verbose) cout << processed_nodes[i-1] << "->" << processed_nodes[i] << "\t\t" << distances[i-1] << endl;
	}
    return distances;
}

// Graph print function for debugging
void print_graph(vector < vector<int> > my_graph){
	for(int i=0;i<my_graph.size();i++){
		for(int j=0; j<my_graph[i].size(); j++){
            if (verbose) cout << my_graph[i][j];
		}
        if (verbose)  cout << endl;
	}
}

void modify_value(vector < vector<int> > &my_graph, int source, int target){
	for(int i=0;i<my_graph.size();i++){
		for(int j=0; j<my_graph[i].size(); j++){
			if(my_graph[i][j]==0)
				my_graph[i][j] = 99999;
		}
	}
}

// Graph Abstract Data Type
class GraphADT{

public:
	// Constructor
	GraphADT(float density_, int range_min_, int range_max_, int node_count_){
		density = density_;
		range_min = range_min_;
		range_max = range_max_;
		node_count = node_count_;
	}

	// Generate the 2D Array - n = size
	void generate(){

        std::vector<std::vector<int> > matrix(
                node_count,std::vector<int>(node_count));
        int dense_check;

		for(int i=0;i<node_count;i++){
			for (int j=0;j<node_count;j++){

				// Identity part should be all zeros.
				// A node does not have connection to itself.
				if (i == j) {
                    matrix[i][j] = 0;
                }else{
                    // Fill according to the random density constraint
                    dense_check = rand() % 10;

                    if (dense_check > int(density*10))
				        matrix[i][j] = rand() % range_max + range_min;
                    else
                        matrix[i][j] = 0;

                }
            }
		}
		graph = matrix;
    }

    void show(){
        if (verbose) cout << "Undirected & Weighted Graph (in Connectivity Matrix Format, 0 = no connection)" << endl;
        print_graph(graph);
	}

	void calculate_shortest_path(){
        // Change zeroes with the 99999 to make the distance infinite for those
        modify_value(graph,0 , 99999);
        vector<int> distances = shortest_path(graph);

        // Average all the distances
        int sum = 0;
        for(int i=0; i<distances.size(); i++)
            sum += distances[i];
        if (verbose) cout << endl << "SIZE:" << distances.size() << endl;
        if (verbose) cout << endl << "SUM: " << sum << endl;
        cout << endl << "Average Path Length: " << (float(sum)/distances.size()) << endl;

    }

private:

	int node_count;
	float density;
	int range_min;
	int range_max;
    std::vector<std::vector<int> > graph;
};



int main()
{
    cout << "Coursera Assignment 2" << endl;

    float density = 0.2;
	int min_range = 1;
	int max_range = 9;
    int n = 50;
    // Description
    cout << "[Graph] n:" << n << " density:" << density << " path length range: " << min_range << " to " << max_range;
    GraphADT graph1(density, min_range, max_range, n);
    graph1.generate();
	// Print the Graph
    graph1.show();
    // Calculate the Shortest Path
    if (verbose) cout << endl << "Shortest distance to each node from node 0:" << endl;
    graph1.calculate_shortest_path();

    // Second graph
    density = 0.4;
    cout << "[Graph] n:" << n << " density:" << density << " path length range: " << min_range << " to " << max_range;
    GraphADT graph2(density, min_range, max_range, n);
    graph2.generate();
    graph2.show();
    if (verbose) cout << endl << "Shortest distance to each node from node 0:" << endl;
    graph2.calculate_shortest_path();

	return 0;
}
