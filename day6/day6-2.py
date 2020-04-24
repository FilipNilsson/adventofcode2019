"""
Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)
"""
from pathlib import Path

class day6:

    def __init__(self): 
        # Parse input into list
        values = []
        with Path(__file__).parent.joinpath('input.txt').open('r') as f:
            values = f.read().split('\n')
            values.pop() # Last object is empty string
        
        # Build tree (without leafs)
        self.nodes = {}
        for item in values:
            left,right = item.split(')')
            if left not in self.nodes:
                self.nodes[left] = {'id': left, 'children': [right]}
            else:
                self.nodes[left]['children'].append(right)
        
        print("Total number of orbits: %s" % self.find_depth_of_children(self.nodes['COM'], 0))
        youPath = self.path_to_COM(self.nodes['YOU'])
        sanPath = self.path_to_COM(self.nodes['SAN'])
        print("Minimum number of orbital transfers required: %s"
              % len(set(youPath).symmetric_difference(sanPath)))


    # Find the total number of orbits (depth level) for this node and all its children
    # Add any leafs found to the nodes dict and also add the name of the parent
    # to the child.
    def find_depth_of_children(self, node, current_depth):
        total_orbits = 0
        for child in node['children']:
            if child not in self.nodes: # A leaf
                total_orbits += current_depth + 1
                self.nodes[child] = {'parent': node['id']}
            else:
                total_orbits += self.find_depth_of_children(self.nodes[child], current_depth + 1)
                self.nodes[child]['parent'] = node['id']
        return total_orbits + current_depth


    # Returns a list of all nodes between 'node' and COM.
    def path_to_COM(self, node):
        parent = node['parent']
        path = []
        while parent != 'COM':
            path.append(self.nodes[parent]['id'])
            parent = self.nodes[parent]['parent']
        return path

day6()
