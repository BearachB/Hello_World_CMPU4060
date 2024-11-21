def get_data_list():
   data_file = open("GOOG.csv", "r")
   data_list = []  # start with an empty list
   # strip end-of-line, split on commas, and append items to list
   for line_str in data_file:
       data_list.append(line_str.strip().split(','))
   print(len(data_list))
   return data_list

print(get_data_list())


def get_monthly_averages(data_list):
    pass
