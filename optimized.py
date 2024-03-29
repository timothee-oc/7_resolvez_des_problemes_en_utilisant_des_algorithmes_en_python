import csv
import os
import time
import argparse

MAX_BUDGET = 500

def parse_csv_input(file_path):
    shares = {}
    with open(file_path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if float(row[1]) <= 0:
                continue
            else:
                name = row[0]
                cost = int(float(row[1]) * 100)
                profit = cost * float(row[2]) / 100
                shares[name] = (cost, profit)
    return shares

def optimized(shares, budget):
    """
    Take a list of shares (with a name, a cost and a profit) and return the best
    combination of them given a budget (500€ by default).
    User dynamic programming by building a matrix which resolves sub problems of
    the main one iteratively (i.e. with less budget and/or shares) in each cell.
    Last cell gives the max profit and then best combination is retrieved by walking
    back and up the matrix.
    Complexity is O(budget*len(shares)), much more efficient than bruteforce.
    """
    max_budget = budget * 100
    matrix = [[0] * (max_budget + 1) for _ in range(len(shares) + 1)]

    for i, (_, (cost, profit)) in enumerate(shares.items(), 1):
        for budget in range(1, max_budget + 1):
            if cost <= budget:
                matrix[i][budget] = max(matrix[i-1][budget], matrix[i-1][budget-cost] + profit)
            else:
                matrix[i][budget] = matrix[i-1][budget]

    best_comb = []
    current_budget = max_budget
    for i in range(len(shares), 0, -1):
        if matrix[i][current_budget] != matrix[i-1][current_budget]:
            share_name = list(shares.keys())[i-1]
            best_comb.append(share_name)
            current_budget -= shares[share_name][0]

    return best_comb, matrix[len(shares)][max_budget] / 100

if __name__ == '__main__':
    datasets = [file for file in os.listdir(os.getcwd()) if file.endswith(".csv")]

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset")
    args = parser.parse_args()
    if args.dataset not in datasets and args.dataset[2:] not in datasets:
        print(f"Erreur: {args.dataset} does not match any csv file in the current directory.")
        exit(1)

    shares = parse_csv_input(args.dataset)

    start_time = time.time()
    best_comb, max_profit = optimized(shares, MAX_BUDGET)
    end_time = time.time()

    print()
    print(f"The best combination is:\n\t{best_comb}")
    print(f"It generates a profit of: {round(max_profit, ndigits=3)}€")
    print(f"For a cost of: {sum(shares[share_name][0] for share_name in best_comb) / 100}€")
    print(f"Results calculated in: {round(end_time - start_time, ndigits=3)} seconds.")
    print()