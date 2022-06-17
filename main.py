import math

def getlocation(ob:list,radius:list) -> list:
    left1 = (ob[0][0] - ob[1][0]) * (ob[1][1] - ob[2][1])
    left2 = (ob[1][0] - ob[2][0]) * (ob[0][1] - ob[1][1])
    left_result = left1 - left2

    right1_1 = math.pow(ob[0][0],2) + math.pow(ob[0][1],2) - math.pow(radius[0],2)
    right1_2 = math.pow(ob[1][0],2) + math.pow(ob[1][1],2) - math.pow(radius[1],2)
    right1 = (right1_1 - right1_2) * (ob[1][1] - ob[2][1])

    right2_1 = math.pow(ob[1][0],2) + math.pow(ob[1][1],2) - math.pow(radius[1],2)
    right2_2 = math.pow(ob[2][0],2) + math.pow(ob[2][1],2) - math.pow(radius[2],2)
    right2 = (right2_1 - right2_2) * (ob[0][1] - ob[1][1])
    right_result = (right1 - right2) / 2

    x = right_result / left_result
    y = ((ob[1][0] - ob[0][0]) / (ob[0][1] - ob[1][1]) * x) + (right1_1 - right1_2) * 2 * (ob[0][1] - ob[1][1]) #error


    return [x,y]

def main():
    print("input the obsercations' location")
    ob_location = [list(map(int, input().split())) for _ in range(3)]
    print("input distance from observations")
    d = list(map(int,input().split())) 
    location = getlocation(ob_location,d)
    print(*location)

if __name__ == "__main__":
    main()
