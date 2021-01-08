# import module
import dcstyleconstant as dcs
from dcstyleconstant import TextFormation
from dcstyleconstant import Language


# work with heading tag
def heading_tag(text, level=1):
    """
        Return heading tag using level. Here we create variant of heading tag.
        We use first variant because of SEO. 
    """

    return f"<h{level}>{text}</h{level}>"
    # return f'<p class="{TextFormation.headings[level-1]}">{text}</p>'


def codeblock(code, language):
    style_code = f"""
    <pre><code class="{Language.py}">
    {code}
    </code></pre>
    """
    print(type(style_code))
    return style_code


def link():
    pass


def images():
    pass


def mark():
    pass


if __name__ == "__main__":
    # read file
    file = open('input.md')
    lines = file.readlines()
    code = str()
    idx = 0

    while idx < (len(lines)):
        # grab heading
        line = lines[idx]

        if line[0] == '#':
            idx = idx + 1
            level = line.count('#')
            line = line[level:].strip()
            # print(heading_tag(line, level))

        # grab codeblock
        if lines[idx][:3] == '```':
            language = lines[idx][3:]
            idx = idx + 1

            while True:
                if lines[idx][:3] != '```':
                    code += lines[idx] + '\r'
                else:
                    break
                idx += 1
            print(codeblock(code, language))

        if lines[idx] is not None:
            print(lines[idx])
            idx += 1
