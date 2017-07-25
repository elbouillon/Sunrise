import config

from workers import CheckAlarmWorker

def run():
    while True:
        print("Wait for an alarm")
        check_alarm = CheckAlarmWorker(config)
        check_alarm.start()
        check_alarm.join()
        print("Run the alarm !!")

if __name__ == '__main__':
    run()