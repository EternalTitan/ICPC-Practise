def question(stickers, target_word, target_counter, sticker_counter, counter):
    if counter == 0:
        ans_found = True
        for i in range(26):
            if target_counter[i] > sticker_counter[i]:
                ans_found = False
                break
        return ans_found
    for each_sticker in stickers:
        for i in each_sticker:
            sticker_counter[ord(i) - ord('a')] += 1
        if question(stickers, target_word, target_counter, sticker_counter, counter - 1):
            return True
        for i in each_sticker:
            sticker_counter[ord(i) - ord('a')] -= 1
    return False


stickers = input().strip().split()
target_word = input().strip()

target_counter = [0 for i in range(26)]
sticker_counter = [0 for i in range(26)]

for i in target_word:
    target_counter[ord(i) - ord('a')] += 1

for i in range(1, len(target_word) + 1):
    if question(stickers, target_word, target_counter, sticker_counter, i):
        print(i)
        exit()
print("something wrong, maybe no sticker has some letter to make it")
