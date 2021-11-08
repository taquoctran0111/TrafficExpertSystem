from os import name
import PySimpleGUI as sg
import main as expert
from db import db

# Thêm background tài xế minh họa
# Mở rộng form
# Xây dựng form view, thêm, sửa, xóa hệ luật

#FORM MAIN

frame = [
    [sg.Text("Tốc độ tối đa: ", size=(12,1)), sg.Text(" ",size=(582,1), key="max_output", text_color="black")], 
    [sg.Text("Tốc độ tối thiểu: ", size=(12,1)), sg.Text(" ",size=(582,1), key="min_output", text_color="black")],
    [sg.Text("Lời khuyên: ", size=(12,1))],
    [sg.Text(" ",size=(700,4), key="advice_output", text_color="black")]
]
col1 = [
    [sg.Image(filename="images/logo.png", key = "images", size=(270,200))],
]
col2 = [
    [sg.Checkbox('Có phương tiện trong vòng 100m phía trước', default=False, key="safety")],
    [sg.Text("Số làn: ", size=(35,1)), sg.Radio('Một làn', "RADIO1", default=True, key="1lane"), sg.Radio('Hai làn', "RADIO1", default=False, key="2lane"), sg.Radio('Ba làn', "RADIO1", default=False, key="3lane")],
    [sg.Text("Phương tiện đang lưu thông trên làn: ", size=(35,1)), sg.Radio('Không chia làn', "RADIO2", default=True, key="lane-n"), sg.Radio('Làn trái', "RADIO2", default=False, key="lane-l"), sg.Radio('Làn giữa', "RADIO2", default=False, key="lane-c"), sg.Radio('Làn phải', "RADIO2", default=False, key="lane-r")],
    [sg.Text("Tầm nhìn nhỏ hơn: ", size=(35,1)), sg.Radio('Không bị hạn chế', "RADIO3", default=True, key="without"), sg.Radio('200m', "RADIO3", default=False, key="200m"), sg.Radio('100m', "RADIO3", default=False, key="100m"), sg.Radio('50m', "RADIO3", default=False, key="50m")],
    [sg.Text("Trạng thái đường đi: ", size=(35,1)), sg.Checkbox('Đường trơn trượt', default=False, key="slippery"), sg.Checkbox('Địa hình quanh co, đèo dốc', default=False, key="highpass")],
    [sg.Button("Tư vấn"), sg.Button("Hệ luật"), sg.Button("Thêm hệ luật")]
]

layout = [
    [sg.Text("------ ĐIỀU KIỆN ĐƯỜNG VÀ HIỆN TRẠNG GIAO THÔNG")],
    [sg.Text(" ")],
    [sg.Column(col1, element_justification='c'), sg.Column(col2)],
    [sg.Frame("Kết quả tư vấn", frame, key='-FRAME-')]
]

window = sg.Window("Tư vấn tốc độ xe", layout, size=(1000,480))

