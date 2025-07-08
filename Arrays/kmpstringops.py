def build_lps(pattern: str) -> list[int]:
    """
    Build the Longest Prefix Suffix (LPS) array for KMP algorithm.
    Input: "ABABCABAB"
    Output: [0, 0, 1, 2, 0, 1, 2, 3, 4]
    """
    sl = len(pattern)
    i = 1
    length = 0
    lps = [0] * sl
    # lps[0] is always 0, so we start from i = 1
    while i < sl:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps