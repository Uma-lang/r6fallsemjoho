def main():
    cnt = 0
    for i in range(1, 12 + 1):
        S = input()
        if len(S) == i:
            cnt += 1
    print(cnt)
    
if __name__ == "__main__":
    main()