while True:
    event, values = window.read()

    def get_facts():
        facts = ['Freeway']

        if values["safety"]:
            facts.append("Safety distance 100 meters")
        if values["2lane"]:
            facts.append("Two lanes")
        if values["3lane"]:
            facts.append("Three lanes")
        if values["lane-l"]:
            facts.append("Left lane")
        if values["lane-c"]:
            facts.append("Middle lane")
        if values["lane-r"]:
            facts.append("Right lane")
        if values["200m"]:
            facts.append("200m")
        if values["100m"]:
            facts.append("100m")
        if values["50m"]:
            facts.append("50m")
        if values["slippery"]:
            facts.append("Slippery")
        if values["highpass"]:
            facts.append("High pass")
        
        return facts

    #FORM MAIN
    if event == "Tư vấn":
        facts = get_facts()
        rules = db.get_rules()
        Max, Min, Advice = expert.test_one_case(rules, facts)
        print("Max speed: ", Max, end=" km/h \n")
        print("Min speed: ", Min, end=" km/h \n")
        print("Advice: ", Advice)
        window['max_output'].update(str(Max)+" km/h")
        window['min_output'].update(str(Min)+" km/h")
        
        if len(Advice) > 0:
            t = ''
            if 'Open lights' in Advice:
                t += '- Yêu cầu bật đèn!\n'
            if 'Leave ASAP' in Advice:
                t += '- Tầm nhìn quá thấp, rời khỏi đường cao tốc tại lối ra gần nhất!\n'
            if 'Slippery' in Advice:
                t += '- Đường trơn trượt, yêu cầu đi chậm lại!\n'
            if 'High pass' in Advice:
                t += '- Điều kiện đường xấu, giảm tốc độ phương tiện và đảm bảo khoảng cách an toàn!\n'
            window['advice_output'].update(t)
        else:
            window['advice_output'].update("- Đảm bảo khoảng cách an toàn giữa các phương tiện!")

    #FORM VIEW RULES
    if event == "Hệ luật":
        data_list_rules = db.get_rules()
        input = []
        output = []
        for i in range(0, len(data_list_rules)): 
            input.append(data_list_rules[i]['IF'])
            output.append(data_list_rules[i]['THEN'])
        data_rules= list(zip(input, output))
        layout_view_rules = [
            [sg.Text("Các tập luật")],
            [sg.Table(data_rules, headings=['IF','THEN'], justification='left', max_col_width=30, enable_events=True)],
            [sg.Text("Tên luật: "),sg.In(key="name_rule") ,sg.Button("Xóa"), sg.Button("Sửa")]
        ]

        window_rules = sg.Window("Hệ luật", layout_view_rules, size=(600,300))
        while True:
            event1, values1 = window_rules.read()

            #DELETE RULE
            if event1 == "Xóa":
                name_rule = values1["name_rule"]
                if name_rule == "":
                    sg.Popup("Yêu cầu nhập tên luật cần xóa!")
                else:
                    db.delete_rule(name_rule)
                    sg.Popup("Xóa thành công!")


            #FORM EDIT RULE
            if event1 == "Sửa":
                name_rule = values1["name_rule"]
                if name_rule == "":
                    sg.Popup("Yêu cầu nhập tên luật cần sửa!")
                else:
                    rule = db.get_one_rule(name_rule)
                    input = rule["IF"]
                    max_sp = rule["THEN"]["Max"]
                    min_sp = rule["THEN"]["Min"]
                    advice = rule["THEN"]["Advice"]
                    layout_edit_rule = [
                        [sg.Text("SỬA LUẬT")],
                        [sg.Text("Điều kiện: ", size=(20,1)), sg.Input(key="rule", default_text=input)],
                        [sg.Text("Tốc độ tối đa (km/h): ", size=(20,1)), sg.Input(key="max_sp", default_text=max_sp)],
                        [sg.Text("Tốc độ tối thiểu (km/h): ", size=(20,1)), sg.Input(key="min_sp", default_text=min_sp)],
                        [sg.Text("Lời khuyên: ", size=(20,1)), sg.Input(key="advice", default_text=advice)],
                        [sg.Button("Sửa")]
                    ]
                    
                    window_edit_rule = sg.Window("Sửa hệ luật", layout_edit_rule, size=(500,300))
                    while True:
                        event3, values3 = window_edit_rule.read()
                        if event3 == "Sửa":
                            try:
                                max_sp_new = values3["max_sp"]
                                min_sp_new = values3["min_sp"]
                                advice_new = values3["advice"]
                                if min_sp_new == "" or min_sp_new=="" or advice_new=="":
                                    sg.Popup("Không được để trống!")
                                else:
                                    db.update_rule(name_rule, max_sp_new, min_sp_new, advice_new)
                                    sg.Popup("Sửa thành công!")
                            except:
                                sg.Popup("Sửa không thành công!")
                        if event3 == sg.WIN_CLOSED:
                            break 
            if event1 == sg.WIN_CLOSED:
                break
    
    #FORM ADD RULE
    if event == "Thêm hệ luật":
        layout_add_rule = [
            [sg.Text("THÊM LUẬT")],
            [sg.Text("Điều kiện: ", size=(20,1)), sg.In(key="rule")],
            [sg.Text("Tốc độ tối đa (km/h): ", size=(20,1)), sg.In(key="max_sp")],
            [sg.Text("Tốc độ tối thiểu (km/h): ", size=(20,1)), sg.In(key="min_sp")],
            [sg.Text("Lời khuyên: ", size=(20,1)), sg.In(key="advice")],
            [sg.Button("Thêm")]
        ]
        window_add_rule = sg.Window("Thêm hệ luật", layout_add_rule, size=(500,300))
        while True:
            event2, values2 = window_add_rule.read()
            if event2 == "Thêm":
                rule = values2["rule"]
                max_sp = values2["max_sp"]
                min_sp = values2["min_sp"]
                advice = values2["advice"]
                if rule=="" or max_sp=="" or min_sp=="" or advice=="":
                    sg.Popup("Yêu cầu nhập đầy đủ thông tin!")
                else:
                    data = db.json_data(rule, max_sp, min_sp, advice)
                    db.add_rule(data)
                    sg.Popup("Thêm thành công!")
                     
            if event2 == sg.WIN_CLOSED:
                break
                
    if event == sg.WIN_CLOSED:
        break