def solution(new_id): 
  special_ch = '-_.~!@#$%^&*()=+[{]}:?,<>/' 

  new_id = new_id.lower() 
  answer = '' 
  
  for i in range(len(new_id)): 
    if new_id[i] in special_ch and new_id[i] not in '-_.': 
      continue 
    answer+=new_id[i] 
    
  while(-1 != answer.find('..')): answer = answer.replace('..', '.')
  
  answer = answer.strip('.') 
  
  if len(answer) >= 16: 
    answer = answer[0:15].strip('.')
  
  if len(answer) == 0: 
    answer = 'a' 
   
  while len(ans) <= 2: 
    answer += answer[-1] 
  
  return answer
