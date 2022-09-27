import re
import argparse
import os
import glob

# Parse arguments (input and output file names)
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type=str,
                    help="Input file (file containing a list of HTML link tags) or directory (containing multiple .html files to convert)")
parser.add_argument("-o", "--output", type=str,
                    help="Output file (generated XML Sitemap)")
args = parser.parse_args()

# Default input and output file names
defaultInputFileName = "input.html"
defaultOutputFileName = "output.xml"

# Use default input and output file names if not passed as arguments
inputFileName = args.input if args.input else defaultInputFileName
outputFileName = args.output if args.output else defaultOutputFileName

# If inputFileName is a directory, convert all the html files inside
if os.path.isdir(inputFileName):
    print("Input is a directory, ignoring output file name.")
    inputFileNames = glob.glob(f'{inputFileName}/*.html')
    extensionRegex = re.compile('\.html$', re.IGNORECASE)
    outputFileNames = [extensionRegex.sub(
        ".xml", fileName) for fileName in inputFileNames]
else:
    inputFileNames = [inputFileName]
    outputFileNames = [outputFileName]

# To extract all the html <link> tags and the required attributes
regex = re.compile('\s*<link(?:(?:\s+rel="(?P<rel>.*?)")|(?:\s+hreflang="(?P<hreflang>.*?)")|(?:\s+href="(?P<href>.*?)")|(?:\s+.*?))*?\s*/>',
                   re.MULTILINE | re.IGNORECASE | re.DOTALL)

for i, inputFileName in enumerate(inputFileNames):

    # Read input file
    inputFile = open(inputFileName, "r")
    text = inputFile.read()

    # Extract all the html <link> tags and the required attributes
    links = [link.groupdict() for link in regex.finditer(text)]

    # Default url hreflang value
    defaultHreflang = "x-default"

    # Generate XML output
    newline = "\n"

    alternates = newline.join(
        f'    <xhtml:link rel="{link["rel"]}" hreflang="{link["hreflang"]}" href="{link["href"]}"/>' for link in links)

    output = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{newline.join(f'''  <url>
    <loc>{link["href"]}</loc>
{alternates}
  </url>''' for link in links if link["hreflang"] != defaultHreflang)}
</urlset>
"""

    # Write output file
    outputFile = open(outputFileNames[i], "w")
    outputFile.write(output)
