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

      
        stack = [] # Ez a mellékutca
        expected = 1 # Ezt a számot várjuk éppen
        possible = True
        
        for truck in trucks:
           
            if truck == expected:
                expected += 1
            else:
               
                while stack and stack[-1] == expected:
                    stack.pop()
                    expected += 1
                
               
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
