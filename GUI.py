import PySimpleGUI as sg
import main as expert

frame = [
    [sg.Text("Tốc độ tối đa: ", size=(12,1)), sg.Text(" ",size=(582,1), key="max_output", text_color="black")], 
    [sg.Text("Tốc độ tối thiểu: ", size=(12,1)), sg.Text(" ",size=(582,1), key="min_output", text_color="black")],
    [sg.Text("Lời khuyên: ", size=(12,1))],
    [sg.Text(" ",size=(700,4), key="advice_output", text_color="black")]
]

layout = [
    [sg.Text("------ ĐIỀU KIỆN ĐƯỜNG VÀ HIỆN TRẠNG GIAO THÔNG")],
    [sg.Text(" ")],
    [sg.Checkbox('Có phương tiện trong vòng 100m phía trước', default=False, key="safety")],
    [sg.Text("Số làn: ", size=(35,1)), sg.Radio('Một làn', "RADIO1", default=True, key="1lane"), sg.Radio('Hai làn', "RADIO1", default=False, key="2lane"), sg.Radio('Ba làn', "RADIO1", default=False, key="3lane")],
    [sg.Text("Phương tiện đang lưu thông trên làn: ", size=(35,1)), sg.Radio('Không chia làn', "RADIO2", default=True, key="lane-n"), sg.Radio('Làn trái', "RADIO2", default=False, key="lane-l"), sg.Radio('Làn giữa', "RADIO2", default=False, key="lane-c"), sg.Radio('Làn phải', "RADIO2", default=False, key="lane-r")],
    [sg.Text("Tầm nhìn nhỏ hơn: ", size=(35,1)), sg.Radio('Không bị hạn chế', "RADIO3", default=True, key="without"), sg.Radio('200m', "RADIO3", default=False, key="200m"), sg.Radio('100m', "RADIO3", default=False, key="100m"), sg.Radio('50m', "RADIO3", default=False, key="50m")],
    [sg.Text("Trạng thái đường đi: ", size=(35,1)), sg.Checkbox('Đường trơn trượt', default=False, key="slippery"), sg.Checkbox('Địa hình quanh co, đèo dốc', default=False, key="highpass")],
    [sg.Button("Tư vấn")],
    [sg.Frame("Kết quả tư vấn", frame, key='-FRAME-')]
]

window = sg.Window("Tư vấn tốc độ xe", layout, size=(700,420))


while True:
    event, values = window.read()

    def get_facts():
        facts = ['Freeway']

        if values["safety"]:
            facts.append("Safety distance 100 meters")
        # if values["1lane"]:
        #     facts.append("One lane")
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
        # if values["without"]:
        #     facts.append("Without")
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


    if event == "Tư vấn":
        facts = get_facts()
        rules = expert.import_rules()
        Max, Min, Advice = expert.test_one_case(rules, facts)
        window['max_output'].update(str(Max)+"km/h")
        window['min_output'].update(str(Min)+"km/h")
        
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
    if event == sg.WIN_CLOSED:
        break