def main():
    a, b = map(int, input().split())
    cnt = 0
    if a == b:
        print(1)
    elif (a+b) % 2 == 0:
        print(3)
    else:
        print(2)
if __name__ == "__main__":
    main()