from math import dist


n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
h = 'right'
def solution(numbers, hand):
    answer = ''
    num_array = {
        1 : (0, 0), 2: (0, 1), 3 : (0, 2), 
        4 : (1, 0), 5 : (1, 1), 6 : (1, 2), 
        7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
        '*' : (3, 0), 0 : (3, 1), '#' : (3, 2)
    }
    
    leftXY = num_array['*']
    rightXY = num_array['#']
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            leftXY = num_array[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            rightXY = num_array[num]
        else:
            targetXY = num_array[num]
            leftDist = dist(leftXY, targetXY)
            rightDist = dist(rightXY, targetXY)
            if leftDist < rightDist:
                answer += 'L'
                leftXY = num_array[num]
            elif rightDist < leftDist:
                answer += 'R'
                rightXY = num_array[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    leftXY = num_array[num]
                else:
                    answer += 'R'
                    rightXY = num_array[num]
    
    
    return answer

print(solution(n, h))