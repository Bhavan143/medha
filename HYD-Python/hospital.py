
import datetime 
x=datetime.datetime.now()
medical_inventory={}
doctors={}
medical_staff={}
patients={}
rooms = {
    "general_wards": 20,
    "ac_wards": 10,
    "emergency_wards": 10
}
room_assignment={}
medical_record={}
appointments=[]
billing=[]



def register_patient(patient_id,personal_info,medical_history,insurance_info):
    patient={
        patient_id:{
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


def create_medical_record(patient_id, doctor_id, diagnosis, treatment, prescription):
    for appointment in appointments["doctor_id"]:
        if patient_id==appointment[patient_id]:
            record={
            patient_id:{
            "doctor_id":doctor_id,
            "diagnosis":diagnosis,
            "treatment":treatment,
            "prescription":prescription
            }}
            medical_record.update(record)
        else:
            print("Register patient please..!")

def process_billing(patient_id, services_list, insurance_coverage):
    total_bill=sum(service["cost"] for service in services_list)
    covered_amount=total_bill*(insurance_coverage/100)
    due=total_bill-covered_amount
    billing.append({
        "patient_id": patient_id,
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
    if patient_id not in patients:
        print("Unregistered patient. Registering now...")
        register_patient(patient_id, {"name": "Unknown", "mobile": None}, {}, {})
    assign_room(patient_id, "emergency_wards", x.strftime("%Y-%m-%d"), 3)
    print(f"Emergency patient {patient_id} admitted for {emergency_type} with severity {severity_level}")

def track_medication_inventory(medication_id, quantity, expiry_date, supplier):
     medical_inventory[medication_id] = {
        "quantity": quantity,
        "expiry_date": expiry_date,
        "supplier": supplier
    }

def assign_room(patient_id, room_type, admission_date, expected_duration):
    if rooms.get(room_type,0)>0:
        rooms[room_type]-=1
        room_id = f"{room_type}_{len(room_assignment) + 1}"
        room_assignment[patient_id]={
        "patient_id":patient_id,
        "room_type":room_type,
        "admission_date":admission_date,
        "expected_duration":expected_duration
        }
        patients[patient_id]["status"] = "Inpatient"
        patients[patient_id]["room"] = room_id
        patients[patient_id]["admitted_on"] = admission_date        
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
        print("=== BILLING SUMMARY ===")
        for bill in billing:
            if bill["patient_id"] == patient_id:
                print(f"Total: {bill['total']}, Covered: {bill['covered']}, Due: {bill['due']}")
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
    if patient_id in room_assignment:
        room_type = room_assignment[patient_id]["room_type"]
        rooms[room_type] += 1
        del room_assignment[patient_id]
    patients[patient_id]["status"] = "Discharged"
    patients[patient_id]["discharged_on"] = discharge_date
    patients[patient_id]["follow_up"] = follow_up_instructions

def display_patient_dashboard(patient_id):
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
    if p['doctor_id']:
        doc = medical_staff.get(p['doctor_id'], {}).get("name", "Unknown")
        print(f"Attending Doctor: {doc}")
    print("Active Medications:")
    for med in p['medications']:
        print(f"- {med}")

    

register_patient(42089,{"name":"alex","mobile":8567138452,},{"diagnosis":["ashtma","bp","sugar"]},{"name":"policybazar","ID":"PB0008"})
register_patient(42090,{"name":"John","mobile":7183924763,},{"diagnosis":["ashtma","lowbp","sugar","fitz"]},{"name":"LIC","ID":"LIC0008"})
register_patient(42980,{"name":"Peter","mobile":8567183469,},{"diagnosis":["fever","cough","headache"]},{"name":"axis-max-life","ID":"AML0008"})
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
schedule_appointment(420,143,x.strftime("%d/%m/%Y"),"consultation")
    
