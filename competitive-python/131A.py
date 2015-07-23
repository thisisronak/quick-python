string = raw_input()
string_up = string.upper()
if string[1:] == string_up[1:]:
  if string[0] == string_up[0]:
    print string.lower()
  else:
    print string_up[0] + string[1:].lower()
else:
  print string