def solution(id_list, report, k):
    answer = []
    
    reported_num = {}
    check_report = {}
    
    for user in id_list:
        reported_num[user] = 0
        
    save_user = reported_num.copy()
    tmp_user = reported_num.copy()
    
    for user in id_list:
        tmp_dict = reported_num.copy()
        check_report[user] = tmp_dict
        
    for data in report:
        data = data.split()
        if check_report[data[0]][data[1]]==0:
            check_report[data[0]][data[1]] += 1
            reported_num[data[1]] += 1
        else:
            continue
    
    for key in reported_num:
        if reported_num[key] >= k:
            save_user[key] = 1

    for key in save_user:
        if save_user[key]==1:
            for user in check_report:
                if check_report[user][key]==1:
                    tmp_user[user] += 1
        
    for key in tmp_user:
        answer.append(tmp_user[key])

    return answer
