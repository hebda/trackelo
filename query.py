import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

def query(site):
    try:
        with urlopen(site) as response:
            soup = BeautifulSoup(response, 'html.parser')
    except:
        print(f"Bad site, skipping: {site}")
        return []
    return parse(soup)

def parse(soup):
    results = []
    date = getDate(soup)

    ## Return nothing if this is a mid-race split
    is_midrace_split = sum(["Split times" in section for section in soup.find_all("h1")]) > 0
    if is_midrace_split:
        return results
    
    ## Track if there are unwanted finals, to be skipped later
    has_unwanted = sum(["U23 Events" in section or "Pre-Programme" in section or "U18 Events" in section
                       for section in soup.find_all("h1")]) > 0
    
    for section in soup.find_all("section"):
        eventname = section.h2.string
        for race in section:
            racename = ""
            rows = []
            for child in race:
                if type(child) != bs4.element.Tag:
                    continue
                if child.name == "span" and classContains(child, "EventResults_eventMeta"):
                    racename = f"{eventname} {child.get_text()}"
                    # print(f"Race: {racename}")
                if child.name == "div" and classContains(child, "EventResults_tableWrap"):
                    # print(f"Result:")
                    for row in child.find_all(attrs={"role": "row"}):
                        rows.append([])
                        is_header = False
                        for ic, cell in enumerate(row):
                            if cell.name not in ["th", "td"]:
                                fatal(f"Thats a weird cell: {cell.name}")
                            rows[-1].append(cell.get_text())
                        # print(rows[-1])
            if "Final" not in racename:
                continue
            if has_unwanted and len(results) > 0: ## skip - logic is that unwanted finals are lower on the page
                continue
            if len(results) > 0: ## merge with previous result
                results[0] = (racename, date, results[0][2]+rows[1:] )
            else:
                results.append( (racename, date, rows) )
    return results

def getDate(soup):
    for calendar in soup.find_all(attrs={"data-name": "eventCalendar-container"}):
        for h3 in calendar.find_all("h3"):
            return h3.get_text()
    fatal("Cannot find date")

def classContains(child, string):
    return any([string in obj for obj in child["class"]])
