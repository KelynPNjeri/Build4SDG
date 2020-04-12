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
  raised_factor = (2 ** factor)
  currently_infected = data['reportedCases'] * 10
  infections_by_requested_time = currently_infected * raised_factor
  severe_cases_by_requested_time = .15 * currently_infected * raised_factor
  hospital_beds_by_requested_time = (data['totalHospitalBeds'] * .35) - severe_cases_by_requested_time
  cases_for_icu_by_requested_time = .05 * ((data['reportedCases'] * 10) * (2 ** factor))
  cases_for_ventilators_by_requested_time = 0.02 * ((data['reportedCases'] * 10) * (2 ** factor))
  dollars_in_flight = int((infections_by_requested_time * .65 * 1.5) / 30)

  output_data = {
    'data': data,
    'impact': {
      'currentlyInfected': currently_infected,
      'infectionsByRequestedTime': infections_by_requested_time,
      'severeCasesByRequestedTime': severe_cases_by_requested_time,
      'hospitalBedsByRequestedTime': hospital_beds_by_requested_time,
      'casesForICUByRequestedTime': cases_for_icu_by_requested_time,
      'casesForVentilatorsByRequestedTime': cases_for_ventilators_by_requested_time,
      'dollarsInFlight': dollars_in_flight
    },
    'severeImpact': {
      'currentlyInfected': data['reportedCases'] * 50,
      'infectionsByRequestedTime': (data['reportedCases'] * 50) * (2 ** factor),
      'severeCasesByRequestedTime': .15 * (data['reportedCases'] * 50) * (2 ** factor),
      'hospitalBedsByRequestedTime': (data['totalHospitalBeds'] * .35) - (.15 * (data['reportedCases'] * 50) * (2 ** factor)),
      'casesForICUByRequestedTime': .05 * ((data['reportedCases'] * 50) * (2 ** factor)),
      'casesForVentilatorsByRequestedTime': 0.02 * ((data['reportedCases'] * 50) * (2 ** factor)),
      'dollarsInFlight': int(((data['reportedCases'] * 50) * (2 ** factor) * .65 * 1.5) / 30)
    }
  } 
  return output_data


if __name__ == "__main__":
   data = {
      'region': {
        'name': "Africa",
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71
      },
      'periodType': "days",
      'timeToElapse': 58,
      'reportedCases': 674,
      'population': 66622705,
      'totalHospitalBeds': 1380614
}
print(estimator(data))
