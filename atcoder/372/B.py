def main():
    A = []
    M = int(input())
    for k in range(11):
        A += [k] * (M % 3)
        M //= 3
    print(len(A))
    print(*A)
    
if __name__ == "__main__":
    main()