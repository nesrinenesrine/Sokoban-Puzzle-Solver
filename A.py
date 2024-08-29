def A(initial_node, heuristic=1):
        
        # Check if the initial node is the goal
        if initial_node.state.isGoal(Node.wall_space_obstacle):
            return initial_node, 0

        # Evaluate the cost f for the initial node
        initial_node.F_Evaluation(heuristic)

        # Create the OPEN list with the initial node as the first element
        open = [initial_node]

        # Create the CLOSED list
        closed = list()
        
        step = 0
        while True:

            step +=1
            print (f'*** Step {step} ***')            
            
            # Check if the OPEN list is empty => goal not found 
            if len(open) == 0:
                return None, -1
            
            # Get the index of the node with least f in the OPEN list 
            min_index, _ = min(enumerate(open), key=lambda element: element[1].f)            
            current = open[min_index]

            # Remove the current node (i.e. the node with least f) from the OPEN list
            open.remove(current)
            
            # Put the current node in the CLOSED list
            closed.append(current)
            
            # Check if the current state is a goal
            if current.state.isGoal(Node.wall_space_obstacle):
                print ("Goal reached") 
                return current, step 

            # Generate the successors of the current node
            succ = current.succ()
            while len(succ) != 0:
                # Pop a child node from the list of successors 
                child = succ.popleft()
                # Evaluate the cost f for this child node
                child.F_Evaluation(heuristic)
                
                # If the child is in the OPEN list
                if child.state.robot_block in [n.state.robot_block for n in open]:
                    # Get the index of the child in the OPEN list
                    index = [n.state.robot_block for n in open].index(child.state.robot_block)
                    # Replace the node in the OPEN list by the new one if its cost f is less than the old one
                    if open[index].f > child.f: 
                        # Remove the old node from the OPEN list
                        open.remove(open[index])
                        # Put the new node with the minimal cost f in the OPEN list 
                        open.append(child) 

                # If the child is not in the OPEN list    
                else:
                    # If the child is not in the CLOSED list
                    if child.state.robot_block not in [n.state.robot_block for n in closed]:
                        # Put the child in the OPEN list 
                        open.append(child)  

                    # If the child is in the CLOSED list
                    else:
                        # Get the index of the child in the CLOSED list
                        index = [n.state.robot_block for n in closed].index(child.state.robot_block)
                        # Remove the node from the CLOSED list and add the new one in the OPEN list if its cost f is less than the old one
                        if closed[index].f > child.f:
                            # Remove the child from the CLOSED list
                            closed.remove(closed[index])
                            # Put the child in the OPEN list 
                            open.append(child)
            