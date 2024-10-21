from seed import Author, Quote


def get_all_author_quotes(name):
    author = Author.objects(fullname=name).first()
    if not author:
        print(f'No author found with such name "{name}"')
        return
    quotes = Quote.objects(author=author)
    print(f"Quotes of {name}:")
    for quote in quotes:
        print(quote.quote)


def get_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    print(f"Quotes for {tag}:")
    for quote in quotes:
        print(quote.quote)


def get_quotes_by_all_tags(tags):
    quotes = Quote.objects(tags__in=tags)
    print(f"Quotes for {tags}:")
    for quote in quotes:
        print(quote.quote)
