import matplotlib.pyplot as plt
players = ['dhoni','virat','rohit','sir jadeja']
scores = [120,140,180,89]
plt.xlabel('players')
plt.ylabel('scores')
#plt.bar(players,scores,label='2020 score of Indian cricket team')
plt.pie(scores,labels=players,explode=(0.2,0,0,0),shadow=True,autopct='%1.1f%%')
plt.grid(color='green')
plt.legend()
plt.show()
