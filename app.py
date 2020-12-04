from ID import ascii_plot

print (ascii_plot([0,5,9,18,7], width=60, height=10))

f = open("plot.txt", "w")
f.write(ascii_plot([0,5,9,18,7], width=60, height=10))
f.close()
