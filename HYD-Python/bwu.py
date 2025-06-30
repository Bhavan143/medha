
import datetime
patients={}
medical_staff={}
appointments=[]
x=datetime.datetime.now()
def register_patient(patient_id,personal_info,medical_history,insurance_info):
    patient={
        patient_id:{
        "personal_info":personal_info,
        "medical_history":medical_history,
        "insurance_info":insurance_info}
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
register_patient(420,{"name":"alex","mobile":8567138452,},{"diagnosis":["ashtma","bp","sugar"]},{"name":"policybazar","ID":"PB0008"})
add_medical_staff(143,"bhavan","cardiologist",[
    {"day": "Monday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "OPD"},
    {"day": "Tuesday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "OPD"},
    {"day": "Wednesday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "Wards"},
    {"day": "Thursday", "shift": "Evening", "start": "14:00", "end": "20:00", "location": "Emergency"},
    {"day": "Friday", "shift": "Morning", "start": "08:00", "end": "14:00", "location": "OPD"},
    {"day": "Saturday", "shift": "Full Day", "start": "08:00", "end": "20:00", "location": "OPD/Wards"},
    {"day": "Sunday", "shift": "Off", "start": "-", "end": "-", "location": "-"}],
    {"mobile.no":9666688887,"email":"ahbv@email.com"})
schedule_appointment(420,143,x.strftime("%d/%m/%Y"),"consultation")
print(patients)
print(medical_staff)
print(appointments)