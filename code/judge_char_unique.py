# @author Huaze Shen
# @date 2020-03-07


def is_unique(astr: str) -> bool:
    count = [0 for i in range(26)]
    for ch in astr:
        pos = ord(ch) - ord('a')
        count[pos] += 1
        if count[pos] > 1:
            return False
    return True


if __name__ == '__main__':
    print(is_unique("leetcode"))
