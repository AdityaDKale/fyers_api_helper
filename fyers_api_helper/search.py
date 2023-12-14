import pandas as pd


def contains_search(substring, string_list, df):
    """
    Perform a 'contains' string search in a list of strings,
    considering words and ignoring whitespaces.

    Parameters:
    - substring (str): The substring to search for.
    - string_list (list): The list of strings to search in.

    Returns:
    - result_df (DataFrame): A DataFrame containing the matched strings,
    their indices, and corresponding symbols.
    """
    def closeness_score(s):
        s_words = s.replace(" ", "").lower().split()
        sub_words = substring.replace(" ", "").lower().split()
        min_distance = float('inf')

        for i in range(len(s_words) - len(sub_words) + 1):
            distance = sum([abs(len(s_words[i + j]) - len(sub_words[j])) for j in range(len(sub_words))])
            min_distance = min(min_distance, distance)

        return min_distance

    result_list = sorted(enumerate(string_list), key=lambda x: closeness_score(x[1]))
    result_list = [(s, df[9][i]) for i, s in result_list if all(word.lower() in s.lower() for word in substring.split())]

    result_df = pd.DataFrame(result_list, columns=['String', 'Symbol'])
    return result_df


def search(max=10):
    database_code = int(input('''
Enter the database code

1: NSE Currency
2: NSE Equity Derivatives
3: NSE Capital Market
4: BSE Capital Market
5: BSE Equity Derivatives
6: MCX Commodity

Enter your choice: '''))

    # Set df based on the user input
    if database_code == 1:
        df = pd.read_csv(
                "https://public.fyers.in/sym_details/NSE_CD.csv",
                header=None)

    elif database_code == 2:
        df = pd.read_csv(
                "https://public.fyers.in/sym_details/NSE_FO.csv",
                header=None)

    elif database_code == 3:
        df = pd.read_csv(
                "https://public.fyers.in/sym_details/NSE_CM.csv",
                header=None)

    elif database_code == 4:
        df = pd.read_csv(
                "https://public.fyers.in/sym_details/BSE_CM.csv",
                header=None)

    elif database_code == 5:
        df = pd.read_csv(
                "https://public.fyers.in/sym_details/BSE_FO.csv",
                header=None)

    elif database_code == 6:
        df = pd.read_csv(
                "https://public.fyers.in/sym_details/MCX_COM.csv",
                header=None)
    else:
        print("Invalid database code. Exiting.")
        return

    my_list = list(df[1])
    search_term = input("Enter your search: ")

    result = contains_search(search_term, my_list, df)

    if len(result) == 0:
        print("\nNot found. Try again with different terms.\n")
    else:
        print(f"\nSearch Results for: '{search_term}'\n")
        print(result.head(max))


if __name__ == "__main__":
    search()
