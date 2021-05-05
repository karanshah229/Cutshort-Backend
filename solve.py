def simplifyDebts(amount):
    mxCredit = amount.index(max(amount))
    mxDebit = amount.index(min(amount))

    # If both amounts are 0,
    # then all amounts are settled
    if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
        return 0

    # Find the minimum of two amounts
    min_amt = min(-amount[mxDebit], amount[mxCredit])
    amount[mxCredit] -= min_amt
    amount[mxDebit] += min_amt

    # If minimum is the maximum amount to be
    print("Person", mxDebit, "pays", min_amt, "to", "Person", mxCredit)

    simplifyDebts(amount)


def minCashFlow(graph):
    amount = [0 for i in range(N)]

    for p in range(N):
        for i in range(N):
            amount[p] += (graph[i][p] - graph[p][i])

    simplifyDebts(amount)


graph = [[0, 100, 250, 600],
         [800, 0, 5000, 100],
         [0, 900, 600, 0],
         [0, 650, 700, 150]]
N = len(graph)

minCashFlow(graph)
