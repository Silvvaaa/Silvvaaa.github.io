import sys


sys.setrecursionlimit(2000)

def solve_pigbank():
    
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
            E = int(next(iterator)) # Empty weight
            F = int(next(iterator)) # Full weight
            N = int(next(iterator)) # Number of coin types
        except StopIteration:
            break
            
        target_weight = F - E
        
        # Érmék beolvasása: (érték, súly) párok
        coins = []
        for _ in range(N):
            val = int(next(iterator))
            wei = int(next(iterator))
            coins.append((val, wei))
            
      
        
        INF = float('inf')
        dp = [INF] * (target_weight + 1)
        dp[0] = 0
        
        # Végigmegyünk minden érmetípuson
        for value, weight in coins:
            # És végigmegyünk a súlyokon az érme súlyától a célig
            # Ez a sorrend teszi lehetővé, hogy egy érmét többször is használjunk
            for j in range(weight, target_weight + 1):
                if dp[j - weight] != INF:
                    # Ha a (j - weight) súly elérhető, megnézzük, 
                    # hogy ha hozzáadjuk ezt az érmét, olcsóbb-e, mint eddig.
                    if dp[j - weight] + value < dp[j]:
                        dp[j] = dp[j - weight] + value
        
        # Eredmény vizsgálata
        if dp[target_weight] == INF:
            results.append("This is impossible.")
        else:
            results.append(f"The minimum amount of money in the piggy-bank is {dp[target_weight]}.")

  
    print('\n'.join(results))

if __name__ == "__main__":
    solve_pigbank()
