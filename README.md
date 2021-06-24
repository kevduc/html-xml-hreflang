# html-xml-hreflang

Convert HTML hrefelang tags to a valid XML Sitemap.

Follows the Google Guidelines: [Tell Google about localized versions of your page](https://developers.google.com/search/docs/advanced/crawling/localized-versions).

## 📘 How to use

Run `main.py`, optionally specifying an input and/or output file, for example:

\> `python main.py -i test-input.html -o test-output.xml`

> Defaults to `input.html` for the input file and `output.xml` for the output file if not specified

## 👇 Example

### `input.html`

```html
<link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html" />
<link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html" />
<link rel="alternate" hreflang="en" href="http://en.example.com/page.html" />
<link rel="alternate" hreflang="de" href="http://de.example.com/page.html" />
<link rel="alternate" hreflang="x-default" href="http://www.example.com/" />
```

### `output.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>http://en-gb.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
  <url>
    <loc>http://en-us.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
  <url>
    <loc>http://en.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
  <url>
    <loc>http://de.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
</urlset>
```
