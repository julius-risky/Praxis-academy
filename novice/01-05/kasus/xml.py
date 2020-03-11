import xml.dom.minidom as minidom

def main():
    # gunakan fungsi parse() untuk me-load xml ke memori 
    # dan melakukan parsing
    doc = minidom.parse("F:\\Praxis-academy\\novice\\01-05\\kasus\\biodata.xml")

    # Cetak isi doc dan tag pertamanya
    print (doc.nodeName)
    print (doc.firstChild.tagName)

    name = doc.getElementsByTagName("name")[0].firstChild.data
    umur = doc.getElementsByTagName("umur")[0].firstChild.data
    email = doc.getElementsByTagName("email")[0].firstChild.data
    list_hobi= doc.getElementsByTagName("hobi")
    print ("Nama: {}\numur: {}\nemail: {}\n".format(name, umur, email))

    print ("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print ("-", hobi.getAttribute("name"))
if __name__ == "__main__":
    main()