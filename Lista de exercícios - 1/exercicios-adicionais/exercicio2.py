tempo = int(input("Por favor, entre com o número de segundos que deseja converter:"))

d = tempo // (24*60*60)
h = (tempo % (24*60*60)) // (60*60)
m = ((tempo % (24*60*60)) % (60*60)) // 60
s = ((tempo % (24*60*60)) % (60*60)) % 60

print(d, "dias,", h, "horas,", m, "minutos e", s, "segundos.")