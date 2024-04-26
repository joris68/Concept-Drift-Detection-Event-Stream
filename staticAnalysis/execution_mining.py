import pandas as pd
#import numpy as np

df = pd.read_csv("Data/synth/recurring_time_noise0_500_baseline.csv")
# convert startTime column to datetime object
df['startTime'] = pd.to_datetime(df['startTime'])

# define tuple for the analysis
# Define two sets of strings
set1 = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'}
set2 = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'}

# Create a matrix of tuples representing the cross-product
cross_matrix = [(item1, item2) for item1 in set1 for item2 in set2]

sorted_tuples = sorted(cross_matrix, key=lambda x: (x[0], x[1]))

# first for all cases ranging from 0 to 99 calculate the completion time to a matrix berween them
number_range = range(0,100)

filename = 'staticAnalysis/ExecutionTimes/sudden_500.csv'
outfile = open(filename, 'w')

outfile.write("case,activitypair,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O")
outfile.write('\n')

# this is for the whole dataset
for number in number_range:

    # get dataframe for specific cade
    case_df = df[df['case'] == number]

    twoDim_matrix = []

    row_in_matrix = []

    # this is for the specific case
    for x in range(0, len(sorted_tuples)):


        if sorted_tuples[x][0] == sorted_tuples[x][1]:

            row_in_matrix.append(0.0)

        else:

            row1 = case_df[case_df['event'] == sorted_tuples[x][0]]
            row2 = case_df[case_df['event'] == sorted_tuples[x][1]]

            # nicht alle activities kommen in jedem case vor...
            if len(row1) >= 1 and len(row2)>= 1 :

                start1 = row1.iloc[0]['startTime']
                start2 = row2.iloc[0]['startTime']


                timeD = abs(start1 - start2)
                result = timeD.total_seconds()
                row_in_matrix.append(round(float(result)))
            
            else:
                row_in_matrix.append(0.0)
        
        if len(row_in_matrix) == 15:

            twoDim_matrix.append(row_in_matrix)
            outfile.write(str(number))
            outfile.write(',')
            outfile.write(str(sorted_tuples[x][0]))
            outfile.write(',')
            for x in range(0, len(row_in_matrix)):
                if x < 14:
                    outfile.write(str(row_in_matrix[x]))
                    outfile.write(',')
                else:
                    outfile.write(str(row_in_matrix[x]))
                    outfile.write('\n')
            row_in_matrix.clear()         

    # ---------------------------------------------------- innere schleife zu ende

    # jetzt wird die vollständige Matrix in den File geschrieben
   
    #outfile.write(f"{str(number)}")
    #outfile.write(',')
    #for row in twoDim_matrix:
     #  outfile.write("[")
      # outfile.write(" ".join(map(str,row))+"\n")
      # outfile.write("]")

    #outfile.write('\n')
# ------------------------------------------------------ äußere schleife zu ende


outfile.close()



        






            


