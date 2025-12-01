import sys

def solve_eko():
    # Bemenet gyors beolvasása
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # N: fák száma, M: szükséges faanyag mennyisége
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Fák magasságainak beolvasása
    trees = []
    max_height = 0
    for _ in range(N):
        h = int(next(iterator))
        trees.append(h)
        if h > max_height:
            max_height = h

    # --- Bináris Keresés a Válaszon ---
    # A vágási magasság (H) valahol 0 és a legmagasabb fa között van.
    
    low = 0
    high = max_height
    result = 0

    while low <= high:
        mid = (low + high) // 2
        
        # Mennyi fa jön össze, ha 'mid' magasságban vágunk?
        wood_collected = 0
        
        # Ez a rész kritikus a sebesség szempontjából
        # Csak akkor vágunk, ha a fa magasabb, mint a 'mid'
        for t in trees:
            if t > mid:
                wood_collected += (t - mid)
        
        # Döntés a bináris keresésben:
        if wood_collected >= M:
            # Sikerült eleget vágni!
            # De Mirko "környezettudatos", a lehető legmagasabban akar vágni.
            # Tehát ez egy lehetséges megoldás, de próbáljunk meg MAGASABBAN vágni.
            result = mid
            low = mid + 1
        else:
            # Nem jött össze elég fa.
            # ALACSONYABBAN kell vágni, hogy több fát kapjunk.
            high = mid - 1

    print(result)

if __name__ == "__main__":
    solve_eko()
