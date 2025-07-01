import datetime 
x=datetime.datetime.now()
medical_inventory={}
doctors={}
medical_staff={}
patients={}
rooms = {
    "general_ward": 20,
    "ac_ward": 10,
    "emergency_ward": 10
}
room_assignment={}
medical_record={}
appointments=[]
billing=[]



def register_patient(patient_id,personal_info,medical_history,insurance_info):
    patient={
        str(patient_id):{
        "personal_info":personal_info,
        "medical_history":medical_history,
        "insurance_info":insurance_info,
        "status": "Outpatient",
        "room": None,
        "admitted_on": None,
        "doctor_id": None,
        "medications": [],
        "vitals": {}
        }
    }
    patients.update(patient)

    
def add_medical_staff(staff_id, name, specialization, shift_schedule, contact_info):
    staff = {
        staff_id:{
        "name": name,
        "specialization": specialization,
        "shift_schedule": shift_schedule,
        "contact_info": contact_info
    }}
    medical_staff.update(staff)


def schedule_appointment(patient_id, doctor_id, appointment_date, appointment_type):
    if doctor_id not in medical_staff:
        print(f"Doctor {doctor_id} not found.")
        return
    appointment = {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "appointment_date": appointment_date,
        "appointment_type": appointment_type
    }
    appointments.append(appointment)


def create_medical_record(patient_id, doctor_id, diagnosis=[], treatment="", prescription=[]):
    patient_id = str(patient_id)
    record={
        patient_id:{
        "doctor_id":doctor_id,
        "diagnosis":diagnosis,
        "treatment":treatment,
        "prescription":prescription
        }}
    medical_record.update(record)
    patients[patient_id]["doctor_id"] = doctor_id
    patients[patient_id]["medications"] = prescription

def process_billing(patient_id, services_list, insurance_coverage):
    total_bill=sum(service["cost"] for service in services_list)
    covered_amount=total_bill*(insurance_coverage/100)
    due=total_bill-covered_amount
    service_dict = {service['name']: service['cost'] for service in services_list}
    billing.append({
        "patient_id": patient_id,
        "admission_date": x.strftime("%Y-%m-%d"),
        "discharge_date": "Pending",
        "services": service_dict,
        "total": total_bill,
        "insurance": covered_amount,
        "due": due
    })
    return{
        "total":total_bill,
        "covered":covered_amount,
        "Due":due
    }

def manage_emergency_admission(patient_id, emergency_type, severity_level):
    if str(patient_id) not in patients:
        print("Unregistered patient. Registering now...")
        register_patient(patient_id, {"name": "Unknown", "mobile": None}, {}, {})
    assign_room(patient_id, "emergency_ward", x.strftime("%Y-%m-%d"), 3)
    print(f"Emergency patient {patient_id} admitted for {emergency_type} with severity {severity_level}")

def track_medication_inventory(medication_id, quantity, expiry_date, supplier):
     medical_inventory[medication_id] = {
        "quantity": quantity,
        "expiry_date": expiry_date,
        "supplier": supplier
    }

def assign_room(patient_id, room_type, admission_date, expected_duration):
    patient_id = str(patient_id)
    if rooms.get(room_type,0)>0:
        rooms[room_type]-=1
        room_id = f"{room_type}_{len(room_assignment)+1}"
        room_assignment[patient_id]={
        "patient_id":patient_id,
        "room_type":room_type,
        "admission_date":admission_date,
        "expected_duration":expected_duration,
        "room_id": room_id
        }
        patients[patient_id]["status"] = "Inpatient"
        patients[patient_id]["admitted_on"] = admission_date
        patients[patient_id]["room"] = room_id
    else:
        return f"No {room_type} rooms are available."


def calculate_treatment_cost(patient_id, treatment_plan, insurance_details):
    total_cost = sum(item['cost'] for item in treatment_plan)
    coverage = insurance_details.get("coverage", 0)
    covered_amount = total_cost * (coverage / 100)
    due = total_cost - covered_amount
    print(f"Total: {total_cost}, Covered: {covered_amount}, Due: {due}")
    return {"total": total_cost, "covered": covered_amount, "due": due}


def generate_patient_report(patient_id, report_type):
    if patient_id not in patients:
        print("Patient not found.")
        return
    if report_type == "summary":
        display_patient_dashboard(patient_id)
    elif report_type == "billing":
        display_billing_summary(patient_id)
    elif report_type == "medical_record":
        print("=== MEDICAL RECORD ===")
        print(medical_record.get(patient_id, "No record found."))
    else:
        print("Invalid report type.")

