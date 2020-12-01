# frontmatter_keywords
A script that will extract keywords from a markdown file and update the frontmatter in that file to hold the keywords

## Installation
```
git clone frontmatter_keywords
cd frontmatter_keywords
pip3 install -r requirements.txt
```

## Quickstart
Run:
```
# head -5 samples/enchiridion.md
---
title: The Enchiridion
author: Epictetus
translator: Thomas Wentworth Higginson
---

# python3 frontmatter_keywords.py -c 3 -e enchiridion.md
[must entirely quit, every unpleasing semblance, concerns anything beyond]

# head -5 samples/enchiridion.md
---
title: The Enchiridion
author: Epictetus
translator: Thomas Wentworth Higginson
keywords: [must entirely quit, every unpleasing semblance, concerns anything beyond]
``` 

