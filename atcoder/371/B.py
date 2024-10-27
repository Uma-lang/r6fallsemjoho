def main():
    N, M = map(int, input().split())
    hastaro = [False for _ in range(N)]
    for i in range(M):
        a, b = input().split()
        a = int(a) - 1
        if hastaro[a] == False and b =='M':
            print("Yes")
            hastaro[a] = True
        else:
            print("No")
            
if __name__ == "__main__":
    main()