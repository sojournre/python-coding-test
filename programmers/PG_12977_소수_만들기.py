def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum_three = nums[i] + nums[j] + nums[k]
                if is_prime(sum_three):
                    answer += 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return answer


numbers = [1, 2, 7, 6, 4]
print(solution(numbers))
