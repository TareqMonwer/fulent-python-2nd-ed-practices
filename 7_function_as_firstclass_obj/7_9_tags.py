def tag(name, *content, class_=None, **attrs):
    """Generate one or more html tags"""
    if class_ is not None:
        attrs['class'] = class_

    attr_n_values = [f'{attr}="{value}"' for attr, value in attrs.items()]
    attrs_as_str = ' '.join(attr_n_values)
    attrs_as_str = ' ' + attrs_as_str if attr_n_values else ''

    if not content:
        return f"<{name} {attrs_as_str}/>"

    tags = []
    for element in content:
        item = f'<{name}{attrs_as_str}>{element}</{name}>'
        tags.append(item)

    return tags


# Single tag
br = tag('br')  # <br />
print(br)
p = tag('p', 'Hello world')  # <p>Hello world</p>
print(p)
li = tag('li', 'one', 'two', class_='numbers', data="{dynamicContent}")
print(li)
"""
<li class="numbers" data="{dynamicContent}">one</li>
<li class="numbers" data="{dynamicContent}">two</li>
"""