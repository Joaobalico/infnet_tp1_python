# Exercício 8
# No código abaixo, são mostradas algumas linhas para manipulação de números em horas. Adicione os comentários apropriados para deixar o código mais inteligível.

# O código foi gerado inicialmente por causa desse enunciado:

# Você está enchendo uma piscina e tem duas mangueiras. A mangueira verde enche em 1,5 horas e a mangueira azul em 1,2 horas. Você deseja acelerar o processo usando as duas mangueiras. Quanto tempo levará usando as duas mangueiras, em minutos?

# Por fim, preveja qual vai ser o valor da variável time, escrevendo a resposta como comentário

# Adicione seu comentário aqui

# Atribuindo os tempos de cada mangueira às variáveis
time_green = 1.5
time_blue = 1.2

# Adicione seu comentário aqui
# Transformando os tempos de cada mangueira em minutos ao invés de horas
minutes_green = 60 * time_green
minutes_blue = 60 * time_blue

# Adicione seu comentário aqui
# Calculando a taxa de enchimento de cada mangueira em piscinas por minuto
rate_hose_green = 1 / minutes_green
rate_hose_blue = 1 / minutes_blue

# Adicione seu comentário aqui
# Somando a taxa de enchimento das duas mangueiras
rate_host_combined = rate_hose_green + rate_hose_blue

# Adicione seu comentário aqui
# Calculando o tempo total em minutos para encher a piscina usando ambas as mangueiras
time = 1 / rate_host_combined

# Escreva neste comentário qual será o valor de time no final da execução do código

# Resposta
# O valor de time será 40.0