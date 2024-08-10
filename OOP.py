def bill():
    try:
        current_reading = int(input("Enter Your current reading : "))
        last_reading = int(input("Enter your last reading : "))
        
        unit = current_reading - last_reading
        if unit <= 0:
            raise Exception("check reading you have entered.")

        if 0 < unit <= 100 :
            net_total = round(total(unit, 4.41 , 0.250))
            
            print( f"Your Expecting bill amount is {net_total} rupees.")
        
        elif 100 < unit <= 300:
            net_total = round(total(100, 4.41 , 0.250) + total((unit - 100), 9.64 , 0.450))
            print( f"Your Expecting bill amount is {net_total} rupees.")

    
    except Exception as e:
        print("Please enter valid unit.")


def total(unit , f , x):
    # f = rate per unit.
    # x = energy transfer rate per unit.
    output =  116 + (f * unit) + (1.17 * unit) + (x * unit) 
    return output + (0.16 * output)



bill()


