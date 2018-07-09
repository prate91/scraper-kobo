# scraper-kobo

For many application is interesting to get information from the web. This scraper help us to get from Kobo some information about books, authors and their correlation.

## Installation


In order to install the package just download (or clone) the current project and copy the scraper-kobo folder in the root of your application.

Scraper-kobo is written in python and requires the following package to run:
- random
- bs4
- urllib

## Implementation details


# Execution

The algorithm can be used as standalone program as well as integrated in python scripts.

## Standalone

```bash

python scraperKobo.py filename iterations
```

where:
* *filename*: list of starting list 
* *iterations*: number of iterations for each link

Scraper-kobo results will be saved on two files. You have to choose the name of the files when the program starts

### Input file specs 
List of urls: an url for each row. The file format is .txt.

Example:
```
link1
link2
...
linkn
```
