def main():
    S=input()
    T=input()
    n = min(len(S), len(T))
    for i in range(n):
        if S[i] != T[i]:
            print(i + 1, '\n')
            return 0
        
    if len(S) != len(T):
        print(n + 1, '\n')
    else:
        print(0, '\n')
        
    return 0

if __name__ == "__main__":
    main()