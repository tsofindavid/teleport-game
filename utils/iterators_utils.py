from typing import List


class IteratorsUtils:
    def get_range(iterates: int, step: int = 1, initial: int = 0) -> List[List[int]]:
        i = initial

        result = []

        while i < iterates:
            result.append([i, i * step])

            i += 1

        return result
