 
# Top Down (1)
def min_cost_climbing_stairs(cost: list):

    totalCost = {}

    def recursive_mccs(n):
        if n == 0 or n == 1:
            return cost[n]
        
        if n not in totalCost:
            if n == len(cost):
                totalCost[n] = min(recursive_mccs(n-1), recursive_mccs(n-2))
            else:
                totalCost[n] = cost[n] + min(recursive_mccs(n-1), recursive_mccs(n-2))
        
        return totalCost[n]
    
    return recursive_mccs(len(cost))

print(min_cost_climbing_stairs([10, 15, 20, 17, 1]))



# Top Down (2)

def mccs(cost: list):
    costDict = {}

    def dp(n):
        if n == 0 and n == 1:
            """
            현재 dfs의 리턴 값은 n-1층, n-2층까지 걸린 비용의 최소 값을 리턴함.
            위 문제에서 첫 시작은 1, 2층에서 시작하게 되고, 이전까지 걸린 비용은 없으므로 0을 리턴.
            """
            return 0
        
        if n not in costDict:
            costDict[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
        
        return costDict[n]
    
    return dp(len(cost))


# Bottom Up

def mccs_bottomUp(cost: list):
    # len(cost) + 1의 위치한 계단까지의 최소 비용을 알고 싶음.
    memo = [-1] * (len(cost) + 1)
    memo[0] = 0
    memo[1] = 0

    for i in range(2, len(cost) + 1):
        memo[i] = min(memo[i-1] + cost[i-1], memo[i-2] + cost[i-2])

    return memo[-1]

print(mccs_bottomUp([10, 15, 20]))