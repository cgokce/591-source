//
// Coursera Assignment 3
// Kruskal's algorithm for finding the minimum spanning tree
//
// Cagri Gokce
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <fstream>

using namespace std;

const bool verbose = true;

// Helper function prototypes
int greedy_calc(vector <int> current_array, vector <int> processed_nodes);
vector<int> shortest_path(vector <vector<int> > matrix);
void print_graph(vector < vector<int> > my_graph);
void modify_value(vector < vector<int> > &my_graph, int source, int target);

// Edge structure to code edge for easier sorting
struct Edge{

public:
    int source;
    int target;
    int weight;

    // Constructor: Default
    Edge(){}

    // Constructor: Parameter
    Edge(int s, int t, int w){
        source = s;
        target = t;
        weight = w;
    }
};

// Graph Abstract Data Type
class GraphADT{

public:
	// Constructor: Generates graph randomly from density.
	GraphADT(float density_, int range_min_, int range_max_, int node_count_){
		density = density_;
		range_min = range_min_;
		range_max = range_max_;
		node_count = node_count_;
	}

	// Constructor: Constructs graph by reading weights from file
	GraphADT(string file_path = "../sample_test_data.txt"){
        //1. Read the file.
        cout << "Reading from file -> sample_text_data.txt";
        ifstream infile(file_path);
        if (!infile) {
            cerr << "Error reading the sample_test_data.txt";
            exit(1);
        }

        //2. Get the graph node count
        infile >> node_count;
        cout << endl << "Graph Node Count" << node_count << endl;

        //3. Init the empty matrix
        std::vector<std::vector<int> > matrix(
                node_count,std::vector<int>(node_count));
        for(int i=0;i<node_count;i++) {
            for (int j = 0; j < node_count; j++) {
                matrix[i][j] = 0;
            }
        }

        //4. Read the all other lines and construct to matrix
        int source,target,weight;
        while(infile >> source >> target >> weight){
            matrix[source][target] = weight;
        }


        //5. Set the innate graph
        graph = matrix;
	}

	// Generate() : Generates the random graph.
	void generate(){

        // 1. Create the empty graph
        std::vector<std::vector<int> > matrix(
                node_count,std::vector<int>(node_count));
        int dense_check;

        // 2. Fill with random values
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

		// 3. Assign the value
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

    int bfs(vector<Edge> & edges, int start, int end){
	    // return all possible nodes reachable for current node
	    // recursive bfs algorithm

	    vector<Edge> temp = vector<Edge>();
        for (int i=0; i<edges.size(); i++)
            temp.push_back(edges[i]);


	    for(int i = 0;i < edges.size();i++){

	        // Restore the temp array
	        for (int i=0; i<edges.size(); i++)
                temp.push_back(edges[i]);

            // S->T
            if (edges[i].source == start){
                // Terminal condition
                if (edges[i].target == end)
                    return 1;

                temp.erase( temp.begin() + i );
                return bfs(temp, edges[i].target, end);
            }

	    }
	    // Terminal condition
	    return 0;

	}


    void findMSTKruskal(){
        // Order all the weights with keeping their edge count
        // My strategy is just vectorize all the edges
        // And also keep the source,target values in another
        // It is probably not the most efficient way but whatever

        // Change zero nodes with higher int values
        modify_value(graph,0 , 99999);

        // Use the edge struct here
        vector<Edge> edges = vector<Edge>();
        for(int i=0;i<node_count;i++){
            // Undirected, only take the lower triangle of the matrix
            for (int j=0;j<i;j++){
                edges.emplace_back(i,j,graph[i][j]);
            }
        }

        // Sort the edge values by comparing weights
        sort(edges.begin(), edges.end(),
             [](const auto& i, const auto& j) { return i.weight < j.weight; } );


        vector<Edge> MST = vector<Edge>();

        bool createsCycle;
        for (int i = 0; i < edges.size(); i++){

            createsCycle = false;

            // If there is a path, then it'll create a cycle
            if (bfs(MST, edges[i].source, edges[i].target)){
                createsCycle = true;
            }


            // First edge or does not create cycle, then take it
            if (i==0 || !createsCycle){
                MST.push_back(edges[i]);
            }

            // End case -- MST reaches (V-1) nodes
            if (MST.size() == node_count-1){
                cout << "-----Calculating MST-----" << endl << "MinimumSpanningTree node count:" << MST.size() << endl;
                break;
            }
        }


        int totalCost = 0;
        for(auto & j : MST){
            cout << j.source <<" --> " << j.target << " ( Cost: " << j.weight << ")" << endl;
            totalCost += j.weight;
        }
        cout << "Total Cost: " << totalCost << endl;

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

    // Read the Graph
    GraphADT graph1("sample_test_data.txt");
    //graph1.show();

    // Apply the Kruskal Algorithm
    cout << endl << endl;
    graph1.findMSTKruskal();


	return 0;
}


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
            processed_nodes[i] = -1;
        if(verbose) cout << "No path error";

        if(verbose) cout << processed_nodes[i-1] << "->" << processed_nodes[i] << "\t\t" << distances[i-1] << endl;
    }
    return distances;
}

// Graph print function for debugging
void print_graph(vector < vector<int> > my_graph){
    for(int i=0;i<my_graph.size();i++){
        for(int j=0; j<my_graph[i].size(); j++){
            if (verbose) cout << my_graph[i][j] << " ";
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
