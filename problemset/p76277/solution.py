import datetime


class FactorHandler:

    def get_time(self, time_format, time):
        result = {}
        for i in range(0, 3):
            counter = 2
            print('test1')
            if time_format[0] == 'y':
                counter = 4
            print('test2')
            result[time_format[:counter]] = int(time[:counter])
            time_format = time_format[counter+1:]
            time = time[counter+1:]
            print('time_format: ', time_format)
            print('time: ', time)
        print('result: ', result)
        return datetime.date(result['yyyy'], result['mm'], result['dd'])
        # return result
    def __init__(self):
        self.time = {}

    def add_factor(self, time_format, time, value):
        time = self.get_time(time_format, time)
        amount = self.time.get(time) if self.time.get(time) else 0
        self.time[time] = amount + value

    def remove_all_factors(self, time_format, time):
        time = self.get_time(time_format, time)
        self.time.pop(time)

    def get_sum(self, time_format, start_time, finish_time):
        start_time = self.get_time(time_format, start_time)
        finish_time = self.get_time(time_format, finish_time)
        summ = 0
        for key in self.time.keys():
            if start_time <= key <= finish_time:
                summ += self.time[key]
        return summ

