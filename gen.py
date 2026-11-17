# | [Title]({{% ref "06-spring2025#e1"  %}}) | Student Name | Advisor | Tue, May 12 | 8:00 AM | DUE 2168 | [Zoom](https://bit.ly/cis598s24a) |

dates = [
  { 
    "title": "Wed, Dec 16",
    "times" : {
      "8:45 AM": "DUE 2168",
      "9:30 AM": "DUE 2168",
      "10:15 AM": "DUE 2168",
      "11:00 AM": "DUE 2168",
      "11:45 AM": "DUE 2168",
      "1:15 PM": "DUE 2168",
      "2:00 PM": "DUE 2168",
      "2:45 PM": "DUE 2168",
      "3:30 PM": "DUE 2168",
      "4:15 PM": "DUE 2168",
    }
  },
  { 
    "title": "Thur, Dec 17",
    "times" : {
      "8:45 AM": "DUE 2168",
      "9:30 AM": "DUE 2168",
      "10:15 AM": "DUE 2168",
      "11:00 AM": "DUE 2168",
      "11:45 AM": "DUE 2168",
      "1:15 PM": "DUE 2168",
      "2:00 PM": "DUE 2168",
      "2:45 PM": "DUE 2168",
      "3:30 PM": "DUE 2168",
      "4:15 PM": "DUE 2168",
    }
  },
]
sheet = "09-fall2026"
i = 1

first = []
second = []
# third = []

for adate in dates:
  date = adate['title']
  for time, room in adate['times'].items():
    if room == "DUE 2168":
      zoom = '{{% button href="https://bit.ly/cis598s26a" style="primary" color="#512888" %}}Zoom A{{% /button %}}'
      badge = '{{% badge style="primary" title="DUE" %}}2168{{% /badge %}}'
    else:
      zoom = '{{% button href="https://bit.ly/cis598s26b" style="grey" %}}Zoom B{{% /button %}}'
      badge = '{{% badge style="grey" title="DUE" %}}2183{{% /badge %}}'
    first.append(f'| [Title]({{{{% ref "{ sheet }#e{ i }" %}}}}) | Student Name | Advisor | { date } | { time } | { badge } | {zoom} |')
    second.append(f'## Project Name {{#e{ i }}}\n\nStudent Name\n\n![Image](images/placeholder.png)\n\nAbstract')
    i += 1

# print("# Daily Schedule\n")
# print('\n'.join(third))
print("# Full Schedule\n")
print('\n'.join(first))
print("# Project Details\n")
print('\n\n'.join(second))
