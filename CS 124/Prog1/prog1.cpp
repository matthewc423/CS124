#include <algorithm>
#include <iostream>
#include <tuple>
#include <set>
#include <vector>
#include <cmath>
#include <random>
#include <time.h>

using namespace std;

/*
 * Tuple that stores the vertex number and its corresponding weight
 */
class Node {
  public:  
    int vertex;
    double weight;

    Node () {
      vertex = -1;
      weight = -1;
    }

    Node (int v, double w) {
      vertex = v;
      weight = w;
  }
};

/*
 * Our graph implementation which contains the number of vertices and 
 * a list of lists containing the vertices that the index vertex has
 * an edge to
 */

class Graph {
  public:
    int vertices;
    vector <vector <Node> > edges;
    
    Graph (int v, vector <vector <Node> > e){
      vertices = v;
      edges = e;  
    }
    
    int len() { 
      return vertices; 
      };
    
    double length(int u, int v) {
      for (int i = 0; i < edges[u].size(); i++) {
        if (v == edges[u][i].vertex) {
          return edges[u][i].weight;
        }
      }
      return 2.0; //if doesn't exist, no edge length can be greater than 1
    }
    
};

/*
 * Minheap implementation of a priority queue
 * 
 */
class Priority_heap {
  
  public:
    vector<Node> H;

    Priority_heap () {
      // H = {};
    }
  
  int get_parent(int x){
    return (x+1)/2 -1;
  }
  
  int get_left(int x){
    return (x+1)*2 -1;
  }
  
  int get_right(int x){
    return (x+1)*2;
  }
  
  //rearranges heap with root node N
  void min_heapify(int N) {
    int l = get_left(N);
    int r = get_right(N);
    
    int smallest = N; 
    
    if (l < H.size() && H[l].weight < H[N].weight) {
      smallest = l;
    }
    
    if (r < H.size() && H[r].weight < H[smallest].weight) {
      smallest = r;
    }
    
    if (smallest != N) {
      swap(N, smallest);
      min_heapify(smallest);
    }
  }
  
  void build_heap(vector <Node> A) {
    for (int i = (A.size() / 2); (i = 0); i--) {
      min_heapify(i);
    }
  }
  
  void swap(int x, int y)
	{
    iter_swap(H.begin()+x,H.begin()+y);
	}
  
	Node extract_min() { 
    if (H.size() > 0) {
      Node min = H[0];
      H[0] = H[H.size() - 1]; 
      H.pop_back();
      min_heapify(0);
      return min;
    }
    throw -1;
  };
  
  void insert(Node new_node) {
    H.push_back(new_node);
    int N = H.size() - 1;
    
    while (N != 0 && H[get_parent(N)].weight > H[N].weight) {
      swap(get_parent(N), N);
      N = get_parent(N);
    }
  }

  int len() {
    return H.size();
  }
};


double prim(Graph G, int s) {

  vector <double> dist;
  vector <int> prev;

  int n = G.vertices;
  set<int> S;

  for (int i = 0; i < n; i++) {
    dist.push_back(2.0);
  }

  for (int i = 0; i < n; i++) {
    prev.push_back(-1);
  }

  vector <Node> Node_lst;
  Node_lst.clear();

  Priority_heap H = Priority_heap();
  H.insert(Node(s, 0.0));

  dist[s] = 0;
  
  while (H.len() > 0) 
  {
    int v = H.extract_min().vertex;

    S.insert(v);
    
    for (int i = 0; i < G.edges[v].size(); i++) {
      Node w_node = G.edges[v][i];
      int w = w_node.vertex;
      
      if (S.count(w) != 1) {

        double edge_length = G.length(v, w);
        
        if (dist[w] > edge_length) {

          dist[w] = edge_length;
          prev[w] = v;
          H.insert(Node(w, dist[w]));

          
        }
        
      }
      
    }
    
  }


  double sum = 0.0;
  for (int i = 0; i < n; i++) {
    sum += dist[i];
  }

  return sum / n;
}

