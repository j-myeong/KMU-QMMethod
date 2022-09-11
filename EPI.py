PI_with_Info = []

def solution(arr):
    PI = find_PI(arr)
    min_num = arr[2:]
    without_num = []
    EPI = []
    for min in min_num:
        if (min in without_num): 
            continue
        only_cover_check = 0
        cover_idx = 0
        for idx in range(len(PI)):
            if min in PI_with_Info[idx][2]:
                only_cover_check += 1
                cover_idx = idx
            if (only_cover_check > 1):
                break
        if only_cover_check == 1 and not PI[cover_idx] in EPI:
            without_num += PI_with_Info[cover_idx][2]
            EPI.append(PI[cover_idx])
    return PI + ['EPI'] + EPI

def find_PI(arr):
    PI = []
    var_cnt = arr[0]
    min_int = arr[2:]
    min_bin = init_array(var_cnt)

    for m in min_int:
        m_bin = format(m, "0" + str(var_cnt) + "b")
        min_bin[m_bin.count('1')].append([m_bin, False, [m]])

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
                            combined[step].append([tmp, False, x[2] + y[2]])
                        x[1] = True
                        y[1] = True
        for step in range(len(min_bin)):
            for x in min_bin[step]:
                if not x[1] and not x[0] in PI:
                    PI.append(x[0])
                    PI_with_Info.append(x)
        if combined == []:
            break
        min_bin = combined

    PI.sort()
    PI_with_Info.sort(key=lambda x:x[0])
    for i in range(len(PI)):
        PI[i] = PI[i].replace('2', '-')
        PI_with_Info[i][0] = PI[i]
    return PI
    
    
def init_array(one_cnt):
    return [[] for i in range(one_cnt + 1)]

def combine(x, y):
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