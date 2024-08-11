# Exercício 3
# Tarefa - Fazer 
# Escreva um programa que produza uma história. A história e a conclusão da história devem sair em várias linhas.

# Tarefa - Fazer

# Escreva um programa que gere uma história com várias linhas.
print("Em uma pequena floresta, havia um coelho chamado Pip.")
print("Pip adorava explorar e fazer novos amigos para poder competir contra.")
print("Um dia, ele encontrou uma tartaruga chamada Tuca.")
print("Juntos, decidiram fazer uma corrida até a colina.")
print("Pip correu rápido, mas Tuca foi constante.")
print("No final, Tuca venceu a corrida, mostrando que a persistência vale a pena.")
print("E assim, Pip aprendeu que a amizade é mais importante que ganhar.")


# Tarefa de extensão 1
# Existe uma maneira de usar uma única instrução de impressão para gerar texto em várias linhas. Crie o programa de história que funciona da mesma forma do que anteriormente, mas usa apenas uma instrução de impressão.#
print("""Em uma pequena floresta, havia um coelho chamado Pip. Pip adorava explorar e fazer novos amigos para poder competir contra. Um dia, ele encontrou uma tartaruga chamada Tuca. Juntos, decidiram fazer uma corrida até a colina. Pip correu rápido, mas Tuca foi constante. No final, Tuca venceu a corrida, mostrando que a persistência vale a pena. E assim, Pip aprendeu que a amizade é mais importante que ganhar.""")


# Tarefa de extensão 2
# Existe uma maneira de adicionar um atraso de tempo no código python. Faça alguma pesquisa e crie um programa de história que produza a história e atrase antes de gerar a conclusão.

from time import sleep
print("""Em uma pequena floresta, havia um coelho chamado Pip. Pip adorava explorar e fazer novos amigos para poder competir contra. Um dia, ele encontrou uma tartaruga chamada Tuca. Juntos, decidiram fazer uma corrida até a colina. Pip correu rápido, mas Tuca foi constante.""")

sleep(5)

print("""No final, Tuca venceu a corrida, mostrando que a persistência vale a pena. E assim, Pip aprendeu que a amizade é mais importante que ganhar.""")
