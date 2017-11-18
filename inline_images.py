from string import Template

class DoublePercentTemplate(Template):
    delimiter = '%%'

template = DoublePercentTemplate(open('template.js').read())

images = {name: open(f'{name}.svg').read() for name in ['facebook',
                                                        'generic_web_site',
                                                        'github', 'hackernews',
                                                        'keybase', 'reddit']}
print(template.substitute(images))