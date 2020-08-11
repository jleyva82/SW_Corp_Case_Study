import matplotlib.pyplot as plt

years = [1950,
         1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000,
         2005, 2010, 2015]

pops = [2.5, 2.8, 3.0, 3.3, 3.7,
        4.1, 4.4, 4.9, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]   #data of wiki

deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]  #made up data for learning perpuses

plt.plot(years, pops, color=(255/255, 100/255, 100/255), marker="o")
plt.plot(years, deaths, "--", color=(.6, .6, 1), marker="x")


plt.ylabel("Populations in billions")
plt.xlabel("Population growth by year")
plt.title("Population Growth")


plt.show()
