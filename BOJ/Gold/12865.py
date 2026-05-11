import sys
input = sys.stdin.readline

N, K = map(int, input().split())

things = []
for _ in range(N):
    things.append(list(map(int, input().split())))

things.sort(reverse=True)
# bag[가치] = 무게
bag = {0: 0}

for weight, value in things:
    tmp = {}
    for bag_value, bag_weight in bag.items():
        next_value = bag_value + value
        next_weight = bag_weight + weight

        if next_weight <= K:
            # 기존에 저장된 무게(next_bag_value)가 있으면 가져오고, 없으면 비교에서 무조건 지게 큰 값(K+1)을 가져온다. 
            # 더 적은 무게로 같은 가치를 만들 수 있는 경우에만 갱신
            if bag.get(next_value, K+1) > next_weight:
                tmp[next_value] = next_weight

    # 이번 물건을 추가해서 만든 새로운 물건 조합을 기본 가방에 합친다. 
    bag.update(tmp)

print(max(bag.keys()))
