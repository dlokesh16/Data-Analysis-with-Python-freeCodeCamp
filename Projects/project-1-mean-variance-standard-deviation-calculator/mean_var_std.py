import numpy as np

def calculate(list):
  if(list.__len__() == 9):
    input = np.array(list).reshape((3,3))
    
    output = {'mean': [np.mean(input, axis=0).tolist(), np.mean(input, axis=1).tolist(), np.mean(input)],
    'variance': [np.var(input, axis=0).tolist(), np.var(input, axis=1).tolist(), np.var(input)],
    'standard deviation': [np.std(input, axis=0).tolist(), np.std(input, axis=1).tolist(), np.std(input)],
    'max': [np.max(input, axis=0).tolist(), np.max(input, axis=1).tolist(), np.max(input)],
    'min': [np.min(input, axis=0).tolist(), np.min(input, axis=1).tolist(), np.min(input)],
    'sum': [np.sum(input, axis=0).tolist(), np.sum(input, axis=1).tolist(), np.sum(input)]}
  else:
    raise ValueError("List must contain nine numbers.")

  return output