# PokemonsGame


### Task :
-  We are asked to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible and  implementing our UI that will draw graphs, Pokemons and Agents.


### Overview 
- This assignment was based by  directed weighted graph with graph's algorithms.

- we implement a GameData structure that will communicate with the server, and make updates to the game.
- we also impelment Agent behaviour each Agent has it's own thread and will decide when to call "Move", each agent will also decide what his next action should be.

- The game purpose : The agens are asked to collect the highest score by eating Pokemon when each has a different value. 


### Design

- Client_python folder : contains all the graph classes, e.g. edge data, node data, directed weighted graph, graph algorithms and so.
-  This section is responsible of creating graphs, edges and algorithms from graph theory such as shortest path and check whether the graph is connected by using Dijkstra-algorithm ...
-  We used the classes that we had Implemented in the previous assignmet (EX3).
-  New Main classes : 
-   They contains all the game planning and running, Pokemon and agent classes, GUI and more.
This part is responsible for running the game (automatically by algorithm) and the GUI.
    -  client.py : Manges all the Networking with  the servers , and takes all the data  and the graph .
    -  student_code.py : we use all the implementation and the Algorithms ...
- and One secondry class:
    - Calc_Pos: this class we implement in order to find the edge fot each pokemon and the position would be calculated  by linear equation

### How to run?
 - In order to be able to use this project, you should have JDK 11 or above (not tetsted on older versions).
 - Simply clone this project to you computer and then import it to your favorite IDE (pycharm..).
 - to run the game you can simply Click on the Ex4.jar, or run the Ex4.py file, either way, it depends on outside Server with would probably be dead in a month.

### Ingame result footage

![צילום מסך 2022-01-08 235245](https://user-images.githubusercontent.com/84326639/148661190-28f98261-f9a7-4606-aed3-de3715a8180e.png)




### UML Diagram:
![image](https://user-images.githubusercontent.com/84326639/148701940-c61f6e0f-5aa3-42f2-9380-ab51e8cee7e2.png)





### Sources:
- Assignment 1-3


