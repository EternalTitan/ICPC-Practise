def check_log_history(events):
    lock_stack = []
    lock_set = set()
    for i in range(len(events)):
        statement = events[i].strip().split()
        if statement[0] == "ACQUIRE":
            if statement[1] in lock_set:
                return i + 1
            else:
                lock_set.add(statement[1])
                lock_stack.append(statement[1])
        else:
            if statement[1] not in lock_set or lock_stack[-1] != statement[1]:
                return i + 1
            else:
                lock_set.remove(statement[1])
                lock_stack.pop()
    if len(lock_stack) > 0:
        return len(events) + 1
    else:
        return 0


a = ["ACQUIRE 123", "ACQUIRE 123", "ACQUIRE 84", "RELEASE 84", "RELEASE 333", "ACQUIRE 333"]
print(check_log_history(a))
