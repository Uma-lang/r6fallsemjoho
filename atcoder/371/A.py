def main():
    ab, ac, bc = input().split()
    if ab != ac:
        print('A')
    elif ab == bc:
        print('B')
    else:
        print('C')

if __name__ == "__main__":
    main()