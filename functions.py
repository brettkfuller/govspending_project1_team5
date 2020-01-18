import pycountry

def get_country_name(isocode3):
    try:
        name = pycountry.countries.get(alpha_3=isocode3).name
        return name
    except:
        return None

    
def plotter(df, x, y):
    x_axis = df[x]
    y_axis = df[y]
    plt.title(f"{x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.scatter(x_axis, y_axis, marker='o', facecolors="steelblue", edgecolors="black", alpha=0.75)
    plt.grid()
    #plt.savefig(f"output_data/Latitude_Vs_{factor}.png")
    plt.show()
    
# Function to create Linear Regression plots
# I designed this function to accept two parameters, a (1) factor/variable, and (2) if it's northern hemisphere or southern hemisphere
# The function parameters defaults to Max Temp and Northern Hemisphere, if no parameters are passed
def linregplotter( factor='Max Temp', where='north'):
    # The plt clf will CLear out the Figure settings, for reusability
    plt.clf()
    if where == "north":
        x_values = northern_df["Lat"]
        y_values = northern_df[f'{factor}']
    elif where == "south":
        x_values = southern_df["Lat"]
        y_values = southern_df[f'{factor}']
    
    # Calcluation of linear regression given x and y values
    slope, intercept, rvalue, pvalue, stderr = linregress(x_values, y_values)
    regression_values = x_values * slope + intercept
    line_eq = f"y = {round(slope, 2)}x + {round(intercept,2)}"
    print(f"The r-squared (absolute) is :{abs(rvalue)}\n")
    
    #Plot proper
    plt.scatter(x_values, y_values, facecolors="steelblue")
    plt.plot(x_values, regression_values, 'r-')
    plt.annotate(line_eq, (min(x_values)+5, min(y_values)+5), fontsize=15, color="red")

    plt.title(f"Latitude vs. {factor} Plot (as of {today})")
    plt.xlabel("Latitude")
    plt.ylabel(f"{factor} Plot")
    plt.savefig(f"output_data/LinReg_Latitude_Vs_{factor}_{where.title()}.png")
    plt.show()