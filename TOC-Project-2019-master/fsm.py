from transitions.extensions import GraphMachine
from utils import *



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_statea1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '我要查氣象'
        return False

    def is_going_to_statea2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return 1
        return False

    def on_enter_statea1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請問你要查哪一區的氣象(北區、中區、南區、東區)")
        #self.go_back()

    def on_exit_statea1(self,event):
        print('Leaving state1')

    def on_enter_statea2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "我只提供查氣象的功能，欲查詢氣象請輸入\"我要查氣象\"")
        self.go_back()

    def on_exit_statea2(self):
        print('Leaving state2')
        
    def is_going_to_stateb1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '北區'
        return False
    
    def is_going_to_stateb2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '中區'
        return False
    
    def is_going_to_stateb3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '南區'
        return False
    
    def is_going_to_stateb4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '東區'
        return False
    def on_enter_stateb1(self, event):
        print("I'm entering stateb1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "北區縣市有基隆、台北、新北、桃園、新竹市、新竹縣、苗栗縣請選擇欲查詢縣市")
        #self.go_back()

    def on_exit_stateb1(self, event):
        print('Leaving stateb1')
    
    def on_enter_stateb2(self, event):
        print("I'm entering stateb2")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "中區縣市有台中、彰化、南投、雲林、嘉義市、嘉義縣請選擇欲查詢縣市")
        #self.go_back()

    def on_exit_stateb2(self, event):
        print('Leaving stateb2')
        
    def on_enter_stateb3(self, event):
        print("I'm entering stateb3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "南區縣市有台南、高雄、屏東請選擇欲查詢縣市")
        #self.go_back()

    def on_exit_stateb3(self, event):
        print('Leaving stateb3')
        
    def on_enter_stateb4(self, event):
        print("I'm entering stateb4")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "東區縣市有宜蘭、花蓮、台東請選擇欲查詢縣市")
        #self.go_back()

    def on_exit_stateb4(self, event):
        print('Leaving stateb4')
    
    def is_going_to_staten1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '基隆'
        return False
    def is_going_to_staten2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台北'
        return False
    def is_going_to_staten3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '新北'
        return False
    def is_going_to_staten4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '桃園'
        return False
    def is_going_to_staten5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '新竹市'
        return False
    def is_going_to_staten6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '新竹縣'
        return False
    def is_going_to_staten7(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '苗栗縣'
        return False
    def on_enter_staten1(self, event):
        print("I'm entering staten1")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "基隆氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Keelung_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Keelung_City.htm","title":"基隆氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten1(self, event):
        print('Leaving staten1')

        
    def on_enter_staten2(self, event):
        print("I'm entering staten2")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "台北氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm","title":"台北氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten2(self, event):
        print('Leaving staten2')

        
    def on_enter_staten3(self, event):
        print("I'm entering staten3")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "新北氣象https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/New_Taipei_City.htm","title":"新北氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten3(self, event):
        print('Leaving staten3')

        
    def on_enter_staten4(self, event):
        print("I'm entering staten4")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "桃園氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Taoyuan_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Taoyuan_City.htm","title":"桃園氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten4(self, event):
        print('Leaving staten4')

        
    def on_enter_staten5(self, event):
        print("I'm entering staten5")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "新竹市氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm","title":"新竹市氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten5(self, event):
        print('Leaving staten5')

        
    def on_enter_staten6(self, event):
        print("I'm entering staten6")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "新竹縣氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_County.htm","title":"新竹縣氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten6(self, event):
        print('Leaving staten6')

        
    def on_enter_staten(self, event):
        print("I'm entering staten7")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "苗栗縣氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Miaoli_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Keelung_City.htm","title":"基隆氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_staten7(self, event):
        print('Leaving staten7')

        
    def is_going_to_statem1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台中'
        return False
    
    def is_going_to_statem2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '彰化'
        return False
    
    def is_going_to_statem3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '南投'
        return False
    
    def is_going_to_statem4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '雲林'
        return False
    
    def is_going_to_statem5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '嘉義市'
        return False
    
    def is_going_to_statem6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '嘉義縣'
        return False
    
    def on_enter_statem1(self, event):
        print("I'm entering statem1")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "台中氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Taichung_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Taichung_City.htm","title":"台中氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statem1(self, event):
        print('Leaving statem1')

        
    def on_enter_statem2(self, event):
        print("I'm entering statem2")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "彰化氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Changhua_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Changhua_County.htm","title":"彰化氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statem2(self, event):
        print('Leaving statem2')

        
    def on_enter_statem3(self, event):
        print("I'm entering statem3")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "南投氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Nantou_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Nantou_County.htm","title":"南投氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statem3(self, event):
        print('Leaving statem3')

        
    def on_enter_statem4(self, event):
        print("I'm entering statem4")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "雲林氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Yunlin_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Yunlin_County.htm","title":"雲林氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statem4(self, event):
        print('Leaving statem4')

        
    def on_enter_statem5(self, event):
        print("I'm entering statem5")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "嘉義市氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Chiayi_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Chiayi_City.htm","title":"嘉義市氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statem5(self, event):
        print('Leaving statem5')

    
    def on_enter_statem6(self, event):
        print("I'm entering statem6")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "嘉義縣氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Chiayi_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Chiayi_County.htm","title":"嘉義縣氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statem6(self, event):
        print('Leaving statem6')

        
    def is_going_to_states1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台南'
        return False
    
    def is_going_to_states2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '高雄'
        return False
        
    def is_going_to_states3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '屏東'
        return False
    
    def on_enter_states1(self, event):
        print("I'm entering states1")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "台南氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm","title":"台南氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_states1(self, event):
        print('Leaving states1')

        
    def on_enter_states2(self, event):
        print("I'm entering states2")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "高雄氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Tainan_City.htm","title":"高雄氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_states2(self, event):
        print('Leaving states2')

    
    def on_enter_states3(self, event):
        print("I'm entering states3")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "屏東氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Pingtung_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Pingtung_County.htm","title":"屏東氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_states3(self, event):
        print('Leaving states3')

        
    def is_going_to_statee1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '宜蘭'
        return False
    
    def is_going_to_statee2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '花蓮'
        return False
    
    def is_going_to_statee3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '台東'
        return False
    
    def on_enter_statee1(self, event):
        print("I'm entering statee1")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "宜蘭氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Yilan_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Yilan_County.htm","title":"宜蘭氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statee1(self, event):
        print('Leaving statee1')

        
    def on_enter_statee2(self, event):
        print("I'm entering statee2")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "花蓮氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Hualien_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Hualien_County.htm","title":"花蓮氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statee2(self, event):
        print('Leaving statee2')

    
    def on_enter_statee3(self, event):
        print("I'm entering statee3")

        sender_id = event['sender']['id']
        #responese = send_text_message(sender_id, "台東氣象https://www.cwb.gov.tw/V7/forecast/taiwan/Taitung_County.htm")
        responese = send_button_message(sender_id,"請點下方傳送門",[{"type":"web_url","url":"https://www.cwb.gov.tw/V7/forecast/taiwan/Taitung_County.htm","title":"台東氣象","webview_height_ratio": "full"}])
        #self.go_back()

    def on_exit_statee3(self, event):
        print('Leaving statee3')

    def is_going_to_user(self, event):
        if event.get("message"):
            text = event['message']['text']
            return 1
        return False
        