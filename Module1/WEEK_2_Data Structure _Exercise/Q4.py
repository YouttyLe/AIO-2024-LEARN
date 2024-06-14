def levenshtein_distance(first_string, second_string):
    global j
    len_string1, len_string2 = len(first_string), len(second_string)
    dp = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]
    for i in range(len_string1 + 1):
        dp[i][0] = i
    for j in range(len_string2 + 1):
        dp[0][j] = j

    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):
            if first_string[i - 1] == second_string[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)

    return dp[len_string1][j]


def main():
    first_string = input("Enter First String: ")
    second_string = input("Enter Second String: ")
    print(levenshtein_distance(first_string, second_string))


if __name__ == "__main__":
    main()
