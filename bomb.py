import requests
import services
import random

# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# header



print(f"""{cyan}{red}	                                    
                                                     
@@@@@@@    @@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@   
@@!  @@@  @@!  @@@  @@!  @@@  @@! @@! @@!  !@@       
!@   @!@  !@!  @!@  !@!  @!@  !@! !@! !@!  !@!       
@!@!@!@   @!@  !@!  @!@  !@!  @!! !!@ @!@  !!@@!!    
!!!@!!!!  !@!  !!!  !@!  !!!  !@!   ! !@!   !!@!!!   
!!:  !!!  !!:  !!!  !!:  !!!  !!:     !!:       !:!  
:!:  !:!  :!:  !:!  :!:  !:!  :!:     :!:      !:!   
 :: ::::  ::::: ::  ::::: ::  :::     ::   :::: ::   
:: : ::    : :  :    : :  :    :      :    :: : :    
                                                     {end}""")


print()

print(f"{bold}{red}               << Aziz Tairov >>{end}")


print()

# inputs
print('Введите номер телефона без (+7)\nПример: 9018017010')
input_number = input(green + bold + ">> " + end)
print('Количество СМС')
sms = int(input(green + bold + ">> " + end))



def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nЭтот бомбер предназначен только для Российских номеров!")
		quit()
	return number
number = parse_number(input_number)



services.attack(number, sms)