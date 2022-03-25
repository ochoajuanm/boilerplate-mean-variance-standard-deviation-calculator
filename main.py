import numpy as np

# mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# Input List 9 digits, convert to 3x3 array
# Less than 9 digits rase ValueError "List must contain nine numbers."

def calculate(list):
    if len(list) != 9:
      raise ValueError('List must contain nine numbers.')
    else:
      matrix = np.array([list[0:3], list[3:6], list[6:9]])
      matrix_transpose = np.transpose(matrix)

      mean_columns = []
      mean_rows = []
      mean_flatten = np.mean(list)

      var_columns = []
      var_rows = []
      var_flatten = np.var(list)

      std_columns = []
      std_rows = []
      std_flatten = np.std(list)

      max_columns = []
      max_rows = []
      max_flatten = np.max(list)

      min_columns = []
      min_rows = []
      min_flatten = np.min(list)

      sum_columns = []
      sum_rows = []
      sum_flatten = np.sum(list)
      
      for row in matrix:
        mean_rows.append(np.mean(row))
        var_rows.append(np.var(row))
        std_rows.append(np.std(row))
        max_rows.append(np.max(row))
        min_rows.append(np.min(row))
        sum_rows.append(np.sum(row))

      for column in matrix_transpose:
        mean_columns.append(np.mean(column))
        var_columns.append(np.var(column))
        std_columns.append(np.std(column))
        max_columns.append(np.max(column))
        min_columns.append(np.min(column))
        sum_columns.append(np.sum(column))

      mean = [mean_columns, mean_rows, mean_flatten]
      var = [var_columns, var_rows, var_flatten]
      std = [std_columns, std_rows, std_flatten]
      max = [max_columns, max_rows, max_flatten]
      min = [min_columns, min_rows, min_flatten]
      sum = [sum_columns, sum_rows, sum_flatten]

      dict = {
          'mean': mean,
          'variance': var,
          'standard deviation': std,
          'max': max,
          'min': min,
          'sum': sum
      }
      
      return dict

if __name__ == '__main__':
    print(calculate([0,1,2,3,4,5,6,7,8]))