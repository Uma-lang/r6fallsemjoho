def main():
    l, r = map(int, input().split())
    if l == 1 and r != 1:
        print("Yes")
    elif l != 1 and r == 1:
        print("No")
    else:
        print("Invalid")
if __name__ == "__main__":
    main()