def solution(board, moves):
    answer = 0
    pick_items = []
    flag = False
    while len(moves) > 0:
        for depth in board:
            chooseLine = moves[0] - 1
            if depth[chooseLine] == 0:
                continue
            else:
                pick_items.append(depth[chooseLine])
                depth[chooseLine] = 0
                del moves[0]
                flag = True
                break
                
        if flag:
            flag = False
            continue
            
        del moves[0]
    
    i = 0
    while i < len(pick_items) - 1:
        if pick_items[i]==pick_items[i+1]:
            del pick_items[i]
            del pick_items[i]
            answer += 2
            i = 0
            continue
        i+=1
        
    return answer
