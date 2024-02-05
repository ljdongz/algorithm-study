from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    
    lastTime = 23 * 60 + 59 # 23:59
    inoutRecord = defaultdict(list)
    parkingFee = defaultdict(int)
    
    for record in records:
        time, number, state = record.split(" ") # 시간, 차량번호, 내역(in,out)
        hour, minute = time.split(":")
        totalMinutes = int(hour) * 60 + int(minute)
        inoutRecord[number].append((totalMinutes, state))

    
    for number, record in inoutRecord.items():
        # 입차 후 출차를 하지 않은 경우
        if len(record) % 2 != 0:
            record.append((lastTime, "OUT"))

        inTime = 0 # 입차 시간
        during = 0 # 총 남아있던 시간

        for minute, state in record:
            # 입차인 경우
            if state == "IN":
                inTime = minute
            # 출차인 경우
            else:
                during += minute - inTime

        # 기본 시간 이하로 있었던 경우
        if during <= fees[0]:
            parkingFee[number] += fees[1]
        # 기본 시간을 초과한 경우
        else:
            parkingFee[number] += fees[1] + (math.ceil((during - fees[0]) / fees[2])) * fees[3]
        
    parkingFee = sorted(parkingFee.items())
    for _, fee in parkingFee:
        answer.append(fee)

    return answer