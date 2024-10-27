def main():
    S = input()
    if 4 <= len(S) <= 30:
        if S[-3:] == "san":
            print("Yes")
        else:
            print("No")
    else:
        print("No")
        
if __name__ == "__main__":
    main()