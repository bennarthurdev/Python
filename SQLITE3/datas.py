import sqlite3 
feriados = [["2018-01-01" , "Confraternizacao Universal"] , ["2018-04-21", "Tiradentes"] , ["2018-05-01" , "Dia do Trabalhador"] , ["2018-09-07" , "Independencia"], ["2018-11-15" , "Proclamacao Republica"], ["2018-12-25" , "Natal"]]

with sqlite3.connect("datas.db" , detect_types=sqlite3.PARSE_DECLTYPES) as conn:
    conn.row_factory = sqlite3.Row
    dict_query = conn.execute('''
        SELECT * FROM feriados
    ''')
    for data in dict_query:
        print(f"{data['data'].strftime(%d/%m)} ,{data['descricao']}")
 