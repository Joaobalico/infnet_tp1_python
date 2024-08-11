# Exercício 10
# Escreva um código que funcione de acordo com o enunciado

# Você está enchendo uma piscina e tem 3 mangueiras. A mangueira vermelha enche em 2 horas, a mangueira azul leva 1,2 hora e a mangueira amarela em 1 hora. Você deseja acelerar o processo usando as três mangueiras. Quanto tempo levará usando todas as mangueiras, em minutos?

# Escreva seu código aqui

# Atribuindo os tempos de cada mangueira às variáveis
time_red = 2
time_blue = 1.2
time_yellow = 1

# Transformando os tempos de cada mangueira em minutos ao invés de horas
minutes_red = 60 * time_red
minutes_blue = 60 * time_blue
minutes_yellow = 60 * time_yellow

# Calculando a taxa de enchimento de cada mangueira em piscinas por minuto
rate_hose_red = 1 / minutes_red
rate_hose_blue = 1 / minutes_blue
rate_hose_yellow = 1 / minutes_yellow

# Somando a taxa de enchimento das mangueiras
rate_host_combined = rate_hose_red + rate_hose_yellow + rate_hose_blue

# Calculando o tempo total em minutos para encher a piscina usando as 3 mangueiras
time = 1 / rate_host_combined

print(time)
