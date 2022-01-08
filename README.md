# PokemonsGame


### Task :

- This assignment was based by a directed weighted graph with graph's algorithms.
-  We are asked to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible and  implementing our UI that will draw graphs, Pokemons and Agents.

- we implement a GameData structure that will communicate with the server, and make updates to the game.
- we also impelment Agent behaviour each Agent has it's own thread and will decide when to call "Move", each agent will also decide what his next action should be.

- The game purpose : The agens are asked to collect the highest score by eating Pokemon when each has a different value. 


### Design:
The game based of 2 parts -
api - contains all the graph classes, e.g. edge data, node data, directed weighted graph, graph algorithms and so. This section is responsible of creating graphs, edges and algorithms from graph theory such as shortest path and check whether the graph is connected by using Dijkstra-algorithm anf BFS.
gameClient - contains all the game planning and running, Pokemon and agent classes, GUI and more.
This part is responsible for running the game (automatically by algorithm) and the GUI.
To run the game there is two options, by a jar file or by login with a login screen.

### How to run?
 - In order to be able to use this project, you should have JDK 11 or above (not tetsted on older versions).
 - Simply clone this project to you computer and then import it to your favorite IDE (Eclipse, IntelliJ, etc..).
 - to run the game you can simply Click on the Ex4.jar, or run the Ex4.java file, either way, it depends on outside Server with would probably be dead in a month.

### Tests:
There are 2 JUNIT test (using JUNIT 5 version) :
DWGraph_DSTest and DWGraph_AlgoTest.

### Ingame result footage

### Sources:
- Assignment 1-3


