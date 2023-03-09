import re

filename = 'C:/Users/default.LAPTOP-EK651RO7/Desktop/vulnerable1.html'
with open(filename, "r", encoding="utf-8") as f:
    html_content = f.read()

pattern = r"data-href=\"/iucn/species_view/(\d+)\""
matches = re.findall(pattern, html_content)

# Convert matches to strings
matches = [str(int(match)) for match in matches]

print(matches)
