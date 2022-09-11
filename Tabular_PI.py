def solution(arr):
    PI = []
    var_cnt = arr[0]
    min_int = arr[2:]
    min_bin = init_array(var_cnt)

    for m in min_int:
        m_bin = format(m, "0" + str(var_cnt) + "b")
        min_bin[m_bin.count('1')].append([m_bin, False])

    for circle_size in range(var_cnt):
        combined = []
        combined_bin_raw = []
        for step in range(var_cnt - circle_size):
            for x in min_bin[step]:
                for y in min_bin[step + 1]:
                    tmp = combine(x[0], y[0])
                    if (tmp):
                        if (combined == []):
                            combined = init_array(var_cnt - circle_size - 1)
                        if (not tmp in combined_bin_raw):
                            combined_bin_raw.append(tmp)
                            combined[step].append([tmp, False])
                        x[1] = True
                        y[1] = True
    
        for step in range(len(min_bin)):
            for x in min_bin[step]:
                if not x[1] and not x[0] in PI:
                    PI.append(x[0])
        if combined == []:
            break
        min_bin = combined

    PI.sort()
    return [pi.replace('2', '-') for pi in PI]
    
    
def init_array(one_cnt):
    return [[] for i in range(one_cnt + 1)]

def combine(x, y):
    if (not hammingDistance(x, y)):
        return False
    tmp = 0
    idx = 0
    for char in range(len(x)):
        if x[char] != y[char] and x[char] != 2 and y[char] != 2:
            idx = char
            tmp += 1
        if tmp > 1:
            break
    if tmp == 1:
        tmp_list = list(x)
        tmp_list[idx] = '2'
        return "".join(tmp_list)
    else:
        return False

def hammingDistance(x, y):
    len_x = list(x)
    len_y = list(y)
    count = 0
    rt = True
    for idx in range(len(x)):
        if (int(len_x[idx]) ^ int(len_y[idx]) > 1):
            count += 1
        if count > 1:
            rt = False
            break
    return rt
            

print(solution([50, 50] + [i for i in range(50)]))