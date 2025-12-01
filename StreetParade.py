import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    while True:
        try:
            n_str = next(iterator)
            if n_str == '0': # A bemenet végét a 0 jelzi
                break
            n = int(n_str)
            
            trucks = []
            for _ in range(n):
                trucks.append(int(next(iterator)))
                
        except StopIteration:
            break

        # --- A Logika (Stack Simulation) ---
        stack = [] # Ez a mellékutca
        expected = 1 # Ezt a számot várjuk éppen
        possible = True
        
        for truck in trucks:
            # 1. eset: Ha ez a kamion jön a sorban
            if truck == expected:
                expected += 1
            else:
                # 2. eset: Ha nem ő jön, betoljuk a stack-be.
                # DE ELŐTTE: Nézzük meg, hogy a stack tetején lévő nem-e a soros?
                # Mert ha a stack tetején kisebb szám van, mint a mostani kamion,
                # akkor beragadnak (a stack LIFO - Last In First Out).
                while stack and stack[-1] == expected:
                    stack.pop()
                    expected += 1
                
                # Ha a stack tetején lévő szám kisebb, mint a mostani,
                # akkor baj van, mert a kicsi nem tud majd kijönni a nagy tól.
                if stack and stack[-1] < truck:
                    possible = False
                    break
                
                stack.append(truck)
        
        # A végén még kiszedjük a maradékot a stackből, ha jó a sorrend
        if possible:
            while stack and stack[-1] == expected:
                stack.pop()
                expected += 1
            
            # Ha üres a stack, akkor sikerült mindet kiküldeni
            if not stack:
                print("yes")
            else:
                print("no")
        else:
            print("no")

if __name__ == "__main__":
    solve()