def current_number_of_infections(period, period_type):
  factor = 0
  days = 0
  if period_type == 'months':
    days = int(period) * 30
    factor = days // 3
  elif period_type == 'weeks':
    days = int(period) * 7
    factor = days // 3
  else:
    factor = int(period) // 3
    days = period
  return factor, days

def estimator(data):
  factor, days = current_number_of_infections(data['timeToElapse'], data['periodType']) 
  
  output_data = {
    'data': data,
    'impact': {
      'currentlyInfected': data['reportedCases'] * 10,
      'infectionsByRequestedTime': (data['reportedCases'] * 10) * (2 ** factor),
      'severeCasesByRequestedTime': int(.15 * (data['reportedCases'] * 10) * (2 ** factor)),
      'hospitalBedsByRequestedTime': int((data['totalHospitalBeds'] * .35) - (.15 * (data['reportedCases'] * 10) * (2 ** factor))),
      'casesForICUByRequestedTime': int(.05 * ((data['reportedCases'] * 10) * (2 ** factor))),
      'casesForVentilatorsByRequestedTime': int(0.02 * ((data['reportedCases'] * 10) * (2 ** factor))),
      'dollarsInFlight': int((((data['reportedCases'] * 10) * (2 ** factor)) * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)
    },
    'severeImpact': {
      'currentlyInfected': data['reportedCases'] * 50,
      'infectionsByRequestedTime': (data['reportedCases'] * 50) * (2 ** factor),
      'severeCasesByRequestedTime': int(.15 * (data['reportedCases'] * 50) * (2 ** factor)),
      'hospitalBedsByRequestedTime': int((data['totalHospitalBeds'] * .35) - (.15 * (data['reportedCases'] * 50) * (2 ** factor))),
      'casesForICUByRequestedTime': int(.05 * ((data['reportedCases'] * 50) * (2 ** factor))),
      'casesForVentilatorsByRequestedTime': int(.02 * ((data['reportedCases'] * 50) * (2 ** factor))),
      'dollarsInFlight': int((((data['reportedCases'] * 50) * (2 ** factor)) * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / days)
    }
  } 
  return output_data
