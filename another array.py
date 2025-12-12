# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        station=[
            ['Warrington Bank Quay','WBQ'],
            ['Warrington Central','WAC'],
            ['Warwick','WRW'],
            ['Warwick Parkway','WRP'],
            ['Water Orton','WTO'],
            ['Waterbeach','WBC'],
            ]

        for i in range (0,6):
            print(station[i][1])

        code=input('Please type in a code:')
        for i in range (0,6):
            if code.upper()== station[i][1] :
                print('The station name is:',station[i][0])
                break
            else:
                print('The code is not in the list!')
                break
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        airports=[
            ['BCN','Barcelona International'],
            ['DUB','Dublin'],
            ['LIS','Lisbon'],
            ['LHR','London Heathrow'],
            ['CDG','Paris, Charles De Gaulle'],
            ['PRG','Prague'],
            ['RKV','Reykjavik'],
            ['FCO','Rome, Fiumicino'],
            ]

        
        for i in range (0,8):
            print(station[i][1])
            
        code=input('Please type in a code:')
        
        for i in range (0,8):
            if code== station[i][1] :
                print('The station name is:',station[i][0])
                break
            else:
                print('The code is not in the list!')
                break

        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def three():
    try:
        player=[
            [1,45],
            [2,30],
            [2,46],
            [1,31],
            [1,10],
            [1,32],
            [2,2],
            ]
        red=0
        green=0
        for x in range(0,7):
            if player[x][0] == 2:
                totalRed=red+player[x][1]
                red=player[x][1]
            else:
                totalGreen=green+player[x][1]
                green=player[x][1]
        print('The total score for team red is:',totalRed)
        print('The total score for team green is:',totalGreen)
        pass   
    except Exception as e:
        print("Error occurred:", e )


# [comment]
def four():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )


# [comment]
def main():
    try:
        two()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
