from itertools import permutations

def generate_numbers(numbers):
    results = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        print(perms)
        for perm in perms:
            number = int(''.join(perm))
            print(number)
            results.add(number)
    print(results)
    return results

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    results = generate_numbers(numbers)

    count = 0
    for number in results:
        if prime(number):
            count += 1

    print(count)
    return count

if __name__ == '__main__':
    generate_numbers('17')