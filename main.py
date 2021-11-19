from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as pyplot

median_marriage_age = pd.read_csv("marriage:divorce_data/median_marriage_age.csv")
median_divorce_age = pd.read_csv("marriage:divorce_data/median_divorce_age.csv")
marriage_divorce_count = pd.read_csv("marriage:divorce_data/marriage_divorce_count.csv")


def main():
    count_graph()

def count_graph():
    
    marriage_plot = marriage_count_plot()
    divorce_plot = divorce_count_plot()
    
 

    pyplot.tight_layout()
    pyplot.show()
         
def marriage_count_plot():
    marriage_filter = (marriage_divorce_count["Marriages_or_Divorces"] == "Marriages")
    filtered_married = marriage_divorce_count[marriage_filter]
    barplot = filtered_married.plot(kind="line", x = "Period", y = "Count", title = "Marriage Count", color = "#004CFF")

    return barplot



def divorce_count_plot():
    divorce_filter = (marriage_divorce_count["Marriages_or_Divorces"] == "Divorces")
    filtered_divorced = marriage_divorce_count[divorce_filter]
    barplot = filtered_divorced.plot(kind="line", x = "Period", y = "Count", title = "Divorce Count", color = "#FF0000")
    
    return barplot

 
main()








