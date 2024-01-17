#!/usr/bin/env python3

#2-2 paycheck
taxrate = 0.18

print("Pay check Calculator")
print(" ")

hours_work =float(input("hours worked"))
hours_pay =float(input("hourly pay rate"))
print(" ")

gross_pay = hours_pay * hours_work
print(f"Your Gross pay: {gross_pay} ")
print("Tax rate: 18%")

amount= gross_pay * (taxrate / 100)
print(f"Tax amount: {amount} ")
take_home= {gross_pay} - {taxrate}

print(f"Take home Pay: {take_home} ")
