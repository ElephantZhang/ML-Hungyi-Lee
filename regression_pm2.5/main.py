train_data_path = '/Users/kyoma/Documents/meachineLearning/data/regression_pm2.5/train.csv'
f = open(train_data_path, 'r', encoding='big5')
lines = []
i = 0
for line in f.readlines():
    lines.append([])
    for word in line.split(','):
        lines[i].append(word)
    i = i+1
f.close

x = []
for i in range(1, len(lines)-1):
    if(lines[2] == 'RAINFALL'):     
