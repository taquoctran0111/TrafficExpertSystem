import PySimpleGUI as sg

frame = [
    [sg.Text("Tốc độ tối đa: ", size=(12,1)), sg.Text(" ",size=(582,1), key="max_output", text_color="black")], 
    [sg.Text("Tốc độ tối thiểu: ", size=(12,1)), sg.Text(" ",size=(582,1), key="min_output", text_color="black")],
    [sg.Text("Lời khuyên: ", size=(12,1)), sg.Text(" ",size=(582,1), key="advice_output", text_color="black")]
]

layout = [
    [sg.Text("------ ĐIỀU KIỆN ĐƯỜNG VÀ HIỆN TRẠNG GIAO THÔNG")],
    [sg.Text(" ")],
    [sg.Checkbox('Có phương tiện trong vòng 100m phía trước', default=False)],
    [sg.Text("Số làn: ", size=(35,1)), sg.Radio('Một làn', "RADIO1", default=True), sg.Radio('Hai làn', "RADIO1", default=False), sg.Radio('Ba làn', "RADIO1", default=False)],
    [sg.Text("Phương tiện đang lưu thông trên làn: ", size=(35,1)), sg.Radio('Làn trái', "RADIO2", default=True), sg.Radio('Làn giữa', "RADIO2", default=False), sg.Radio('Làn phải', "RADIO2", default=False)],
    [sg.Text("Tầm nhìn nhỏ hơn: ", size=(35,1)), sg.Radio('Không bị hạn chế', "RADIO3", default=True), sg.Radio('200m', "RADIO3", default=False), sg.Radio('100m', "RADIO3", default=False), sg.Radio('50m', "RADIO3", default=False)],
    [sg.Text("Trạng thái đường đi: ", size=(35,1)), sg.Checkbox('Đường trơn trượt', default=False), sg.Checkbox('Địa hình quanh co, đèo dốc', default=False)],
    [sg.Button("Tư vấn")],
    [sg.Frame("Kết quả tư vấn", frame, key='-FRAME-')]
]

window = sg.Window("Tư vấn tốc độ xe", layout, size=(650,350))


while True:
    event, values = window.read()

    facts = ['Freeway']

    

    if values[0]:
        facts.append("Safety distance 100 meters")
    if values[1]:
        facts.append("One lane")
    if values[2]:
        facts.append("Two lane")
    if values[3]:
        facts.append("Three lane")
    if values[4]:
        facts.append("Left lane")
    if values[5]:
        facts.append("Middle lane")
    if values[6]:
        facts.append("Right lane")
    if values[7]:
        facts.append("Without")
    if values[8]:
        facts.append("200m")
    if values[9]:
        facts.append("100m")
    if values[10]:
        facts.append("50m")
    if values[11]:
        facts.append("Slippery")
    if values[12]:
        facts.append("High pass")


    if event == "Tư vấn":
        print(facts)
        window['max_output'].update("120 km/h")
        window['min_output'].update("100 km/h")
        window['advice_output'].update("Đi chậm lại đi cmm =)))")
    if event == sg.WIN_CLOSED:
        break