def analyze_hospital_efficiency(metrics_type, time_period):
    print(f"Analyzing {metrics_type} for {time_period}...")
    if metrics_type == "occupancy":
        total_rooms = sum(rooms.values()) + len(room_assignment)
        occupied = len(room_assignment)
        print(f"Occupancy Rate: {(occupied/total_rooms)*100:.2f}%")
    elif metrics_type == "billing":
        total_earnings = sum(entry["due"] for entry in billing)
        print(f"Total Earnings: ₹{total_earnings}")
    else:
        print("Unsupported metrics type.")

def manage_discharge_process(patient_id, discharge_date, follow_up_instructions):
    patient_id = str(patient_id)
    if patient_id in room_assignment:
        room_type = room_assignment[patient_id]["room_type"]
        rooms[room_type] += 1
        del room_assignment[patient_id]
    patients[patient_id]["status"] = "Discharged"
    patients[patient_id]["discharged_on"] = discharge_date
    patients[patient_id]["follow_up"] = follow_up_instructions

    # Update billing discharge date
    for bill in billing:
        if str(bill["patient_id"]) == patient_id:
            bill["discharge_date"] = discharge_date

def display_patient_dashboard(patient_id):
    patient_id=str(patient_id)
    p = patients.get(patient_id)
    if not p:
        print("Patient not found.")
        return
    print("=== PATIENT DASHBOARD ===")
    print(f"Patient: {p['personal_info'].get('name')} (ID: {patient_id})")
    print(f"Insurance: {p['insurance_info'].get('name')} (Policy: {p['insurance_info'].get('ID')})")
    print(f"Current Status: {p['status']}")
    print(f"Room: {p['room'] or 'N/A'}")
    print(f"Admitted: {p['admitted_on'] or 'N/A'}")
    doc = medical_staff.get(p['doctor_id'], {}).get("name", "Unknown")
    spec = medical_staff.get(p['doctor_id'], {}).get("specialization", "N/A")
    print(f"Attending Doctor: {doc} ({spec})")
    if p['vitals']:
        print(f"Recent Vitals ({p['vitals']['date']}):")
        print(f"Blood Pressure: {p['vitals']['blood_pressure']}")
        print(f"Heart Rate: {p['vitals']['heart_rate']}")
        print(f"Temperature: {p['vitals']['temperature']}")
        print(f"Oxygen Saturation: {p['vitals']['oxygen']}")
    else:
        print("No vitals available..") 

    print("Active Medications:")    
    for med in p['medications']:
        print(f"- {med}")

def display_appointment_schedule(doctor_id):
    print("=== APPOINTMENT SCHEDULE ===")
    doc = medical_staff.get(doctor_id, {}).get("name", "Unknown Doctor")
    spec = medical_staff.get(doctor_id, {}).get("specialization", "General")
    print(f"{doc} - {spec}")
    for app in appointments:
        if app["doctor_id"] == doctor_id:
            patient_name = patients.get(str(app["patient_id"]), {}).get("personal_info", {}).get("name", "Unknown")
            print(f"{app['appointment_date']} - {app['appointment_type'].title()} - {patient_name}")

def display_billing_summary(patient_id):
    print("=== BILLING SUMMARY ===")
    p = patients.get(str(patient_id), {})
    name = p.get("personal_info", {}).get("name", "Unknown")
    print(f"Patient: {name}")
    for b in billing:
        if str(b["patient_id"]) == str(patient_id):
            print(f"Admission Date: {b.get('admission_date', 'N/A')}")
            print(f"Discharge Date: {b.get('discharge_date', 'N/A')}")
            print("Service Charges:")
            for service, cost in b.get("services", {}).items():
                print(f"{service}: {cost}")
            print(f"Total Bill: {b['total']}")
            print(f"Insurance Coverage (80%): {b['insurance']}")
            print(f"Patient Responsibility: {b['due']}")
register_patient(
    "P12345", 
    {"name": "Rajesh Kumar", "age": 45, "gender": "Male", "blood_type": "B+"},
    {"diagnosis": ["Hypertension", "Diabetes"]},
    {"name": "Star Health", "ID": "SH789456"}
)

register_patient("42089",{"name":"alex","mobile":8567138452,"Blood_type":"O+"},{"diagnosis":["ashtma","bp","sugar"]},{"name":"policybazar","ID":"PB0008"})
register_patient("42090",{"name":"John","mobile":7183924763,"Blood_type":"O-"},{"diagnosis":["ashtma","lowbp","sugar","fitz"]},{"name":"LIC","ID":"LIC0008"})
register_patient("42980",{"name":"Peter","mobile":8567183469,"Blood_type":"AB+"},{"diagnosis":["fever","cough","headache"]},{"name":"axis-max-life","ID":"AML0008"})

