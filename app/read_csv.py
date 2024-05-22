import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

    '''
    ya existe un metodo que pasa los datos a diccionarios
    data = csv.DictReader(file,delimiter=',')
    '''

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])