def getPowerNumber(index):
    class node():
        def __init__(self, basic_value, power_value):
            self.basic_value = basic_value
            self.power_value = power_value

    def get_smallest(min_heap):
        smallest = min_heap[1]
        min_heap[1] = min_heap[len(min_heap) - 1]
        min_heap.pop(-1)
        i = 1
        while i * 2 < len(min_heap):
            if i * 2 + 1 < len(min_heap):
                if min_heap[i].power_value < min_heap[i * 2].power_value and min_heap[i].power_value < min_heap[
                    i * 2 + 1].power_value:
                    break
                elif min_heap[i * 2].power_value < min_heap[i * 2 + 1].power_value:
                    temp = min_heap[i]
                    min_heap[i] = min_heap[i * 2]
                    min_heap[i * 2] = temp
                    i = i * 2
                else:
                    temp = min_heap[i]
                    min_heap[i] = min_heap[i * 2 + 1]
                    min_heap[i * 2 + 1] = temp
                    i = i * 2 + 1
            else:
                if min_heap[i].power_value < min_heap[i * 2].power_value:
                    break
                else:
                    temp = min_heap[i]
                    min_heap[i] = min_heap[i * 2]
                    min_heap[i * 2] = temp
                    i = i * 2
        min_array[smallest.basic_value] += 1
        min_heap.append(node(smallest.basic_value, min_array[smallest.basic_value] ** smallest.basic_value))
        i = len(min_heap) - 1
        while i > 1:
            parent = i // 2
            if min_heap[i].power_value < min_heap[parent].power_value:
                temp = min_heap[parent]
                min_heap[parent] = min_heap[i]
                min_heap[i] = temp
                i = parent
            else:
                break
        return smallest.power_value

    power_number_set = set()
    min_array = [2 for i in range(50)]
    min_heap = [0]
    counter = -1
    for i in range(2, 50):
        min_heap.append(node(i, 2 ** i))
    while counter < index:
        ans = get_smallest(min_heap)
        if ans not in power_number_set:
            counter += 1
            power_number_set.add(ans)
    return ans


if __name__ == '__main__':
    for i in range(10):
        print(getPowerNumber(i))
