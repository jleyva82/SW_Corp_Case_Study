import matplotlib.pyplot as plt


#data
#years
years = [1950, 1955, 1960, 1965, 1970, 1975,
         1980, 1985, 1990, 1995, 2000, 2005,
         2010, 2015]
#world population *according to wiki
pops = [2.5, 2.8, 3.0, 3.3, 3.7, 4.1,
        4.4, 4.9, 5.3, 5.7, 6.1, 6.5,
        6.9, 7.3]
#world deaths *made up data for learning perpuses
deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7,
          2.9, 3.0, 3.1, 3.3, 3.5, 3.8,
          4.0, 4.3]

#lines as variables
lines = plt.plot(years, pops, years, deaths)      #<years, pops> is line one, <years, deaths> is line two

plt.grid(True)                                    #turn on grid for easy reading
plt.setp(lines, color=(1, .4, .4), marker = "o")  #create plot, with redish hue and "o" markers at data points

#labels
plt.xlabel("Population growth by years")
plt.ylabel('Population in billions')
plt.title("Population Growth")

plt.show()                                        #show plot
