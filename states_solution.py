abbv = 'AK, AL, AR'
print(abbv)

state_abbreviations = abbv.split(',')
print(state_abbreviations)

state_names = 'Alabama, Alaska, Arizona'
print(state_names)

states = state_names.split(',')
print(states)

def createSelectStateHTML(abbrev, state):
  print('<select>')
  for state_code, state_name in
  zip(abbrev, state):
    print('\t<option value="{}">{}</option>'.format(state_code, state_name))
  print('</select>')

createSelectStateHTML(abbv = state_abbreviations, state_names = states)
