import csv
from pybliometrics.scopus import AbstractRetrieval

#ab = AbstractRetrieval("10.1016/j.softx.2019.100263")
#print(ab.title)

'''
ab.idxterms --> termos utilizados para indexar o artigo
ab.authors --> Autores
ab.affiliation --> Instituição a que é afiliada
ab.title --> Titulo
ab.abstract / ab.description --> resumo
'''

def RetrieveCodes(fileName):
    """from txt to list

    Args:
        fileName (string): Name of the file contain the
        codes to the abstracts (.txt file).

    Returns:
        List: List of all the codes in the .txt file.
    """
    
    file = open(fileName, "r")
    codes = []
    for line in file.readlines():
        codes.append(line.strip().split())
    file.close()
    return codes


def RetrieveInformation(codesList):
    """from codes to txt

    Args:
        codesList (_type_): _description_
    """
    pass


def SaveAbstractInformation(absInfo, fileName):
    """from list item to csv

    Args:
        absInfo (List): List of Dict contain the
        abstracts information.
        fileName (string): Name of the .csv file
        were the information will be saved.
    """

    file = open(fileName, 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)
    header = ['Title', 'Idx Terms', 'Abstract', 'Authors', 'Affiliation']
    writer.writerow(header)
    for dic in absInfo:
        writer.writerow([dic['title'], dic['idxterms'], dic['abstract'], dic['authors'], dic['affiliation']])
    file.close()


if __name__ == "__main__":
    pass
    '''print(RetrieveCodes("testCodes.txt"))
    dic1 = {'title': 'Test', 'idxterms': 'gato, sapo, lago', 'abstract': 'descrição aqui', 'authors': 'jorge, julia', 'affiliation': 'instituto'}
    dic2 = {'title': 'Test 2', 'idxterms': 'cachorro, sabonete, rã', 'abstract': 'descrição aqui 2', 'authors': 'jose, narciso', 'affiliation': 'instituto 2'}
    lista = [dic1, dic2]
    print(lista)
    SaveAbstractInformation(lista, 'testCsv.csv')'''