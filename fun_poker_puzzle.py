from operator import itemgetter

HAND_SIZE = 5
LOWEST_RANK = 10
POKER_HAND_RANK = {1: "royal-flush", 2: "straight-flush", 3: "four-of-a-kind", 4: "full-house", 5: "flush",
                   6: "straight",
                   7: "three-of-a-kind", 8: "two-pairs", 9: "one-pair", 10: "highest-card"}


def get_value_of_card(val):
    if val == 'A':
        return 14
    elif val == 'K':
        return 13
    elif val == 'Q':
        return 12
    elif val == 'J':
        return 11
    elif val == 'T':
        return 10
    else:
        return ord(val) - ord('0')


def is_flush(sorted_hand):
    for i in range(HAND_SIZE - 1):
        if sorted_hand[i][1] != sorted_hand[i + 1][1]:
            return False
    return True


def is_straight(sorted_hand):
    for i in range(HAND_SIZE):
        if sorted_hand[0][0] == 2 and i + 1 == HAND_SIZE and sorted_hand[HAND_SIZE - 1][0] == 14:
            return True
        if sorted_hand[i][0] != sorted_hand[0][0] + i:
            return False
    return True


def is_straight_flush(sorted_hand):
    if is_straight(sorted_hand):
        if is_flush(sorted_hand):
            return True
    return False


def is_royal_flash(sorted_hand):
    if is_straight_flush(sorted_hand):
        if sorted_hand[0][0] == 10:
            return True
    return False


def is_four_of_a_kind(sorted_hand):
    if sorted_hand[0][0] == sorted_hand[3][0] or sorted_hand[1][0] == sorted_hand[4][0]:
        return True
    else:
        return False


def is_full_house(sorted_hand):
    if sorted_hand[0][0] == sorted_hand[2][0] and sorted_hand[3][0] == sorted_hand[4][0]:
        return True
    if sorted_hand[0][0] == sorted_hand[1][0] and sorted_hand[2][0] == sorted_hand[4][0]:
        return True
    return False


def is_three_of_a_kind(sorted_hand):
    for i in range(HAND_SIZE - 2):
        if sorted_hand[i][0] == sorted_hand[i + 2][0]:
            return True
    return False


def get_different_pair_count(sorted_hand):
    pair_found = 0
    card_dict = {}
    for i in sorted_hand:
        if i[0] not in card_dict:
            card_dict[i[0]] = 1
        else:
            card_dict[i[0]] += 1
    for i in card_dict:
        if card_dict[i] == 2:
            pair_found += 1
    return pair_found


def is_two_pair(sorted_hand):
    if get_different_pair_count(sorted_hand) == 2:
        return True
    else:
        return False


def is_pair(sorted_hand):
    if get_different_pair_count(sorted_hand) == 1:
        return True
    else:
        return False


def get_current_hand(hand):
    sorted_hand = sorted(hand, key=itemgetter(0))
    # if is_royal_flash(sorted_hand):
    #     return 1
    if is_straight_flush(sorted_hand):
        return 2
    if is_four_of_a_kind(sorted_hand):
        return 3
    if is_full_house(sorted_hand):
        return 4
    if is_flush(sorted_hand):
        return 5
    if is_straight(sorted_hand):
        return 6
    if is_three_of_a_kind(sorted_hand):
        return 7
    if is_two_pair(sorted_hand):
        return 8
    if is_pair(sorted_hand):
        return 9
    return 10


def get_rank(data, to_drop, hand_pointer, deck_pointer, hand):
    if hand_pointer == HAND_SIZE:
        return get_current_hand(hand)
    ret = LOWEST_RANK
    if hand_pointer + to_drop < HAND_SIZE:
        hand.append(data[hand_pointer])
        ret = min(ret, get_rank(data, to_drop, hand_pointer + 1, deck_pointer, hand))
        hand.pop(-1)
    if to_drop > 0:
        hand.append(data[HAND_SIZE + deck_pointer])
        ret = min(ret, get_rank(data, to_drop - 1, hand_pointer + 1, deck_pointer + 1, hand))
        hand.pop(-1)
    return ret


def main(data):
    rendered_data = []
    for i in data:
        rendered_data.append((get_value_of_card(i[0]), i[1]))

    ans = LOWEST_RANK
    for i in range(HAND_SIZE + 1):
        ans = min(ans, get_rank(rendered_data, i, 0, 0, []))
    ret = 'Hand: '
    # print('hand: ',end='')
    for i in range(HAND_SIZE):
        ret += data[i] + ' '
    ret += 'Deck: '
    for i in range(HAND_SIZE):
        ret += data[HAND_SIZE + i] + ' '
    ret += 'Best hand: ' + POKER_HAND_RANK[ans]

    return ret


if __name__ == '__main__':
    while True:
        try:
            original_data = input()
            if original_data == '':
                break
            original_data = original_data.strip().split()
            print(main(original_data))
        except:
            break
