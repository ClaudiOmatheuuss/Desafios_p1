# 7. Faça programa que leia uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit. 

temp_celsius = round(float(input("Digite a temperatura em °C: ")), 1)

temp_fahrenheit = (temp_celsius * 1.8) + 32
print(f"Temperatura: {temp_fahrenheit}°F")