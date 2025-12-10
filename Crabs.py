import sys
import random

def solve_crab_graphs():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        num_test_cases = int(next(iterator))
    except StopIteration:
        return

    results = []

    for _ in range(num_test_cases):
        try:
            N = int(next(iterator))
            T = int(next(iterator))
            M = int(next(iterator))
        except StopIteration:
            break

        # Gráf építése
        adj = {i: set() for i in range(1, N + 1)}
        for _ in range(M):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].add(v)
            adj[v].add(u)

      
        max_covered_global = 0
        
       
        for _ in range(100):
            covered_vertices = set()
            current_covered_count = 0
            
           
            nodes = list(range(1, N + 1))
            random.shuffle(nodes)
            
            
            for head in nodes:
                if head in covered_vertices:
                    continue
                
               
                free_neighbors = [n for n in adj[head] if n not in covered_vertices]
                
                if not free_neighbors:
                    continue
                
                
                free_neighbors.sort(key=lambda n: len([x for x in adj[n] if x not in covered_vertices]))
                
                feet_count = min(len(free_neighbors), T)
                
                if feet_count >= 1:
                    selected_feet = free_neighbors[:feet_count]
                    
                    # Foglaljuk le
                    covered_vertices.add(head)
                    for foot in selected_feet:
                        covered_vertices.add(foot)
                    
                    current_covered_count += (1 + feet_count)
            
            
            if current_covered_count > max_covered_global:
                max_covered_global = current_covered_count

        results.append(str(max_covered_global))

    print('\n'.join(results))

if __name__ == "__main__":
    solve_crab_graphs()
