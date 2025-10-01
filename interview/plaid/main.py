class AccountInfo:
    def __init__(self):
        self.account_info = {}

    def add_bank(self, bank: str, account: list[str], interval: int) -> None:
        if bank not in self.account_info:
            self.account_info[bank] = (interval, account)

    def get_accounts_to_update(self, timestamp: int) -> dict[str, list[str]]:
        result = {}
        for bank in self.account_info:
            if timestamp % self.account_info[bank][0] == 0:
                result[bank] = self.account_info[bank][1]
        return result


class AccountInfo2:
    def __init__(self):
        self.account_info = {}

    def add_bank(self, bank: str, account: list[str], interval: int) -> None:
        if bank not in self.account_info:
            self.account_info[bank] = (interval, account)

    def get_accounts_to_update(self, timestamp: int) -> dict[str, list[str]]:
        result = {}
        for bank in self.account_info:
            interval = self.account_info[bank][0]
            account_num = len(self.account_info[bank][1])
            total_update = account_num // interval
            if (
                account_num % interval > 0
                and timestamp % interval < account_num % interval
            ):
                total_update += 1
            result[bank] = []
            for i in range(total_update):
                result[bank].append(
                    self.account_info[bank][1][i * interval + timestamp % interval]
                )
        return result


if __name__ == "__main__":
    # test1 = AccountInfo()
    # test1.add_bank("Chase", ["username_1", "username_2"], 10)
    # assert test1.account_info == {"Chase": (10, ["username_1", "username_2"])}
    # test1.add_bank("Wells Fargo", ["username_3"], 20)
    # assert test1.account_info == {
    #     "Chase": (10, ["username_1", "username_2"]),
    #     "Wells Fargo": (20, ["username_3"]),
    # }
    # assert test1.get_accounts_to_update(0) == {
    #     "Chase": ["username_1", "username_2"],
    #     "Wells Fargo": ["username_3"],
    # }
    # assert test1.get_accounts_to_update(0) == {
    #     "Chase": ["username_1", "username_2"],
    #     "Wells Fargo": ["username_3"],
    # }
    # assert test1.get_accounts_to_update(5) == {}
    # assert test1.get_accounts_to_update(5) == {}
    # assert test1.get_accounts_to_update(10) == {"Chase": ["username_1", "username_2"]}
    # assert test1.get_accounts_to_update(20) == {
    #     "Chase": ["username_1", "username_2"],
    #     "Wells Fargo": ["username_3"],
    # }
    # assert test1.get_accounts_to_update(20) == {
    #     "Chase": ["username_1", "username_2"],
    #     "Wells Fargo": ["username_3"],
    # }
    # assert test1.get_accounts_to_update(0) == {
    #     "Chase": ["username_1", "username_2"],
    #     "Wells Fargo": ["username_3"],
    # }
    test2 = AccountInfo2()
    # test2.add_bank("Chase", ["username_1", "username_2"], 2)
    # assert test2.account_info == {"Chase": (2, ["username_1", "username_2"])}
    # test2.add_bank("Wells Fargo", ["username_3", "username_4", "username_5"], 3)
    # print(test2.account_info)
    # assert test2.get_accounts_to_update(0) == {"Chase": ["username_1"], "Wells Fargo": ["username_3"]}
    test2.add_bank("Chase", ["username_1", "username_2", "3", "4", "5", "6"], 4)
    for i in range(10):
        print(test2.get_accounts_to_update(i))
    # assert test2.get_accounts_to_update(0) == {"Chase": ["username_1"], "Wells Fargo": ["username_3"]}
"""
// Adds a bank with a list of accounts to the scheduler with the
// given interval (in seconds). Returns nothing.
add_bank(bank: string, accounts: Array<string>, interval: int) => void

// Returns a mapping from banks to lists of accounts to update at
// the given timestamp.
get_accounts_to_update(timestamp: int) => Map<string, Array<string>>
Suppose we have two banks, "Chase" and "Wells Fargo". "Chase" has an update
interval of 10 seconds, and "Wells Fargo" has an update interval of 20 seconds.
"Chase" has accounts "username_1" and "username_2". "Wells Fargo" has account
"username_3".

At T=0, all three accounts should be updated.
At T=5, no accounts should be updated.
At T=10, accounts "username_1" and "username_2" should be updated.
At T=20, all three accounts should be updated.

Suppose we have one bank, "Chase". "Chase" has an update interval of 3 seconds,
and has accounts "username_1", "username_2", "username_3", "username_4", and
"username_5".

At T=0, "username_1" and "username_2" should be updated.
At T=1, "username_3" and "username_4" should be updated.
At T=2, "username_5" should be updated.
At T=3, "username_1" and "username_2" should be updated.

"""
