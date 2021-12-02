from numpy import true_divide
import pandas as pd
import matplotlib.pyplot as pyplot

median_marriage_age = pd.read_csv("marriage:divorce_data/median_marriage_age.csv")
median_divorce_age = pd.read_csv("marriage:divorce_data/median_divorce_age.csv")
marriage_divorce_count = pd.read_csv("marriage:divorce_data/marriage_divorce_count.csv")
marriage_divorce_rate = pd.read_csv("marriage:divorce_data/marriage_divorce_rate.csv")

def main():
    
    
    valid = False
    while not valid:
        print()
        choose = int(input("Select a graph(s) to view:\n1) Marriage and Divorce Count\n2) Marriage and Divorce Rate\n3) Median Marriage and Divorce Rate\n"))
        

        if choose == 1:
            count_graph()
            valid = True
        elif choose == 2:
            rate_graph()
            valid = True
        elif choose == 3:
            median_married()
            valid = True
        else:
            print("invalid answer")
            valid = False


def count_graph():
    # Filter for marriage/divorce count to seperate the marriages from divorces
    marriage_filter = (marriage_divorce_count["Marriages_or_Divorces"] == "Marriages")
    divorce_filter = (marriage_divorce_count["Marriages_or_Divorces"] == "Divorces")

    # Apply the filter to the data and plot the graphs
    filtered_married = marriage_divorce_count[marriage_filter]
    lineplot = filtered_married.plot(kind="line", x = "Period", y = "Count", title = "Marriage Count", color = "#004CFF")

    filtered_divorced = marriage_divorce_count[divorce_filter]
    lineplot = filtered_divorced.plot(kind="line", x = "Period", y = "Count", title = "Divorce Count", color = "#FF0000")
    
    pyplot.tight_layout()
    pyplot.show()


def rate_graph():
    # Filter for marriage/divorce rate to seperate the marriages from divorces
    marriage_filter = (marriage_divorce_rate["General Marriage_Rate_and Divorce_Rate"] == "Marriage Rate")
    divorce_filter = (marriage_divorce_rate["General Marriage_Rate_and Divorce_Rate"] == "Divorce Rate")

    # Apply filter and then plot the graphs
    filtered_married = marriage_divorce_rate[marriage_filter]
    barplot = filtered_married.plot(kind = "bar", x = "Period", y = "Count", title = "Marriage Rate")

    filtered_divorced = marriage_divorce_rate[divorce_filter]
    barplot = filtered_divorced.plot(kind = "bar", x = "Period", y = "Count", title = "Divorce Rate", color = "red")

    pyplot.tight_layout()
    pyplot.show()

def median_married():
    
    male_marriage_filter = (median_marriage_age['Male_or_Female'] == 'Male')
    male_marriage_filter = (median_marriage_age[male_marriage_filter]["Period"] == 2010)

    # female_marriage_filter = (median_marriage_age['Male_or_Female'] == 'Female' and median_marriage_age["Status_before_Marriage"] == "Total")
    
   

    line_plot = male_marriage_filter.plot(kind = "bar", x = "Status_before_Marriage", y = "Median_Age_at_Marriage")
    # line_plot = female_marriage_filter.plot(kind = "line", x = "Period", y = "Median_Age_at_Marriage")
   
    pyplot.tight_layout()
    pyplot.show()
    
   

def median_divorce():
    male_divorce_filter = (median_marriage_age['Male_or_Female'] == 'Male')
    female_divorce_filter = (median_marriage_age['Male_or_Female'] == 'Female')
     
   
    pyplot.tight_layout()
    pyplot.show()

main()








