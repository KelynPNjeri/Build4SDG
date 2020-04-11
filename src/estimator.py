def estimator(data):
  reported_cases = 0
  for key, value in data.items():
    if key == 'reportedCases':
        reported_cases = value
  
  output_data = {
    'data': data,
    'impact': {
      'currentlyInfected': reported_cases * 10
    },
    'severeImpact': {
      'currentlyInfected': reported_cases * 50
    }
  }
  return output_data
