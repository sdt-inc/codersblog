# import module
import dcstyleconstant as dcs
from dcstyleconstant import TextFormation

# read file
file = open('input.md')

# work with heading tag
def heading_tag(text, level=1):
    """
        Return heading tag using level. Here we create variant of heading tag.
        We use first variant because of SEO. 
    """

    return f"<h{level}>{text}</h{level}>"
    # return f'<p class="{TextFormation.headings[level-1]}">{text}</p>'   


for line in file.readlines():
    if line[0] == '#':
        level = line.count('#')
        line = line[level:].strip()
        print(heading_tag(line, level))
