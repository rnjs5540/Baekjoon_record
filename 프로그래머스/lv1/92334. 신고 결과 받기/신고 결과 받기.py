def solution(id_list, reports, k):
    who_reported_me:dict[str, list[str]] = {}
    for id in id_list:
        who_reported_me[id] = []

    report_counts:dict[str, int] = {}
    for id in id_list:
        report_counts[id] = 0

    mail_counts:dict[str, int] = {}
    for id in id_list:
        mail_counts[id] = 0
    
    for report in reports:
        reporter, reportee = report.split()
        if reporter not in who_reported_me[reportee]:
            who_reported_me[reportee].append(reporter)
            report_counts[reportee] += 1

    for id in id_list:
        if report_counts[id] >= k:
            for reporter in who_reported_me[id]:
                mail_counts[reporter] += 1

    return list(mail_counts.values())
