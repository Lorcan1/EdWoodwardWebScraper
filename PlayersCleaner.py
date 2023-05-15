from pandas import read_csv


class PlayersCleaner:
    def clean(self,dataframe):
        dataframe = self.name_cleaner(dataframe)
        dataframe['Height'] = dataframe['Height'].map(lambda x: x.split('CM')[0].strip())
        dataframe['Weight'] = dataframe['Weight'].map(lambda x: x.split('KG')[0].strip())
        dataframe['int_caps'] = dataframe['Caps/ Goals'].map(lambda x: x.split('/')[0])
        dataframe['int_goals'] = dataframe['Caps/ Goals'].map(lambda x: x.split('/')[1])

        #dataframe = dataframe.iloc[:, 1:]
        col = dataframe.pop("Unique ID")
        dataframe.insert(0, col.name, col)

        col = dataframe.pop("int_caps")
        dataframe.insert(dataframe.columns.get_loc("Caps/ Goals") + 1, col.name, col)


        col = dataframe.pop("int_goals")
        dataframe.insert(dataframe.columns.get_loc("Caps/ Goals") + 2, col.name, col)

        dataframe = dataframe.drop("Caps/ Goals", axis=1)

        dataframe['sell_value'] = dataframe['sell_value'].str.replace('Not for sale', '-100')
        dataframe['sell_value'] = dataframe['sell_value'].str.replace('€', '')
        dataframe['Wages'] = dataframe['Wages'].str.replace('€', '')
        dataframe['Wages'] = dataframe['Wages'].str.replace('pw', '')

        return dataframe

    def name_cleaner(self, dataframe):
        # dataframe['First Name'] = dataframe['Name'].map(lambda x: x.split(' ')[0].strip())
        # dataframe['Surname'] = dataframe['Name'].map(lambda x: x.split(' ')[1].strip())
        # if name is one - surname is name and first name is blank
        # if name is two - surname is second and first name is first
        # if name is three
        #     if second is de then surname is second and third while firstname is first
        #     else surname is third and first name is first and second
        dfToList = dataframe['Name'].tolist()
        first_name = []
        second_name = []

        names = [x.split() for x in dfToList]
        for name in names:
            if len(name) == 1:
                first_name.append('-')
                second_name.append(name[0])
            elif len(name) == 2:
                first_name.append(name[0])
                second_name.append(name[1])
            elif len(name) == 3:
                first_name.append(name[0])
                if name[1] in ['De']:
                    second_name.append(name[1]+ ' ' + name[2])
                else:
                    first_name.append(name[1])
                    second_name.append(name[2])

        dataframe['first_name'] = first_name
        col = dataframe.pop("first_name")
        dataframe.insert(dataframe.columns.get_loc("Name") + 1, col.name, col)

        dataframe['second_name'] = second_name
        col = dataframe.pop("second_name")
        dataframe.insert(dataframe.columns.get_loc("Name") + 2, col.name, col)

        dataframe = dataframe.drop("Name", axis=1)

        return dataframe

# if __name__ == '__main__':
#     playercleaner = PlayersCleaner()
#
#     dataframe = read_csv("outfield.csv")
#     playercleaner.clean(dataframe)
