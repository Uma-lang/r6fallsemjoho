import math

def cost(a,b,c,d):
    return math.sqrt((a - c) ** 2 + (b - d) ** 2)

def main():
    N = int(input())
    x = [0.0]
    y = [0.0]
    
    for j in range(N):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)
        '''
        x.append(float(input()))
        y.append(float(input()))
        '''
    
    total_cost = 0.0
    for i in range(N):
        total_cost += cost(x[i], y[i], x[i + 1], y[i + 1])
        
    total_cost += cost(x[N], y[N], 0.0, 0.0)
        
    print(total_cost)
    
if __name__ == "__main__":
    main()