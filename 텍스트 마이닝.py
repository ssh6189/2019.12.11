from collections import defaultdict
from collections import OrderedDict

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. …."""

word_count = defaultdict(lambda:0)

for word in text:
    word_count[word] = word_count[word] + 1

    for i, v in OrderedDict(sorted
counter(text)


