# 23. Troubleshooting Car Issues 

print("Type Y for Yes and N for No.")
q1_silentcar = input("Is the car silent when you turn the key? ")

#Silent car situation 
if q1_silentcar.lower() == "y" :
    q2_silentcar = input("Are the battery terminals corroded? ")
    if q2_silentcar.lower() == "y":
        print("Clean terminals and try starting again.")
    else:
        print("Replace cables and try again.")
    print(q2_silentcar)
else:
    q2_noisecar = input("Does the car make a clicking noise? ")    
    if q2_noisecar.lower() == "y":
        print("Replace the battery.")
    else:
        q3_crank_fail_start = input("Does the car crank up but fail to start? ")
        if q3_crank_fail_start.lower() == "y":
            print("Check spark plug connections.")
        else:
            q4_start_then_die = input("Does the engine start and then die? ")
            if q4_start_then_die.lower() == "y":
                q5_fuel_injection = input("Does your car have fuel injection? ")
                if q5_fuel_injection.lower() == "y":
                    print("Get it in for service.")
                else:
                    print("Check to ensure the choke is opening and closing.")
            else:
                print("Start over.")
