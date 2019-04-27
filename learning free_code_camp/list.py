lucky_numbers = [4, 8, 5, 9, 12]
friends = ["Kevin", "Karen", "Kim", "Kade", "Kuzko"]

friends.append("Karol") #adiciona no final
friends.insert(1, "Kelly") #adiciona aonde quiser
friends.remove("Kim") #remove
friends.clear() #limpa tudo
friends.pop() #elimina o último
friends.index("Kevin") #caça a posição do que quiser
friends.count("Kuzao") #conta quantos "" tem na lista
friends.sort()
friends.reverse()

friends2 = friends.copy()

print(friends)