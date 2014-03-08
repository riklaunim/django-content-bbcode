
def b(dic, text):
    for i in dic:
        text = text.replace(i['tag'],  '<b>%s</b>' % i['code'])
    return text


def anchor(dic, text):
    for i in dic:
        href = i['attributes']['href']
        text = text.replace(i['tag'], '<a href="%s">link</a>' % href)
    return text


def test(dic, text):
    for i in dic:
        text = text.replace(i['tag'], 'TEST!')
    return text


registered_tags = {
    'anchor': anchor,
    'b': b,
    'test': test,
}
