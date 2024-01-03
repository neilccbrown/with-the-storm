# On windows, pipe to clip to get on clipboard straight away
from decimal import *
import difflib
from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
import requests
from bs4 import BeautifulSoup

from buildings import And, Or
from resources import *

ingredient_grammar = Grammar(
    """
    ws = ~" *"
    resource = ~"[A-Za-z][A-Z a-z]+[A-Za-z]"
    amount = ~"[0-9]+"
    amount_resource = "Farm Fields" / (amount ws resource) 
    output = amount_resource (amount "%" ws resource)?
    or_list = amount_resource (ws "|" ws or_list)*
    """
)

class Ingredient_Visitor(NodeVisitor):
    def generic_visit(self, node, visited_children):
        return visited_children or node.text
    def visit_amount(self, node, visited_children):
        return int(node.text)
    def visit_amount_resource(self, node, visited_children):
        if node.text.lower() == "farm fields":
            return (1, "FARM_FIELD")
        amount, _, resource = visited_children[0]
        matches = difflib.get_close_matches(resource.upper(), ALL_RESOURCES)
        if len(matches) == 0:
            raise Exception(f"Unknown resource: {resource}")
        return (amount, matches[0].upper())
    def visit_output(self, node, visited_children):
        primary = visited_children[0]
        if visited_children[1]:
            amount, _, _, resource = visited_children[1][0]
            matches = difflib.get_close_matches(resource.upper(), ALL_RESOURCES)
            if len(matches) == 0:
                raise Exception(f"Unknown resource: {resource}")
            return [primary, (str(Decimal(amount) / Decimal(100)), matches[0].upper())]
        else:
            return primary
    def visit_or_list(selfself, node, visited_children):
        items = [visited_children[0]]
        if visited_children[1]:
            sub = visited_children[1][0][3]
            if isinstance(sub, Or):
                items.extend(sub.items)
            else:
                items.append(sub)
        if len(items) > 1:
            return Or(items)
        else:
            return items[0]
def parse_output(text):
    #print(f"Parsing {text}")
    return Ingredient_Visitor().visit(ingredient_grammar["output"].parse(text))
def parse_input(text):
    #print(f"Parsing {text}")
    return Ingredient_Visitor().visit(ingredient_grammar["or_list"].parse((text.replace("OR", "|"))))

# Convert to string without the quotes around each capitalised ingredient:
def to_src(x):
    match x:
        case And(items):
            return f"And([{', '.join([to_src(y) for y in items])}])"
        case Or(items):
            return f"Or([{', '.join([to_src(y) for y in items])}])"
        case (n, var):
            return f"({n}, {var})"
        case [((n,var), (n2, var2))]:
            return f"[({n}, {var}), ({n2}, {var2})]"

# For testing:
#print(to_src(Ingredient_Visitor().visit(ingredient_grammar["or_list"].parse("2 Crystalized Dew|3 Berries| 5 Ale"))))
#raise Exception("Testing only!")

# Map buildings from wiki to game name
BUILDING_NAME_MAP = {
    "Alchemist's Hut": "Alchemist Hut",
    "Teahouse": "Tea House",
    "Small Farm": "SmallFarm",
    "Forester's Hut": "Grove",
    "Druid's Hut": "Druid",
}

def fetch_building(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = None
    for caption in soup.find_all('caption'):
        if caption.get_text().strip() == 'Produced':
            table = caption.find_parent('table')
            break
    if not table:
        return
    title = soup.find("span", {"class": "mw-page-title-main"}).get_text()
    title = BUILDING_NAME_MAP.get(title, title)
    print (f"    \"{title}\": [")
    for row in table.find('tbody').find_all('tr'):
        cols = row.find_all('td')
        if len(cols) == 0:
            continue # Header or footer row
        outcome = parse_output(cols[0].get_text().strip())
        if len(cols) > 3:
            requirements = [parse_input(cols[3].get_text().strip())]
            if len(cols) >= 5 and cols[4].get_text().strip():
                requirements.append(parse_input(cols[4].get_text().strip()))
            if len(cols) >= 6 and cols[5].get_text().strip():
                requirements.append(parse_input(cols[5].get_text().strip()))
            if len(requirements) == 1:
                print(f"        ({to_src(requirements[0])}, {to_src(outcome)}),")
            else:
                print(f"        ({to_src(And(requirements))}, {to_src(outcome)}),")
        elif isinstance(outcome, list):
            for o in outcome:
                # Raw building, just print output:
                print(f"        {o[1]},")
        else:
            # Raw building, just print output:
            print(f"        {outcome[1]},")
    print("    ],")

urls = ["https://against-the-storm.fandom.com/wiki/Category:Food_Production", "https://against-the-storm.fandom.com/wiki/Category:Industry"]
fetched = {}
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all("a", {"class": "category-page__member-link"}):
        if not ("File:" in link.get_text()) and not ("Industry" in link.get_text()):
            if link["href"] not in fetched:
                fetch_building("https://against-the-storm.fandom.com" + link['href'])
                fetched[link['href']] = True