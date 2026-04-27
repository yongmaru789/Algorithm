def solution(record):
    answer = []
    user = {}
    
    for r in record:
        name = r.split()
        if name[0] in ["Enter", "Change"]:
            # name[1] : 유저 아이디 / name[2] : 닉네임
            user[name[1]] = name[2]
    
    for r in record:
        name = r.split()
        if name[0] == "Enter":
            answer.append(user[name[1]] + "님이 들어왔습니다.")
        elif name[0] == "Leave":
            answer.append(user[name[1]] + "님이 나갔습니다.")
    
    
    return answer