#### Multi Dimensional Array List in Java

    https://www.baeldung.com/java-multi-dimensional-arraylist

Two dimensional ArrayList
- Eg. generate a graph with 3 vertices, 0 to 2. 
- Representing edges in 2d arrayList by generating ArrayList of ArrayLists

        int vertexCount = 3;
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>(vertexCount);

        // Initialize
        for(int = 0; i<vertexCount; i++>){
            graph.add(new ArrayList());
        }

        // Add elements
        graph.get(0).add(1);
        graph.get(1).add(2);
        graph.get(2).add(0);
        ...
        
        // Iterate the entire graph using double for loop
        int vertexCount = graph.size();
        for (int i = 0; i< vertexCount; i++){
            int edgeCount = graph.get(i).size();

            for(int j = 0; j<edgeCount; j++){
                Integer startVerted = i;
                Integer endVerted = graph.get(i).get(j);
                //...
            }
        } 

Three dimensional array list
- Eg. representing a 3d space with 3 coordinates (x,y,z)

        ArrayList<ArrayList<ArrayList<String>>> space = new ArrayList<>(x_axis_length);

        //Init the 3d list
        ...

        // Add item
        space.get(0).get(0).add(0, "Red")