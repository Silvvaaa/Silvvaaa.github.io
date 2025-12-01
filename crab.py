import sys

def solve_crab_graphs():
    # Bemenet olvasása
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
            N = int(next(iterator)) # Csúcsok száma
            T = int(next(iterator)) # Max lábak száma
            M = int(next(iterator)) # Élek száma
        except StopIteration:
            break

        # Gráf építése (szomszédsági lista)
        # 1-től N-ig indexelünk, de a listában 0-tól N-1-ig tároljuk
        adj = {i: set() for i in range(1, N + 1)}
        
        for _ in range(M):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].add(v)
            adj[v].add(u)

        covered_vertices = set()
        total_covered_count = 0

        # Mivel a mohó algoritmus sorrendfüggő, érdemes lehet többször futtatni 
        # vagy finomítani, de itt a "Legjobb Fej - Legrosszabb Láb" elvet követjük.
        # Ez egy iteratív folyamat: amíg találunk érvényes rákot.
        
        while True:
            # 1. Keressük meg a potenciális Fejeket (amik még nincsenek lefedve)
            potential_heads = []
            for v in range(1, N + 1):
                if v not in covered_vertices:
                    # Számoljuk meg a még szabad szomszédokat
                    free_neighbors = [n for n in adj[v] if n not in covered_vertices]
                    if len(free_neighbors) > 0:
                        potential_heads.append((v, free_neighbors))
            
            if not potential_heads:
                break
            
            # 2. Rendezés: A legtöbb szabad szomszéddal rendelkező csúcs legyen az első
            # (Heurisztika: Nagy fokszámú csúcs jobb fejnek)
            potential_heads.sort(key=lambda x: len(x[1]), reverse=True)
            
            best_crab_found = False
            
            # Próbáljuk meg a legjobb fejet kiválasztani
            for head, neighbors in potential_heads:
                # 3. Válasszuk ki a lábakat
                # Heurisztika: Olyan szomszédokat válasszunk lábnak, akiknek a legkevesebb
                # szabad szomszédjuk van (hogy ne pazaroljunk el potenciális jó fejeket).
                
                # Szomszédok rendezése fokszám szerint növekvő sorrendbe
                neighbors_sorted = sorted(neighbors, key=lambda n: len([x for x in adj[n] if x not in covered_vertices]))
                
                # Maximum T lábat választhatunk
                feet_count = min(len(neighbors_sorted), T)
                
                if feet_count >= 1:
                    # Találtunk egy érvényes rákot!
                    selected_feet = neighbors_sorted[:feet_count]
                    
                    # Jelöljük be a fedett csúcsokat
                    covered_vertices.add(head)
                    for foot in selected_feet:
                        covered_vertices.add(foot)
                    
                    total_covered_count += (1 + feet_count)
                    best_crab_found = True
                    break # Újra kell számolni a fokszámokat a következő körhöz
            
            if not best_crab_found:
                break

        results.append(str(total_covered_count))

    print('\n'.join(results))

if __name__ == "__main__":
    solve_crab_graphs()
