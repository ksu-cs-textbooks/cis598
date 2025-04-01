# | [Title]({{% ref "06-spring2025#e1"  %}}) | Student Name | Advisor | Tue, May 12 | 8:00 AM | DUE 2168 | [Zoom](https://bit.ly/cis598s24a) |

dates = ["Tue, May 13", "Wed, May 14", "Thur, May 15"]
times = ["8:00 AM", "8:45 AM", "9:30 AM", "10:15 AM", "11:00 AM", "11:45 AM", "1:15 PM", "2:00 PM", "2:45 PM", "3:30 PM", "4:15 PM"]
sheet = "06-spring2025"
i = 1

first = []
second = []

for date in dates:
  for time in times:
    first.append(f'| [Title]({{{{% ref "{ sheet }#e{ i }" %}}}}) | Student Name | Advisor | { date } | { time } | DUE 2168 | [Zoom](https://bit.ly/cis598s24a) |')
    second.append(f'## Project Name {{#e{ i }}}\n\nStudent Name\n\n![Image](images/placeholder.png)\n\nAbstract')
    i += 1

print('\n'.join(first))
print('\n\n'.join(second))
