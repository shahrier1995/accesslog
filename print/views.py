
import django
django.setup()
import pytz
import json
from datetime import datetime
from print.models import Machine, PrintJob, BedTemperatureHistory, ToolTemperatureHistory
from django.utils import timezone
def handle_msg(topic, message):
    printer = topic.split("/")[2]
    p_id = Machine.objects.get(Name=printer).id
    m = message.decode("Utf-8")

    # Check if topic is PrintDone
    try:
        done = topic.split("/")[4]
        if done != "PrintDone":
            done = None
    except:
        done = None

    # Check if topic is PrintStarted
    try:
        start = topic.split("/")[4]
        if start != "PrintStarted":
            start = None
    except:
        start = None

    # Check if topic is Temperature and if tool or bed temp is sent
    try:
        temp = topic.split("/")[3]
        toolbed = topic.split("/")[4]
        if temp != "temperature":
            temp = None
            toolbed = None
    except:
        toolbed = None
        temp = None

    if start == "PrintStarted":
        # Event: Printer is done with PrintJob
        print("Print started")
        # Check if Printjob already exists
        try:
            PrintJob.objects.get(Machine_id=p_id)
            p_exists = True
        except:
            p_exists = False

        try:
            if p_exists and PrintJob.objects.get(Machine_id=p_id).State == 0:
                PrintJob.objects.create(Start=timezone.now(), End=timezone.now(), GCode_id=None,State=1, Machine_id=p_id,User_id=1)
                print("Printjob created")
            elif not p_exists:
                PrintJob.objects.create(Start=timezone.now(), End=timezone.now(), GCode_id=None,State=1, Machine_id=p_id,User_id=1)
                print("Printjob created")
        except Exception as e:
            print(e)

    elif done == "PrintDone":
        # Event: Printer is done with PrintJob
        print("Print Done")

        try:
            PrintJob.objects.get(Machine_id=p_id, State=1)
            p_exists = True
        except:
            p_exists = False

        try:
            if p_exists:
                pj = PrintJob.objects.get(Machine_id=p_id, State=1)
                pj.State = 0
                pj.save()
                print("Printjob state = 0")
        except Exception as e:
            print(e)

    elif temp == "temperature":
        # Temperature is sent
        target = None
        actual = None
        timestamp = None

        # Set Temperature Data
        try:
            timestamp = datetime.fromtimestamp(json.loads(m)["_timestamp"], tz=pytz.timezone('Europe/Berlin'))
            actual = json.loads(m)["actual"]
            target = json.loads(m)["target"]
        except Exception as e:
            print(e)

        # Check if Machine has related PrintJob
        try:
            PrintJob.objects.get(Machine_id=p_id, State=1)
            p_exists = True
        except:
            p_exists = False

        # If Temperature is bed info
        if p_exists:
            if toolbed == "bed":
                try:
                    BedTemperatureHistory.objects.create(PrintJob_id=PrintJob.objects.get(Machine_id=p_id, State=1).id, Target=target, Actual=actual, TimeStamp=timestamp)
                    print(timestamp)
                except Exception as e:
                    print(e)

            # If Temperature is tool info
            elif toolbed == "tool0":
                try:
                    ToolTemperatureHistory.objects.create(PrintJob_id=PrintJob.objects.get(Machine_id=p_id, State=1).id, Target=target, Actual=actual, TimeStamp=timestamp)
                except Exception as e:
                    print(e)