add_medical_staff(143,"bhavan","GeneralDoctor",[
    {"day": "Monday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "OPD"},
    {"day": "Tuesday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "OPD"},
    {"day": "Wednesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Wards"},
    {"day": "Thursday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Emergency"},
    {"day": "Friday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "OPD"},
    {"day": "Saturday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "OPD/Wards"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}],
    {"mobile.no":9666688887,"email":"ahbv@email.com"})
add_medical_staff(101143,"Dr.Santosh","Ortho Surgeon",[
    {"day": "Monday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Neuro OPD"},
    {"day": "Tuesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Neuro Ward"},
    {"day": "Wednesday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "Neurology & ICU"},
    {"day": "Thursday", "shift": "Off", "start": "-", "end": "-", "location": "-"},
    {"day": "Friday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Neuro OPD"},
    {"day": "Saturday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Neuro Ward"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}
    ],
    {"mobile.no":8937384574,"email":"sjdbxc4t@email.com"})
add_medical_staff(101243,"Dr.Jay Kumar","emergency doctor",[
    {"day": "Monday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Cardiology OPD"},
    {"day": "Tuesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Cardiology Ward"},
    {"day": "Wednesday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "ICU"},
    {"day": "Thursday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Cath Lab"},
    {"day": "Friday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "OPD & Ward"},
    {"day": "Saturday", "shift": "On Call", "start": "-", "end": "-", "location": "-"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}
    ], {"mobile.no":73948512358,"email":"ewwfgyreug@email.com"})

create_medical_record(
    "P12345", 
    101143, 
    diagnosis=["Hypertension", "High Cholesterol"],
    treatment="Lifestyle modification + medication",
    prescription=[
        "Metoprolol 50mg - Twice daily",
        "Aspirin 75mg - Once daily",
        "Atorvastatin 20mg - Bedtime"
    ]
)
create_medical_record(
    "42089", 
    143, 
    diagnosis=["Hypertension", "High Cholesterol"],
    treatment="Lifestyle modification + medication",
    prescription=[
        "Metoprolol 50mg - Twice daily",
        "Aspirin 75mg - Once daily",
        "Atorvastatin 20mg - Bedtime"
    ]
)
assign_room("P12345","general_ward",x.strftime("%d/%m/%Y"),3)
assign_room("42090","ac_ward",x.strftime("%d/%m/%Y"),5)
assign_room("42089","ac_ward",x.strftime("%d/%m/%Y"),4)
patients["P12345"]["vitals"] = {
    "date": "March 17, 2025 - 8:00 AM",
    "blood_pressure": "130/85 mmHg",
    "heart_rate": "78 BPM",
    "temperature": "98.6°F",
    "oxygen": "97%"
}
patients["42089"]["vitals"] = {
    "date": "March 17, 2025 - 8:00 AM",
    "blood_pressure": "130/85 mmHg",
    "heart_rate": "78 BPM",
    "temperature": "98.6°F",
    "oxygen": "97%"
}

schedule_appointment("P12345",101143,x.strftime("%d/%m/%Y"),"consultation")
schedule_appointment("42089",143,x.strftime("%d/%m/%Y"),"ECG-TEST")
schedule_appointment("42089",143,x.strftime("%d/%m/%Y"),"consultation")
schedule_appointment("42089",143,x.strftime("%d/%m/%Y"),"surgery")
schedule_appointment("42090",101243,x.strftime("%d/%m/%Y"),"consultation")
process_billing("P12345", [
    {"name": "Room Charges (3 days)", "cost": 4500},
    {"name": "Doctor Consultation", "cost": 2000},
    {"name": "ECG Test", "cost": 800},
    {"name": "Blood Tests", "cost": 1200},
    {"name": "Medications", "cost": 1800},
    {"name": "Nursing Care", "cost": 2400}
], insurance_coverage=80)
process_billing("42089", [
    {"name": "Room Charges (5 days)", "cost": 10000},
    {"name": "Doctor Consultation", "cost": 2000},
    {"name": "ECG Test", "cost": 800},
    {"name": "Blood Tests", "cost": 1200},
    {"name": "Medications", "cost": 1800},
    {"name": "Nursing Care", "cost": 2400}
], insurance_coverage=80)
process_billing("42090", [
    {"name": "Room Charges (4 days)", "cost": 8000},
    {"name": "Doctor Consultation", "cost": 2000},
    {"name": "ECG Test", "cost": 800},
    {"name": "Blood Tests", "cost": 1200},
    {"name": "Medications", "cost": 1800},
    {"name": "Nursing Care", "cost": 2400}
], insurance_coverage=80)
manage_discharge_process("P12345", "2025-03-18", "Return after 2 weeks for follow-up")

manage_discharge_process("42089", "2025-03-18", "Return after 10 weeks for follow-up")

manage_discharge_process("42090", "2025-03-18", "Return after 1 weeks for follow-up")


display_patient_dashboard("42089")
display_appointment_schedule(143)
display_billing_summary("42089")

# display_patient_dashboard("P12345")
# display_appointment_schedule(101143)
# display_billing_summary("P12345")
