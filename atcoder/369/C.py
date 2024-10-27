def f(n):
    return n * (n + 1) // 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = n
    pre = 0
    for i in range(1, n - 1):
        if a[i] - a[i - 1] != a[i + 1] - a[i]:
            ans += f(i - pre)
            pre = i
            
    ans += f(n - 1 - pre)
    print(ans)

if __name__ == "__main__":
    main()