Graph make_graph (int n, int type) {

  vector <vector <Node> > edge_nums;
  vector <Node> Node_lst;
  switch (type) {
    case 1:
      for (int i = 0; i < n; i++) {
				Node e;
        Node_lst.clear();

        for (int j = 0; j < i; j++) {
          e = Node(j, edge_nums[j][i - 1].weight);
          Node_lst.push_back(e);
        }
        for (int j = i + 1; j < n; j++) {
          e = Node(j, (double) rand() / RAND_MAX);
          Node_lst.push_back(e);
        }
        edge_nums.push_back(Node_lst);
      }
      break;
    case 2:
      for (int i = 0; i < n; i++) {
        Node e;
        Node_lst.clear();
        for (int j = 0; j < i; j++) {
          e = Node(j, edge_nums[j][i-1].weight);
          Node_lst.push_back(e);
        }
        for (int j = i + 1; j < n; j++) {
          double x_coord = (double) rand() / RAND_MAX;
          double x2_coord = (double) rand() / RAND_MAX;
          double y_coord = (double) rand() / RAND_MAX;
          double y2_coord = (double) rand() / RAND_MAX;

          double distance = sqrt(pow((x_coord - x2_coord),2) + pow((y_coord - y2_coord),2));
          
          
          e = Node(j, distance);
          Node_lst.push_back(e);
        }
        edge_nums.push_back(Node_lst);
      }
      
      break;
    case 3:
      for (int i = 0; i < n; i++) {
        Node e;
        Node_lst.clear();
        for (int j = 0; j < i; j++) {
          e = Node(j, edge_nums[j][i-1].weight);
          Node_lst.push_back(e);
        }
        for (int j = i + 1; j < n; j++) {
          double x_coord = (double) rand() / RAND_MAX;
          double x2_coord = (double) rand() / RAND_MAX;
          double y_coord = (double) rand() / RAND_MAX;
          double y2_coord = (double) rand() / RAND_MAX;
      		double z_coord = (double) rand() / RAND_MAX;
      		double z2_coord = (double) rand() / RAND_MAX;
      
      		double distance = sqrt( pow((x_coord - x2_coord),2) + pow((y_coord - y2_coord),2) + pow((z_coord - z2_coord),2) );
          
          e = Node(j, distance);
          Node_lst.push_back(e);
        }

        edge_nums.push_back(Node_lst);
      }
      Node_lst.clear();
      break;
    case 4:
      for (int i = 0; i < n; i++) {
        Node e;
        Node_lst.clear();
        for (int j = 0; j < i; j++) {
          e = Node(j, edge_nums[j][i-1].weight);
          Node_lst.push_back(e);
        }
        for (int j = i + 1; j < n; j++) {
          double x_coord = (double) rand() / RAND_MAX;

          double x2_coord = (double) rand() / RAND_MAX;

          double y_coord = (double) rand() / RAND_MAX;

          double y2_coord = (double) rand() / RAND_MAX;

      		double z_coord = (double) rand() / RAND_MAX;

      		double z2_coord = (double) rand() / RAND_MAX;

          double a_coord = (double) rand() / RAND_MAX;

          double a2_coord = (double) rand() / RAND_MAX;
      
      		double distance = sqrt( pow((x_coord - x2_coord),2) + pow((y_coord - y2_coord),2) + pow((z_coord - z2_coord),2) + pow((a_coord - a2_coord),2));

          e = Node(j, distance);
          Node_lst.push_back(e);
        }
      
        edge_nums.push_back(Node_lst);
      }
      Node_lst.clear();
      break;
  }

  return Graph(n, edge_nums);
}


int main() {

  srand (time(0));
  
  vector <int> n;
  vector <double> g1_values;
  vector <double> g2_values;
  vector <double> g3_values;
  vector <double> g4_values;

  for (int i = 128; i <= 128; i *= 2) {
    n.push_back(i);
  }
  
  for (int i = 0; i < n.size(); i++) {
    for (int j = 0; j < 5; j++) {
    Graph g1 = make_graph(n[i], 1);
    Graph g2 = make_graph(n[i], 2);
    Graph g3 = make_graph(n[i], 3);
    Graph g4 = make_graph(n[i], 4);

    g1_values.push_back(prim(g1, 0));
    g2_values.push_back(prim(g2, 0));
    g3_values.push_back(prim(g3, 0));
    g4_values.push_back(prim(g4, 0));
    }
  }

  for (int i = 0; i < g1_values.size(); i++) {
    cout << n[i] << ": " << g1_values[i] << " " << g2_values[i] << " " << g3_values[i] << " " << g4_values[i] << "\n";
  }
  return 0; 
}

