def grosspay(hour,rate):
    if hour <= 40:
        pay = hour*rate
    else:
        extra = hour - 40
        pay = (40*rate)+(extra*rate*1.5)
    return pay

hour = float(input("How many hours have you worked? "))
rate = float(input("How much are you paid hourly? "))

print(grosspay(hour,rate))
