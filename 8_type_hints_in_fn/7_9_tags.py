from typing import Optional, NoReturn


def tag(
    __name: str,
    /,
    *content: str,
    class_: Optional[str] = None,
    **attrs: str
) -> str:
    """Generate one or more html tags"""
    if class_ is not None:
        attrs['class'] = class_

    attr_n_values = [f'{attr}="{value}"' for attr, value in attrs.items()]
    attrs_as_str = ' '.join(attr_n_values)
    attrs_as_str = ' ' + attrs_as_str if attr_n_values else ''

    if not content:
        return f"<{__name} {attrs_as_str}/>"

    tags = []
    for element in content:
        item = f'<{__name}{attrs_as_str}>{element}</{__name}>'
        tags.append(item)

    return '\n'.join(tags)


def stop() -> NoReturn:
    raise RuntimeError('no way')


# Single tag
br = tag('br')  # <br />
print(br)
p = tag("p", "Hello world")  # <p>Hello world</p>
print(p)
li = tag('li', 'one', 'two', class_='numbers', data="{dynamicContent}")
print(li)
"""
<li class="numbers" data="{dynamicContent}">one</li>
<li class="numbers" data="{dynamicContent}">two</li>
"""