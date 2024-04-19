import pandas as pd
import statistics
import matplotlib.pyplot as plt

df = pd.read_csv("staticAnalysis/ExecutionTimes/sudden.csv")


# we are going to start with the A -B execution time
letters = ["B", "C", "M"]

letters2 = ["B"]

df_F = df[df['activitypair'] == 'H']

for let in letters2:

    column = df_F[let]

    column_list = column.tolist()

    sublists = [column_list[i:i+5] for i in range(0, len(column_list), 5)]

    averages = []
    std = []

    for l in sublists:

        if 0.0 in l:
            l.remove(0.0)

        avg = statistics.mean(l)
        stdev = statistics.stdev(l)

        averages.append(avg)
        std.append(stdev)

    #x = list(range(1, 21))
    x = list(range(1, len(averages) + 1))
    plt.figure(let)
    #plt.plot(x, averages, std)
    plt.plot(x, averages, color='black', label='Average')
    plt.errorbar(x, averages, yerr=std, color='purple', label='STD', fmt='o')

    # Label the axes and add a title
    plt.xlabel('number of window')
    plt.ylabel('AVG/STD in ms')
    #plt.title(f"F and {let}")
    plt.legend()

    #plt.savefig(f"metricsSudden/Band{let}.png")

    averages.clear()
    std.clear()

    plt.show()
 

 