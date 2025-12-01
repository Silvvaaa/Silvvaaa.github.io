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

        # --- A JAVÍTÁS ITT KEZDŐDIK ---
        # Többször futtatjuk le véletlenszerű sorrendben, és a maximumot vesszük.
        # Mivel N kicsi (<= 100), ez nagyon gyors lesz.
        max_covered_global = 0
        
        # 100-szor próbálkozunk
        for _ in range(100):
            covered_vertices = set()
            current_covered_count = 0
            
            # Készítünk egy listát a csúcsokról és összekeverjük
            nodes = list(range(1, N + 1))
            random.shuffle(nodes)
            
            # Ebben a véletlenszerű sorrendben próbálunk fejeket választani
            for head in nodes:
                if head in covered_vertices:
                    continue
                
                # Megnézzük a szabad szomszédokat
                free_neighbors = [n for n in adj[head] if n not in covered_vertices]
                
                if not free_neighbors:
                    continue
                
                # Heurisztika: A szomszédok közül azokat választjuk lábnak,
                # akiknek a legkevesebb szabad szomszédjuk van (hogy a jó fejeket megkíméljük).
                # De itt is vihetünk bele egy kis véletlent, vagy maradhatunk a rendezésnél.
                # Most maradunk a rendezésnél, mert a fő ciklus keverése általában elég.
                free_neighbors.sort(key=lambda n: len([x for x in adj[n] if x not in covered_vertices]))
                
                feet_count = min(len(free_neighbors), T)
                
                if feet_count >= 1:
                    selected_feet = free_neighbors[:feet_count]
                    
                    # Foglaljuk le
                    covered_vertices.add(head)
                    for foot in selected_feet:
                        covered_vertices.add(foot)
                    
                    current_covered_count += (1 + feet_count)
            
            # Ha ez a kör jobb eredményt adott, mint az eddigiek, mentsük el
            if current_covered_count > max_covered_global:
                max_covered_global = current_covered_count

        results.append(str(max_covered_global))

    print('\n'.join(results))

if __name__ == "__main__":
    solve_crab_graphs()
