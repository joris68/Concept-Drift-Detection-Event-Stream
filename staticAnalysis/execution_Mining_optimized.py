import pandas as pd
#import numpy as np

df = pd.read_csv("data/recurring_time_noise0_100_baseline.csv")
# convert startTime column to datetime object
df['startTime'] = pd.to_datetime(df['startTime'])

# all directly follows relations
directly_follows_relation = [
    ('A', 'B'), ('A', 'F'), ('B', 'C'), ('C', 'A'), ('D', 'E'), ('E', 'G'),
    ('F', 'D'), ('G', 'H'), ('G', 'I'), ('I', 'J'), ('J', 'K'), ('J', 'L'),
    ('K', 'M'), ('L', 'M'), ('M', 'N'), ('M', 'O')
]
#print(directly_follows_relation[('A', 'B')])

# all cases in the dataset
number_range = range(0,100)

filename = 'ExecutionTimesOptimized/recurringOptimized.csv'
outfile = open(filename, 'w')

outfile.write("case,start,end,timeSpread")
outfile.write('\n')

# für den ganzen dataset
for number in number_range:

     # get dataframe for specific cade
    case_df = df[df['case'] == number]

     # für ein case im dataset
    for x in range(0, len(directly_follows_relation)):
          
          a = directly_follows_relation[x][0]
          b = directly_follows_relation[x][1]

          row1 = case_df[case_df['event'] == a]
          row2 = case_df[case_df['event'] == b]

          if len(row1) >= 1 and len(row2)>= 1 :

                start1 = row1.iloc[0]['startTime']
                start2 = row2.iloc[0]['startTime']


                timeD = abs(start1 - start2)
                result_total = timeD.total_seconds()
                result = round(float(result_total))
          else :
               
               result = "N/A"
          
          outfile.write(str(number))
          outfile.write(',')
          outfile.write(a)
          outfile.write(',')
          outfile.write(b)
          outfile.write(',')
          outfile.write(str(result))
          outfile.write('\n')

outfile.close()