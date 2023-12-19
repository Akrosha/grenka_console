########################################################################
# some fabulous comment
########################################################################

from math import ceil

# this is really terrible shit
def list_like(daList: list,
               name: str = "NaN",
               page: int = 1,
               iterator: int = 5):
    if page > 0 and page <= ceil(len(daList)/iterator):
        daList = [f"({i+1}) {element}" for i, element in enumerate(daList)]
        text = """{} (total: {}):
{}

{} page of {}""".format(
               name,
               len(daList),
               "\n".join(daList[(page - 1)*iterator:(page - 1)*iterator + iterator]),
               page,
               ceil(len(daList)/iterator) )
    else:
        if ceil(len(daList)/iterator) > 0:
            text = f"{page} page is out of range, available pages: 1 - {ceil(len(daList)/iterator)}"
        else:
            text = f"{name} list is empty"
    return text