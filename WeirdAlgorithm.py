import sys

def solve():
    # Beolvassuk az egyetlen számot
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    result = [str(n)]

    # Amíg nem érünk el 1-ig, csináljuk a szabályokat
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        result.append(str(n))

    # Kiírjuk a számokat szóközzel elválasztva
    print(" ".join(result))

if __name__ == "__main__":
    solve()
