from time import time
def Parse_lib():
    import xmlplain

    with open("Lab3.yaml", 'r', encoding="utf-8") as inf:
        root = xmlplain.obj_from_yaml(inf)
    with open('Res3_Lib.xml', 'w', encoding="utf-8") as outfile:
        xmlplain.xml_from_obj(root, outfile, pretty=True)

def Parse():
    file_in = open("Lab3.yaml", 'r', encoding="utf-8")
    file_out = open('Res3.xml', 'w', encoding="utf-8")
    list_of_text = file_in.readlines()
    list_main_tab = list()
    last_count_space = -1
    for line in list_of_text:
        line = line[: -1]
        peace_of_line = line.split(': ')
        tab_name = peace_of_line[0]
        count_space = peace_of_line[0].count(' ')
        tab_name = tab_name[count_space:]
        tab_body = ': '.join(peace_of_line[1:])
        if last_count_space > count_space:
            file_out.write(' ' * 2 * count_space + '</' + list_main_tab[-1] + '>' + '\n')
            list_main_tab.pop()
        if tab_body == '':
            list_main_tab.append(tab_name[:-1])
            file_out.write(' ' * 2 * count_space + '<' + tab_name[:-1] + '>' + '\n')
        else:
            file_out.write(' ' * 2 * count_space + '<' + tab_name + '>' + tab_body[1:-1] + '</' + tab_name + '>' + '\n')
        last_count_space = count_space
    while len(list_main_tab) > 0:
        last_count_space -= 1
        file_out.write(' ' * 2 * last_count_space + '</' + list_main_tab[-1] + '>' + '\n')
        list_main_tab.pop()
    file_in.close()
    file_out.close()

print('\tWithout libs\t\t\t\tWith libs')

start = time()
for i in range(10):
    Parse()
total_without = time() - start

start = time()
for i in range(10):
    Parse_lib()
total_with = time() - start

print(f'{total_without}\t{("<", ">")[total_without > total_with]}\t{total_with}')