import pandas

data = pandas.read_csv('squirrel_data.csv')

squirrel_color_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'count': [0, 0, 0]
}

# Get Hold of Column 'Primary Fur Color' with Gray
squirrel_color_dict['count'][0] =len(data[data['Primary Fur Color'] == 'Gray'])

# Get Hold of Column 'Primary Fur Color' with Black
squirrel_color_dict['count'][2] =len(data[data['Primary Fur Color'] == 'Black'])

# Get Hold of Column 'Primary Fur Color' with Cinnamon
squirrel_color_dict['count'][1] =len(data[data['Primary Fur Color'] == 'Cinnamon'])

squirrel_count_frame = pandas.DataFrame(squirrel_color_dict)
squirrel_count_frame.to_csv('color_count.csv')