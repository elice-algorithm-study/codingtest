def solution(board, moves):
    answer = 0
    pick_items = []

    i = 0
    # moves 갯수만큼 반복
    for k in range(len(moves)):
        
        # 위에서부터 1 행씩 돌음
        for depth in board:
            chooseLine = moves[i] - 1
            
            # 칸이 비어있다면
            if depth[chooseLine] == 0:
                continue
            # 칸에 인형이 있다면
            else:
                # 마지막 넣은 인형과 들어올 인형과 다르다면
                if pick_items[-1:] != [depth[chooseLine]]:
                    pick_items.append(depth[chooseLine])    # 바구니에 넣어줌
                # 같다면
                else:
                    pick_items.pop()
                    answer += 2                             # 추가하지 않고 터트림 갯수 + 1                
                depth[chooseLine] = 0                       # board에서 인형 빼줌
                break
        i += 1
        
    return answer
  

"""
def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
"""
