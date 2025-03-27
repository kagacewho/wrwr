import pandas as pd
import os
import datetime




class logging:
    def true_log(func):
        def wrapper(*args, **kwargs):
            user_login = os.getlogin()
            func_name = func.__name__
            current_date = datetime.datetime.now().strftime('%d %m %Y')
            current_time = str(datetime.datetime.now()).split()[1]

            original_result = func(*args, **kwargs)

            logs = "logs.csv"

            if os.path.isfile(logs):
                file_df = pd.read_csv(logs)
                data = {"":[len(file_df)],"User_Login": [user_login], "Function_name": [func_name], "Date": [current_date], "Time": [current_time]}
                df = pd.DataFrame(data)
                df.to_csv("logs.csv", mode = 'a', index = False, header = False)
            else:
                data = {"":[len(file_df)],"User_Login": [user_login], "Function_name": [func_name], "Date": [current_date], "Time": [current_time]}
                df = pd.DataFrame(data)
                df.to_csv("logs.csv")
            
            return original_result
        return wrapper
    df = pd.read_csv("logs.csv")     
df     
    
            








    #фунция логирования. логирование всех действий - все фунцкии с @log имя польз имя время Все лоши кладем в датафрейм каждый вызов функции любой выгружаем в айл logs.csv        
