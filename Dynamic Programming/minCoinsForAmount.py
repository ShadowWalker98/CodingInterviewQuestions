# Question:

''' An array of positive integers representing coin denominations and a single non
negative integer n representing a target amount of money is given. Write a function that returns the
smallest number of coins required to make change for that target amount using the given coin
denominations. An unlimited number of coins are available. If it is impossible to make then return -1'''

# Sample Input/Output

# i/p: n = 7, coins = [1, 5, 10]
# o/p: 3 (2x1 + 1x5)

# solution:

def minNumberCoins(n, denoms):
    memo = dict()
    return coinChange(denoms, n, memo)

def coinChange(denoms, n, memo):
    if n in memo: return memo[n]

    if n < 0:
        return -1
    elif n == 0:
        return 0
    res = float('INF')
    for coin in denoms:
        subprob = coinChange(denoms, n - coin, memo)
        if subprob == -1:
            continue
        res = min(res, 1 + subprob)

    memo[n] = res if res != float('INF') else -1

    return memo[n]

if __name__ == "__main__":
    coins = [1, 5, 10]
    n = 7
    ans = minNumberCoins(n, coins)
    print(" min number of coins required: ", ans)

