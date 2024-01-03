def is_expired(today, theday):
    for today,theday in zip(today.split('.'),theday.split('.')):
        if(int(today)>int(theday)):
            return True
        if(int(today)<int(theday)):
            return False
    return True
        

def add_months(date, months):
    date_split = date.split('.')
    date_y = int(date_split[0])
    date_m = int(date_split[1])
    date_d = int(date_split[2])
    date_m += months
    while date_m > 12:
        date_y += 1
        date_m -= 12
        
    new_date = f"{date_y}.{date_m}.{date_d}"
    return new_date

def solution(today, terms, privacies):
    answer = []
        
    term_dict = {}
    for term in terms:
        t_type, months = term.split()
        term_dict[t_type]=int(months)    
    
    for idx, privacy in enumerate(privacies):
        date, t_type = privacy.split()
        date = add_months(date, term_dict[t_type])
        if is_expired(today, date):
            answer.append(idx+1)     
    return answer