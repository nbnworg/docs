from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # We have 8 bins
        # Will it work, if, we have Maximum number of times appearing letter first 
        # in bins?
        letter_counts = Counter(word)
        most_common_counts = letter_counts.most_common(26)
        letter_dict = {}
        idx = 1
        for i in range(len(most_common_counts)):
            letter_dict[most_common_counts[i][0]] = idx
            if i % 8 == 7:
                idx += 1

        tap_required = 0
        for i in range(len(word)):
            tap_required += letter_dict[word[i]]

        return tap_required

sol = Solution().minimumPushes("aaaabbccdefghijklmnopqrstuvwxyzzzzzzzzzzz")