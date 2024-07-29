kg = int(input())

FIVE = 5
THREE = 3

min_bag_count = float('inf')
CAN_MAKE_KG_FLAG = False
for i in range(1001):
    for j in range(1700):
        if FIVE * i + THREE * j == kg:
            bag_count = i + j
            CAN_MAKE_KG_FLAG = True
            
            if bag_count < min_bag_count:
                min_bag_count = bag_count
                
if CAN_MAKE_KG_FLAG:
    print(min_bag_count)

else:
    print('-1')