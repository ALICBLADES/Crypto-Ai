from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QTextDocument
from main import Ui_MainWindow
import paho.mqtt.client as mqtt
import mysql.connector
import os
import sys
import getpass
import pygame
user = getpass.getuser()

if sys.platform == 'win32':
    messages_dir = 'C:/Users/{}/Documents/kontrol/'.format(user)
    messages_path = 'C:/Users/{}/Documents/kontrol/messages'.format(user)
elif sys.platform == 'linux':
    messages_dir = os.path.relpath(
        '/home/{}/.local/share/kontrol/'.format(user))
    messages_path = os.path.relpath(
        '/home/{}/.local/share/kontrol/messages'.format(user))

if getattr(sys, 'frozen', False):
    # frozen
    dir_ = os.path.dirname(sys.executable)
else:
    # unfrozen
    dir_ = os.path.dirname(os.path.realpath(__file__))


def on_message(client, userdata, message):
    msg = str(message.payload.decode('utf-8'))
    with open(messages_path, 'w') as op:
        op.write(msg + message.topic)
        op.close()


class get_message(QThread):
    signal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(get_message, self).__init__(parent)

    def run(self):
        while True:
            with open(messages_path, 'r') as op:
                message = op.readlines()
                op.close()
            for line in message:
                if 'room_light_cb' in line:
                    topic = 'room_light_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'room_fan_cb' in line:
                    topic = 'room_fan_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'room_air_cb' in line:
                    topic = 'room_air_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'room_curtain_cb' in line:
                    topic = 'room_curtain_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'room_door_cb' in line:
                    topic = 'room_door_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'OPEN' in msg:
                        self.signal.emit('OPEN', topic)
                    elif 'CLOSE' in msg:
                        self.signal.emit('CLOSE', topic)

                elif 'room_temp_cb' in line:
                    topic = 'room_temp_cb'
                    msg = line.replace('room_temp_cb', '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'room_alarm_cb' in line:
                    topic = 'room_alarm_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'outdoor_light_cb' in line:
                    topic = 'outdoor_light_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'irrigation' in line:
                    topic = 'irrigation_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    if 'ON' in msg:
                        self.signal.emit('ON', topic)
                    elif 'OFF' in msg:
                        self.signal.emit('OFF', topic)
                    elif 'AUTO' in msg:
                        self.signal.emit('AUTO', topic)
                    else:
                        self.signal.emit(msg, topic)

                elif 'outdoor_temp_cb' in line:
                    topic = 'outdoor_temp_cb'
                    msg = line.replace('outdoor_temp_cb', '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'outdoor_hum_cb' in line:
                    topic = 'outdoor_hum_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'outdoor_alarm_cb' in line:
                    topic = 'outdoor_alarm_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)

                elif 'alarm_cb' in line:
                    topic = 'alarm_cb'
                    msg = line.replace(topic, '')
                    msg = msg.strip()
                    self.signal.emit(msg, topic)
            open(messages_path, 'w')


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.file_dir()
        self.connect()
        self.conf_ui()
        self.conf_buttons()
        self.conf_sliders()
        self.thread = get_message()
        self.thread.start()
        self.thread.signal.connect(self.conf_labels)

    def keyPressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.AltModifier:
            if event.key() == Qt.Key_1:
                self.tabWidget.setCurrentIndex(0)
            elif event.key() == Qt.Key_2:
                self.tabWidget.setCurrentIndex(1)
            elif event.key() == Qt.Key_3:
                self.tabWidget.setCurrentIndex(2)
            elif event.key() == Qt.Key_4:
                self.tabWidget.setCurrentIndex(3)

    def closeEvent(self, event):
        if sys.platform == 'win32':
            os.system('taskkill /f /im kontrol.exe')
        elif sys.platform == 'linux':
            os.system('pkill python3; pkill python; pkill kontrol')
        event.accept()

    def file_dir(self):
        if not os.path.exists(messages_dir):
            os.makedirs(messages_dir)
        open(messages_path, 'w')

    def connect(self):
        self.mqttc = mqtt.Client('Desktop')
        try:
            self.mqttc.connect('localhost')
        except Exception:
            QMessageBox.information(
                self, 'Information',
                'Can\'t connect to MQTT Broker', QMessageBox.Ok)
        self.mqttc.on_message = on_message
        self.mqttc.loop_start()
        self.mqttc.subscribe([
            ('room_light_cb', 1), ('room_fan_cb', 1), ('room_air_cb', 1),
            ('room_curtain_cb', 1), ('room_door_cb', 1), ('room_temp_cb', 1),
            ('outdoor_light_cb', 1), ('irrigation_cb', 1), ('alarm_cb', 1),
            ('outdoor_temp_cb', 1), ('outdoor_hum_cb', 1),
            ('room_alarm_cb', 1), ('outdoor_alarm_cb', 1)])

    def conf_ui(self):
        self.setFixedSize(901, 547)

    def conf_buttons(self):
        # room
        self.r_light_b_on.clicked.connect(self.button_rlbon)
        self.r_light_b_off.clicked.connect(self.button_rlboff)
        self.r_light_b_auto.clicked.connect(self.button_rlbauto)
        self.r_fan_b_on.clicked.connect(self.button_rfbon)
        self.r_fan_b_off.clicked.connect(self.button_rfboff)
        self.r_fan_b_auto.clicked.connect(self.button_rfbauto)
        self.r_air_b_on.clicked.connect(self.button_rabon)
        self.r_air_b_off.clicked.connect(self.button_raboff)
        self.r_air_b_auto.clicked.connect(self.button_rabauto)
        self.r_curtain_b_on.clicked.connect(self.button_rcbon)
        self.r_curtain_b_off.clicked.connect(self.button_rcboff)
        self.r_curtain_b_auto.clicked.connect(self.button_rcbauto)
        self.r_door_b_open.clicked.connect(self.button_rdbopen)
        self.r_door_b_close.clicked.connect(self.button_rdbclose)
        self.r_b_open.clicked.connect(self.button_r_open)
        self.r_b_close.clicked.connect(self.button_r_close)
        self.r_b_alarm.clicked.connect(self.button_r_alarm)

        # outdoor
        self.o_light_b_on.clicked.connect(self.button_olbon)
        self.o_light_b_off.clicked.connect(self.button_olboff)
        self.o_light_b_auto.clicked.connect(self.button_olbauto)
        self.o_irri_b_on.clicked.connect(self.button_oibon)
        self.o_irri_b_off.clicked.connect(self.button_oiboff)
        self.o_irri_b_auto.clicked.connect(self.button_oibauto)
        self.o_b_open.clicked.connect(self.button_o_open)
        self.o_b_close.clicked.connect(self.button_o_close)
        self.o_b_alarm.clicked.connect(self.button_o_alarm)

        # message
        self.message_send.clicked.connect(self.button_message_send)
        self.message_clear.clicked.connect(self.button_message_clear)
        self.refresh.clicked.connect(self.db)

    # Room
    def button_rlbon(self):
        self.mqttc.publish('room_light', '01')

    def button_rlboff(self):
        self.mqttc.publish('room_light', '0')
        self.r_light_s.setValue(0)

    def button_rlbauto(self):
        self.mqttc.publish('room_light', '02')

    def button_rfbon(self):
        self.mqttc.publish('room_fan', '01')

    def button_rfboff(self):
        self.mqttc.publish('room_fan', '0')
        self.r_fan_s.setValue(0)

    def button_rfbauto(self):
        self.mqttc.publish('room_fan', '02')

    def button_rabon(self):
        self.mqttc.publish('room_air', '01')

    def button_raboff(self):
        self.mqttc.publish('room_air', '0')

    def button_rabauto(self):
        self.mqttc.publish('room_air', '02')

    def button_rcbon(self):
        self.mqttc.publish('room_curtain', '01')

    def button_rcboff(self):
        self.mqttc.publish('room_curtain', '0')

    def button_rcbauto(self):
        self.mqttc.publish('room_curtain', '02')

    def button_rdbopen(self):
        self.mqttc.publish('room_door', '01')

    def button_rdbclose(self):
        self.mqttc.publish('room_door', '0')

    def button_r_open(self):
        self.button_rlbon()
        self.button_rfbon()
        self.button_rcbon()
        self.button_rabon()

    def button_r_close(self):
        self.button_rlboff()
        self.button_rfboff()
        self.button_rcboff()
        self.button_raboff()

    def button_r_alarm(self):
        doc = QTextDocument()
        doc.setHtml(self.label_r_alarm.text())
        if doc.toPlainText() == 'Active':
            self.mqttc.publish('room_alarm', '0')
        else:
            self.mqttc.publish('room_alarm', '01')

    # Outdoor
    def button_olbon(self):
        self.mqttc.publish('outdoor_light', '01')

    def button_olboff(self):
        self.mqttc.publish('outdoor_light', '0')
        self.o_light_s.setValue(0)

    def button_olbauto(self):
        self.mqttc.publish('outdoor_light', '02')

    def button_oibon(self):
        self.mqttc.publish('irrigation', '01')

    def button_oiboff(self):
        self.mqttc.publish('irrigation', '0')
        self.o_irri_s.setValue(0)

    def button_oibauto(self):
        self.mqttc.publish('irrigation', '02')

    def button_message_send(self):
        self.mqttc.publish('message', self.message_text.toPlainText())

    def button_message_clear(self):
        self.message_text.setText('')

    def button_o_open(self):
        self.button_olbon()
        self.button_oibon()

    def button_o_close(self):
        self.button_olboff()
        self.button_oiboff()

    def button_o_alarm(self):
        doc = QTextDocument()
        doc.setHtml(self.label_o_alarm.text())
        if doc.toPlainText() == 'Active':
            self.mqttc.publish('outdoor_alarm', '0')
        else:
            self.mqttc.publish('outdoor_alarm', '01')

    def conf_sliders(self):
        self.r_light_s.sliderReleased.connect(self.slider_rl)
        self.r_fan_s.sliderReleased.connect(self.slider_rf)
        self.o_light_s.sliderReleased.connect(self.slider_ol)
        self.o_irri_s.sliderReleased.connect(self.slider_oi)
        self.r_light_s.valueChanged.connect(self.slider_rl_)
        self.r_fan_s.valueChanged.connect(self.slider_rf_)
        self.o_light_s.valueChanged.connect(self.slider_ol_)
        self.o_irri_s.valueChanged.connect(self.slider_oi_)
        self.r_air_sb.valueChanged.connect(self.spin_ra)

    def slider_rl(self):
        self.mqttc.publish('room_light', int(self.r_light_s.value()))

    def slider_rl_(self):
        self.r_light_l2.setText(str(self.r_light_s.value()) + '%')

    def slider_rf(self):
        self.mqttc.publish('room_fan', int(self.r_fan_s.value()))

    def slider_rf_(self):
        self.r_fan_l2.setText(str(self.r_fan_s.value()) + '%')

    def slider_ol(self):
        self.mqttc.publish('outdoor_light', int(self.o_light_s.value()))

    def slider_ol_(self):
        self.o_light_l2.setText(str(self.o_light_s.value()) + '%')

    def slider_oi(self):
        self.mqttc.publish('irrigation', int(self.o_irri_s.value()))

    def slider_oi_(self):
        self.o_irri_l2.setText(str(self.o_irri_s.value()) + '%')

    def spin_ra(self):
        self.mqttc.publish('room_air', self.r_air_sb.value())

    def alarm(self, msg):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        if sys.platform == 'win32':
            song = pygame.mixer.Sound(
                'C:/Program Files (x86)/kontrol/alarm.wav')
        elif sys.platform == 'linux':
            song = pygame.mixer.Sound(
                '/home/amr/Projects/kontrol/alarm.wav')
        song.play(-1)
        reply = QMessageBox.warning(None, 'Alarm', msg, QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            song.stop()

    def conf_labels(self, msg, topic):

        if topic == 'room_light_cb':
            if msg == 'ON':
                self.r_label_light.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_light_level.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.r_label_light.setText('<p style="color:#C62828">OFF</p>')
                self.r_label_light_level.setText('-')
            elif msg == 'AUTO':
                self.r_label_light.setText('<p style="color:#1565C0">AUTO</p>')
                self.r_label_light_level.setText('-')
            else:
                self.r_label_light.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_light_level.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'room_fan_cb':
            if msg == 'ON':
                self.r_label_fan.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_fan_level.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.r_label_fan.setText('<p style="color:#C62828">OFF</p>')
                self.r_label_fan_level.setText('-')
            elif msg == 'AUTO':
                self.r_label_fan.setText('<p style="color:#1565C0">AUTO</p>')
                self.r_label_fan_level.setText('-')
            else:
                self.r_label_fan.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_fan_level.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'room_air_cb':
            if msg == 'ON':
                self.r_label_air.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_air_level.setText(
                    '<p style="color:#2E7D32">21°</p>')
            elif msg == 'OFF':
                self.r_label_air.setText('<p style="color:#C62828">OFF</p>')
                self.r_label_air_level.setText('-')
            elif msg == 'AUTO':
                self.r_label_air.setText('<p style="color:#1565C0">AUTO</p>')
                self.r_label_air_level.setText('-')
            else:
                self.r_label_air.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_air_level.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'room_curtain_cb':
            if msg == 'ON':
                self.r_label_curtain.setText('<p style="color:#2E7D32">ON</p>')
                self.r_label_curtain_level.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.r_label_curtain.setText(
                    '<p style="color:#C62828">OFF</p>')
                self.r_label_curtain_level.setText('-')
            elif msg == 'AUTO':
                self.r_label_curtain.setText(
                    '<p style="color:#1565C0">AUTO</p>')
                self.r_label_curtain_level.setText('-')

        elif topic == 'room_door_cb':
            if msg == 'ON':
                self.r_label_door.setText('<p style="color:#2E7D32">OPEN</p>')
            elif msg == 'OFF':
                self.r_label_door.setText(
                    '<p style="color:#C62828">CLOSED</p>')

        elif topic == 'room_temp_cb':
            if int(msg) > 22 and int(msg) < 28:
                self.r_label_temp.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            elif int(msg) <= 22:
                self.r_label_temp.setText(
                    '<p style="color:#1565C0">{}°</p>'.format(msg))
            elif int(msg) >= 28:
                self.r_label_temp.setText(
                    '<p style="color:#C62828">{}°</p>'.format(msg))

        elif topic == 'room_alarm_cb':
            if msg == 'ON':
                self.label_r_alarm.setText(
                    '<p style="color:#2E7D32">Active</p>')
            elif msg == 'OFF':
                self.label_r_alarm.setText(
                    '<p style="color:#C62828">Inactive</p>')

        elif topic == 'outdoor_light_cb':
            if msg == 'ON':
                self.o_label_light.setText('<p style="color:#2E7D32">ON</p>')
                self.o_label_light_level.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.o_label_light.setText('<p style="color:#C62828">OFF</p>')
                self.o_label_light_level.setText('-')
            elif msg == 'AUTO':
                self.o_label_light.setText('<p style="color:#1565C0">AUTO</p>')
                self.o_label_light_level.setText('-')
            else:
                self.o_label_light_setText('<p style="color:#2E7D32">ON</p>')
                self.o_label_light_level.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'irrigation_cb':
            if msg == 'ON':
                self.o_label_irri.setText('<p style="color:#2E7D32">ON</p>')
                self.o_label_irri_level.setText(
                    '<p style="color:#2E7D32">100%</p>')
            elif msg == 'OFF':
                self.o_label_irri.setText('<p style="color:#C62828">OFF</p>')
                self.o_label_irri_level.setText('-')
            elif msg == 'AUTO':
                self.o_label_irri.setText('<p style="color:#1565C0">AUTO</p>')
                self.o_label_irri_level.setText('-')
            else:
                self.o_label_irri.setText('<p style="color:#2E7D32">ON</p>')
                self.o_label_irri_level.setText(
                    '<p style="color:#2E7D32">{}%</p>'.format(msg))

        elif topic == 'outdoor_temp_cb':
            if int(msg) >= 23 and int(msg) <= 27:
                self.o_label_temp.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            elif int(msg) <= 22:
                self.o_label_temp.setText(
                    '<p style="color:#1565C0">{}°</p>'.format(msg))
            elif int(msg) >= 28:
                self.o_label_temp.setText(
                    '<p style="color:#C62828">{}°</p>'.format(msg))

        elif topic == 'outdoor_hum_cb':
            if int(msg) >= 45 and int(msg) <= 55:
                self.o_label_hum.setText(
                    '<p style="color:#2E7D32">{}°</p>'.format(msg))
            else:
                self.o_label_hum.setText(
                    '<p style="color:#C62828">{}°</p>'.format(msg))

        elif topic == 'outdoor_alarm_cb':
            if msg == 'ON':
                self.label_o_alarm.setText(
                    '<p style="color:#2E7D32">Active</p>')
            elif msg == 'OFF':
                self.label_o_alarm.setText(
                    '<p style="color:#C62828">Inactive</p>')

        elif topic == 'alarm_cb':
            self.alarm(msg)

    def db(self):
        row = 0
        col_aname = 0
        col_code = 1
        col_year = 2
        col_uid = 3
        col_s1 = 4
        col_s2 = 5
        col_s3 = 6
        col_s4 = 7
        col_s5 = 8

        cnx = mysql.connector.connect(
            user='root', password='mysql',
            host='localhost', database='assc')
        cursor = cnx.cursor()
        get_code = ("""SELECT aname, uid, code, year, s1, s2, s3,
                    s4, s5 FROM students""")
        cursor.execute(get_code)
        for (aname, uid, code, year, s1, s2, s3, s4, s5) in cursor:
            self.table.setItem(row, col_code, QTableWidgetItem(str(code)))
            self.table.setItem(row, col_year, QTableWidgetItem(str(year)))
            self.table.setItem(row, col_uid, QTableWidgetItem(str(uid)))
            self.table.setItem(row, col_aname, QTableWidgetItem(str(aname)))
            self.table.setItem(row, col_s1, QTableWidgetItem(str(s1)))
            self.table.setItem(row, col_s2, QTableWidgetItem(str(s2)))
            self.table.setItem(row, col_s3, QTableWidgetItem(str(s3)))
            self.table.setItem(row, col_s4, QTableWidgetItem(str(s4)))
            self.table.setItem(row, col_s5, QTableWidgetItem(str(s5)))
            row = row + 1
        cnx.commit()
        cursor.close()
        cnx.close()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
