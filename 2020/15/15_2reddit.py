from array import array
import fileinput


def run(n, lines):
    
    nums = list(map(int, lines[0].split(',')))
    if n <= len(nums):
        return int(nums[n - 1])
    last = nums[-1]
    seen = array('I', (0, ) * (max(n - 1, *nums) + 1))
    for i, x in enumerate(nums[:-1]):
        seen[x] = i + 1
    for i in range(len(nums), n):
        next = i - (seen[last] or i)
        seen[last] = i
        last = next
    return last


def part1(lines):
    
    return run(2020, lines)


def part2(lines):
    
    return run(30000000, lines)


parts = (part1, part2)

if __name__ == '__main__':
    lines = list(fileinput.input())
    print(part1(lines))
    print(part2(lines))
