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

def kmp_search(text: str, pattern: str) -> List[int]:
    """
    KMP algorithm to find all occurrences of pattern in text.
    Input: text = "ABABDABACDABABCABAB", pattern = "ABABCABAB"
    Output: [10]
    """
    if not pattern or not text:
        return []

    lps = build_lps(pattern)
    result = []
    i = j = 0  # i for text, j for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)  # Found a match
            j = lps[j - 1]  # Reset j using LPS

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Use LPS to skip characters
            else:
                i += 1

    return result