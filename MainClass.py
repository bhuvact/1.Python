class ClassFirst():
    def Subfields():
        print('Sub-Fields in a Functions are : ')
        print('Machin Learning')
        print('Neural Network')
        print('Vision')
        print('Robotics')
        print('Speech Processing')
        print('Natural Languag Processing')

    def oddEven():
        Input = int(input('Enter an number'))
        if Input % 2 ==0:
            print(Input, 'is even number')
        else:
            print(Input, 'is odd number')

    def Bridedetails():
            Gender = input ('Enter your Gender :')
            Age = int(input('Enter your Age : '))
            if Gender == 'Male' and Age >= 21 :
                print ('You are Eligible for Marriage')
            elif Gender == 'Female' and Age >=18 :
                print ('You are Eligible for Marriage')
            else:
                print('NOT ELIGIBLE')
    def Marks():
            Total = 0
            for i in range(1,6):
                Mark = int(input(f"Subject {i}: Enter the Mark: "))
                Total = Total + Mark
            print('Total mark is : ', Total)
            print('Percentage is : ', float(Total/5))
    
    def Areatriange():
        Height = int (input('Height : '))
        Breadth = int (input('Breadth : '))
        Area = float ((Height * Breadth)/2)
        return Area
    
    def Perimeter():
        Height = int (input('Height 1 : '))
        Height2 = int (input('Height 2 : '))
        Breadth = int (input('Breadth : '))
        Perimeter = Height+Height2+Breadth
        return Perimeter