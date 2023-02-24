import pandas as pd
import glob
from datetime import timedelta

folder_name = "testdata"
data_file = glob.glob("./"+ folder_name + "/*")
df = pd.DataFrame()

for file in data_file:
    data = pd.read_csv(file)
    df = pd.concat([df, data])

columns_list = ['終了', '開始','機器名']
df[columns_list[0:1]] = df[columns_list[0:1]].astype(str)



def overlap_calc(df, overlap_df, overlap_df_total, car_list):
    overlap_day = set(overlap_df['日付'])
    df = df[df['日付'].isin(overlap_day)]

    start_list = []
    stop_list = []
    overlap_carlist = []
    overlap_daylist = []
    overlap_num = []
    
    overlap_result = pd.DataFrame()

    for day in overlap_day:
        df_day = df[df['日付'] == day]

        for overlap in overlap_df.itertuples():
            overlap_car = list(map(lambda x: x.strip(), overlap[3]))
            overlap_car = set(overlap_car)
            non_overlap_car = car_list.difference(overlap_car)
            df_day_2 = df_day[df_day['機器名'].isin(non_overlap_car)]

            start =  overlap[1]
            stop =  overlap[2]
            non_overlap_car = list(non_overlap_car)

            num = 0
            while num <= (len(non_overlap_car)-1):
                car_2 = non_overlap_car[num]
                df_car_2 = df_day[df_day['機器名'] == car_2]
                num+=1
                for st, sp in zip(df_car_2['開始'], df_car_2['終了']):
                    if start <= sp and stop >= st:
                        overlap_car_list = sorted(list(overlap_car.union({car_2})))
                        condition = [start, stop, st, sp, overlap_car_list, len(overlap_car_list)]
                        if condition[0] >= condition[2] and condition[1] >= condition[3]:
                            start = condition[0]
                            stop = condition[3]

                        elif condition[0] >= condition[2] and condition[1] <= condition[3]:
                            start = condition[0]
                            stop = condition[1]

                        elif condition[0] <= condition[2] and condition[1] >= condition[3]:
                            start = condition[2]
                            stop = condition[3]

                        elif condition[0] <= condition[2] and condition[1] <= condition[3]:
                            start = condition[2]
                            stop = condition[1]

                        else:
                            print('重複が無いデータがあります')

                        start_list.append(start)
                        stop_list.append(stop)
                        overlap_carlist.append(condition[4])
                        overlap_daylist.append(day)
                        overlap_num.append(condition[5])

    overlap_result["開始"] = start_list
    overlap_result['終了'] = stop_list
    overlap_result['重複有_機器名'] = overlap_carlist
    overlap_result['日付'] = overlap_daylist
    overlap_result['重複台数'] = overlap_num
    
    overlap_result['重複有_機器名'] = overlap_result['重複有_機器名'].map(lambda x : str(x).replace("'", "").replace("[", "").replace("]", ""))
    overlap_result = overlap_result.drop_duplicates()
    overlap_result['重複有_機器名'] = overlap_result['重複有_機器名'].map(lambda x : x.split(","))
    overlap_df_total = pd.concat([overlap_df_total, overlap_result])
    
    return df, overlap_result, overlap_df_total



def overlap_calc_all(df, columns_list):

    day_list = []
    for day in list(df['開始']):
        day = str(day).split()
        day_list.append(day[0])

    df['日付'] = day_list
    df['終了'] = pd.to_datetime(df['終了'], format='%Y/%m/%d %H:%M:%S')
    df['開始'] = pd.to_datetime(df['開始'], format='%Y/%m/%d %H:%M:%S')
    day_list = set(day_list)

    columns_list = ['終了', '開始','機器名']
    car_list = set(df['機器名'])


    start_list = []
    stop_list = []
    overlap_carlist = []
    overlap_daylist = []
    overlap_num = []
    overlap_df = pd.DataFrame()

    for day in day_list:
        num = 0
        df_day = df[df['日付'] == day]
        cars = list(car_list)
        
        while num <= (len(cars)-2):
            car_1 = cars[num]
            car_2 = cars[num+1]
            df_car_1 = df_day[df_day['機器名'] == car_1]
            df_car_2 = df_day[df_day['機器名'] == car_2]
            num+=1
            for start, stop in zip(df_car_1['開始'], df_car_1['終了']):
                for st, sp in zip(df_car_2['開始'], df_car_2['終了']):
                    if start <= sp and stop >= st:
                        overlap_car = sorted([car_1, car_2])
                        condition = [start, stop, st, sp, overlap_car, len(overlap_car)]
                        if condition[0] >= condition[2] and condition[1] >= condition[3]:
                            start = condition[0]
                            stop = condition[3]

                        elif condition[0] >= condition[2] and condition[1] <= condition[3]:
                            start = condition[0]
                            stop = condition[1]

                        elif condition[0] <= condition[2] and condition[1] >= condition[3]:
                            start = condition[2]
                            stop = condition[3]

                        elif condition[0] <= condition[2] and condition[1] <= condition[3]:
                            start = condition[2]
                            stop = condition[1]

                        else:
                            print('重複が無いデータがあります')
                            
                        start_list.append(start)
                        stop_list.append(stop)
                        overlap_carlist.append(condition[4])
                        overlap_daylist.append(day)
                        overlap_num.append(condition[5])
                        
    overlap_df["開始"] = start_list
    overlap_df['終了'] = stop_list
    overlap_df['重複有_機器名'] = overlap_carlist
    overlap_df['日付'] = overlap_daylist
    overlap_df['重複台数'] = overlap_num
    overlap_result = overlap_df.copy()
    overlap_df_total = overlap_df.copy()

    number_of_line = len(overlap_result)
    while number_of_line != 0:

        df, overlap_result, overlap_df_total = overlap_calc(df, overlap_result, overlap_df_total, car_list)
        number_of_line = len(overlap_result)


    max_over_lap_num = int(overlap_df_total['重複台数'].max())

    return max_over_lap_num


if __name__ == '__main__':
    max_over_lap_num = overlap_calc_all(df, columns_list)
    print(max_over_lap_num)