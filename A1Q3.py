def string_both_ends(str1):
  if len(str1) < 2:
    return ''

  return str1[:2] + str1[-2:]

print(string_both_ends('Lakshay'))
print(string_both_ends('LJ'))
print(string_both_ends('L'))