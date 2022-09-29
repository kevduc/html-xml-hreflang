# HTML hreflang ➡ XML Sitemap converter

Convert HTML hreflang tags to a valid XML Sitemap.

Follows the Google Guidelines: [Tell Google about localized versions of your page](https://developers.google.com/search/docs/advanced/crawling/localized-versions).

## 📘 How to use

### 🌐 Online version

https://kevduc.github.io/html-xml-hreflang/

### 🐍 Python script

Run `main.py`, optionally specifying an input and/or output file, for example:

\> `python main.py -i test/test-input.html -o test/test-output.xml`

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
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
  <url>
    <loc>http://en-us.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
  <url>
    <loc>http://en.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
  <url>
    <loc>http://de.example.com/page.html</loc>
    <xhtml:link rel="alternate" hreflang="en-gb" href="http://en-gb.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en-us" href="http://en-us.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="en" href="http://en.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="de" href="http://de.example.com/page.html"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="http://www.example.com/"/>
  </url>
</urlset>

```
## 🎉 Support
<a href="https://www.buymeacoffee.com/kevduc"><img width="20" height="20" src="https://user-images.githubusercontent.com/64347790/193020287-f6bfa3a0-1c31-43e0-92f4-50235b9ff53b.png" title="buymeacoffee.com" /> Buy me a hot chocolate</a>
