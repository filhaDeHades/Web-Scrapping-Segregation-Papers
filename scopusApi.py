from pybliometrics.scopus import AbstractRetrieval
ab = AbstractRetrieval("10.1016/j.softx.2019.100263")
print(ab.title)


def RetrieveCodes(fileName):
    """from txt to list"""
    pass

def SaveAbstractInformation(code, fileName):
    """from list item to csv"""
    pass