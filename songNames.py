file = open('FavoriteSongs.txt', 'w')

Songs = {'SB' : 'Carried Away', 'RHCP' : 'Dani California', 'NIN' : 'The Perfect Drug', 'Tool' : 'Schism'}

for item in Songs:
    file.write(f"{item} : {Songs[item]}\n")

file.close()
print("Favorite songs have been written to FavoriteSongs.txt")