

# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:()):
        self.position = position
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.t = 0 # Total time
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

# Draw a grid
def draw_grid(map, width, height, observations, spacing=2, **kwargs):
    #for y in range(height):
    #    for x in range(width):
    #        print('%%-%ds' % spacing % draw_tile(map, (x, y), kwargs), end='')
    #    print()
    l=[[0]*height for i in range(width)]

    # fill some random values in it
    for i in range(0,width):
        for j in range(0,height):
            l[i][j] = '-'
    
    for i in range(0,len(observations)):
        l[observations[i][0]][observations[i][1]] = 'O'
        
            
    # print the list
    for i in range(0,width):
        print()
        for j in range(0,height):
            print(l[i][j],end=" ")

# Draw a tile
#def draw_tile(map, position, kwargs):
    
    # Get the map value
    #value = map.get(position)
    #if position in kwargs == (0,8): value= ''

    # Check if we should print the path
    #if 'path' in kwargs and position in kwargs['path']: value = 'x'
    # Check if we should print start point
    #if 'start' in kwargs and position == kwargs['start']: value = '@'
    # Check if we should print the goal point
    #if 'goal' in kwargs and position == kwargs['goal']: value = 'O'
    # Return a tile value
    #return value 


def astar_search(map, start, end, battery):
    #(Hour, Orbit, Band1, Band2, Bat1, Bat2, 
    # pendingObservation, pendingDownload, Downloaded)

    #creating list for the opened nodes and closed nodes
    open = []
    closed =[]
    bat =0

    #create two nodes: start and goal node
    startNode= Node(start, None)
    goalNode= Node(end, None)

    #adding the start node to the opened list
    open.append(startNode)
    #battery=battery-1


    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        currentNode = open.pop(0)
        # Add the current node to the closed list
        closed.append(currentNode)
        battery= battery +1
        #check if we have reached the goal
        #return path
        if currentNode == goalNode:
            path= []
            while currentNode != startNode:
                path.append(currentNode.position)
                currentNode=currentNode.parent  
            return path[:: -1]
                
        #in order to geth the current position of the node
        (x,y)=currentNode.position

        #get neighbors
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        #loop neighbors
        for next in neighbors:
            # Get value from map
            map_value = map.get(next)
            # Check if the node is a wall
            #if(map_value == '#'):
            #    continue
            # Create a neighbor node
            neighbor = Node(next, currentNode)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue

            # Generate heuristics (Manhattan distance)
            #neighbor.f = battery
            # Generate heuristics (Manhattan distance)
            #neighbor.g = abs(neighbor.position[0] - startNode.position[0]) + abs(neighbor.position[1] - startNode.position[1])
            #neighbor.h = abs(neighbor.position[0] - goalNode.position[0]) + abs(neighbor.position[1] - goalNode.position[1])
            #neighbor.f = neighbor.g + neighbor.h
            
            neighbor.f = abs(startNode.position[0] - goalNode.position[0]) 

            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)       
            # Return None, no path is found
        #return battery
        #print("Battery: {0}".format(str(bat)))
    return None
        

    
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

# The main entry point for this module
def main():
    # Get a map (grid)
    map = {}
    chars = ['c']
    start = None
    end = None
    etc = None
    width = 4
    height = 12

    file1 = open("problema.prob","r+")  
  
    observations ={}
    while True:
        # read a single line
        line = file1.readline()
        if not line:
            break
        content=line.split(":")
        if(content[0]=="OBS"):
            obPos = content[1].split(";")
            i=0
            for ob in obPos:
                ob = ob.replace("(","")
                ob = ob.replace(")","")
                intOb = ob.split(",")
                for j in range(0, len(intOb)): 
                    intOb[j] = int(intOb[j]) 
                observations[i]=intOb
                i+=1
        #if(content[0]=="SAT1"):
        #SATX: measure; downlink; turn; charge; initialBat
        
        print(line)
    file1.close()

    battery=0
    # Find the closest path from start(@) to end(O)
    path = astar_search(map, start, end, battery)
    print()
    print(path)
    print()
    draw_grid(map, width, height,observations, spacing=1, path=path, start=start, goal=end)
    #print("Battery: {0}".format(str(battery)))
    print()
    print('Steps to goal: {0}'.format(len(path)))
    print()


# Tell python to run main method
if __name__ == "__main__": main()