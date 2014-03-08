
def b(occurrences, text):
    for occurrence in occurrences:
        text = text.replace(occurrence['tag'],  '<b>%s</b>' % occurrence['code'])
    return text


def anchor(occurrences, text):
    for occurrence in occurrences:
        href = occurrence['attributes']['href']
        text = text.replace(occurrence['tag'], '<a href="%s">link</a>' % href)
    return text


def test(occurrences, text):
    for occurrence in occurrences:
        text = text.replace(occurrence['tag'], 'TEST!')
    return text


registered_tags = {
    'anchor': anchor,
    'b': b,
    'test': test,
}
