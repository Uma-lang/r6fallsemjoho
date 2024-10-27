def main():
    n = int(input())
    pos = [-1, -1]
    ans = 0
    for i in range(n):
        a, s = input().split()
        hand = (s == 'R')
        if pos[hand] != -1:
            ans += abs(pos[hand] - int(a))
        pos[hand] = int(a)
    print(ans)
if __name__ == '__main__':
    main()