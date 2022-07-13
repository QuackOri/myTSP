# making TSP
import math

# 배달원의 위치
g_sales_man = (2, 8)

# 배달가는 곳의 위치들
a = (5, 8)
b = (10, 4)
c = (-40, 2)
d = (-1, 8)
e = (100, 100)
f = (29, -48)
g = (-50, -50)
h = (1, 1)
i = (90, -90)
j = (50, 8)
delivery_places = [a, b, c, d, e, f, g, h, i, j]

# 추후 배달 우선 순위가 기록될 리스트
g_rank_list = [0 for _ in range(len(delivery_places))]

number_dp = len(delivery_places)
g_rank = 1

# 입력 받은 두 지점 사이의 거리를 구하는 함수
def calc_distance(point_a, point_b):
    sqrt_x = (point_a[0] - point_b[0]) ** 2
    sqrt_y = (point_a[1] - point_b[1]) ** 2
    distance = math.sqrt(sqrt_x + sqrt_y)
    return distance

# calc_distance 함수를 사용해, 입력받은 좌표 리스트와 sales_man과의 거리를 구하고, 그 리스트를 반환
def find_distance(dp):
    distances = []

    for p in dp:
        distance = calc_distance(g_sales_man, p)
        distances.append(distance)

    return distances


# def define_rank(distances):
#     rank_dict = {}
#     rank = 1
#
#     for k in range(len(delivery_places)):
#         rank_dict[k] = 0
#
#     while rank < len(delivery_places) + 1:
#         min_index = distances.index(min(distances))
#         rank_dict[min_index] = rank
#         distances[min_index] = max(distances) + 1
#         rank += 1
#
#     return rank_dict

# 거리들이 적힌 리스트에서 가장 거리가 짧은(가까운) 곳의 인덱스를 반환
def find_close_place(distances):
    return distances.index(min(distances))


# print(define_rank(find_distance(delivery_places)))


# 입력된 area에서 있는 배달지에 대해 우선순위를 찾는다.
# 거리계산 후 가장 가까운 거리로 가고, 그 위치에서 또 가장 가까운 위치를 찾는다.
# 이 방법을 통해 우선순위 리스트를 만든다.
def delivery(area):
    global g_sales_man
    global g_rank

    for _ in range(len(area)):
        delivery_values = [delivery_places[a] for a in area]
        close_place = find_close_place(find_distance(delivery_values))
        g_rank_list[area[close_place]] = g_rank
        g_sales_man = delivery_values[close_place]
        del area[close_place]

        g_rank += 1

# 영역을 나눌 가로선과 세로선을 구하는 함수
# 지금 코드에서는 네부분으로 나눈다.
# 평균값을 기준으로 오른쪽 위가 0번(a), 왼쪽 위가 1번(b), 왼쪽 아래가 2번(c), 오른쪽 아래가 3번(d)이다.
def make_area():
    horizontal = sum([dp[0] for dp in delivery_places]) / number_dp
    vertical = sum([dp[1] for dp in delivery_places]) / number_dp
    return horizontal, vertical

# 각 배달지를 make_area에서 나눈 영역에 따라 나눈다.
def devide_area(horizontal, vertical):
    a = []
    b = []
    c = []
    d = []
    for place in delivery_places:
        if place[0] >= vertical and place[1] >= horizontal:
            a.append(delivery_places.index(place))
        elif place[0] < vertical and place[1] >= horizontal:
            b.append(delivery_places.index(place))
        elif place[0] >= vertical and place[1] < horizontal:
            d.append(delivery_places.index(place))
        else:
            c.append(delivery_places.index(place))
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    return [a, b, c, d]

# 판매원이 있는 영역을 구한다.
def where_is_sales_man(horizontal, vertical):
    if g_sales_man[0] >= vertical and g_sales_man[1] >= horizontal:
        return 0
    elif g_sales_man[0] < vertical and g_sales_man[1] >= horizontal:
        return 1
    elif g_sales_man[0] >= vertical and g_sales_man[1] < horizontal:
        return 3
    else:
        return 2

# 하나의 영역을 모두 배달하고 다음 배달 영역을 찾는 함수이다.
# 이 코드에서는 간단하게 다음 영역을 정할 때 거리를 계산하지 않고
# 시계방향으로 다음 영역으로 넘어가도록 하였다.
def next_array():
    global now_area

    if now_area == 0:
        now_area = 1
    elif now_area == 1:
        now_area = 2
    elif now_area == 2:
        now_area = 3
    else:
        now_area = 0


# 기준선을 만든다.
h, v = make_area()
# 배달지를 영역에 따라 나눈다.
area_array = devide_area(h, v)
# 배달원이 속한 영역을 구한다.
sales_man_area = where_is_sales_man(h, v)

# now_area는 인덱스이고, now_delivery는 list이다.
now_area = sales_man_area
now_delivery = area_array[sales_man_area]
# 영역마다 배달한다.
for _ in range(len(area_array)):
    if not now_delivery:
        next_array()
        now_delivery = area_array[now_area]
        continue
    delivery(now_delivery)
    next_array()
    now_delivery = area_array[now_area]

# 우선 순위를 출력한다.
print(g_rank_list)
