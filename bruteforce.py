import os
import time
import csv
import itertools
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
                cost = int(float(row[1]))
                profit = cost * float(row[2]) / 100
                shares[name] = (cost, profit)
    return shares


def bruteforce(shares, budget):
    """
    Take a list of shares (with a name, a cost and a profit) and return the best
    combination of them given a budget (500€ by default).
    User itertools combinations to try every single possible combination of shares
    for combination size from 1 to len(shares).
    Complexity is O(2**len(shares)), very unefficient.
    """
    max_budget = budget
    best_comb = None
    max_profit = 0

    for comb_size in range(1, len(shares) + 1):
        for comb in itertools.combinations(shares.keys(), comb_size):
            comb_cost = sum(shares[share_name][0] for share_name in comb)
            comb_profit = sum(shares[share_name][1] for share_name in comb)

            if comb_cost <= max_budget and comb_profit > max_profit:
                max_profit = comb_profit
                best_comb = comb
    return best_comb, max_profit

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
    best_comb, max_profit = bruteforce(shares, MAX_BUDGET)
    end_time = time.time()

    print()
    print(f"The best combination is:\n\t{best_comb}")
    print(f"It generates a profit of: {round(max_profit, ndigits=3)}€")
    print(f"For a cost of: {sum(shares[share_name][0] for share_name in best_comb)}€")
    print(f"Results calculated in: {round(end_time - start_time, ndigits=3)} seconds.")
    print()
