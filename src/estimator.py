def current_number_of_infections(period, period_type):
  factor = 0
  if period_type == 'months':
    month_to_days = int(period) * 30
    factor = month_to_days // 3
  elif period_type == 'weeks':
    weeks_to_days = int(period) * 7
    factor = weeks_to_days // 3
  else:
    factor = int(period) // 3
  return factor

def estimator(data):
  factor = current_number_of_infections(data['timeToElapse'], data['periodType']) 
  output_data = {
    'data': data,
    'estimate': {
      'impact': {
        'currentlyInfected': data['reportedCases'] * 10,
        'infectionsByRequestedTime': (data['reportedCases'] * 10) * (2 ** factor)
      },
      'severeImpact': {
        'currentlyInfected': data['reportedCases'] * 50,
        'infectionsByRequestedTime': (data['reportedCases'] * 50) * (2 ** factor)
      }
    } 
  }
  return output_data
