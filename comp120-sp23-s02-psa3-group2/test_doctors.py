"""
Module: test_doctors

PyTest Unit Test cases for comp120 psa3 (Doctors Without Orders)
"""

# the following is the module(s) we are testing
import doctors
from doctors import Doctor, Patient

def test_no_patients():
    """Test for the base case of when there is a doctor but are no patients to be seen."""

    d = Doctor("D1", 100)
    schedule = {d: set()} # schedule has doctor with no patients

    result = doctors.can_schedule_all([d], [], {d: set()})
    assert result == True


def test_no_doctors():
    """Test for the base case of when there isn't a doctor but there are patients."""

    p = Patient("P1", 1)
    result = doctors.can_schedule_all([], [p], {})

    assert result == False

# Add your unit tests below this point


def test_one_doctor_one_patient_and_can_schedule():
    d = Doctor("D1", 100)
    p = Patient("P1", 2)
    result = doctors.can_schedule_all([d], [p], {d: set()})
    assert result == True 

def test_one_doctor_one_patient_and_can_not_schedule():
    d = Doctor("D1", 1)
    p = Patient("P1", 2)
    result = doctors.can_schedule_all([d], [p], {d: set()})
    assert result == False

def test_two_patients_one_doctor_True():
    d = Doctor("D1", 100)
    p1 = Patient("P1", 5)
    p2 = Patient("P2",6)
    result = doctors.can_schedule_all([d], [p1,p2], {d: set()})
    assert result == True 

def test_two_patients_one_doctor_False():
    d = Doctor("D1", 10)
    p1 = Patient("P1", 5)
    p2 = Patient("P2",6)
    result = doctors.can_schedule_all([d], [p1,p2], {d: set()})
    assert result == False 

def test_two_doctors_three_patients_True():
    d1 = Doctor("D1", 10)
    d2 = Doctor("D2",10)
    p1 = Patient("P1", 5)
    p2 = Patient("P2",6)
    p3 = Patient("P3",2)
    result = doctors.can_schedule_all([d1,d2], [p1,p2], {d1: set(), d2: set()})
    assert result == True 

def test_two_doctors_three_patients_False():
    d1 = Doctor("D1", 10)
    d2 = Doctor("D2",10)
    p1 = Patient("P1", 5)
    p2 = Patient("P2",6)
    p3 = Patient("P3",8)
    result = doctors.can_schedule_all([d1,d2], [p1,p2,p3], {d1: set(), d2: set()})
    assert result == False 

def test_five_doctors_two_patients_True():
    d1 = Doctor("D1",1)
    d2 = Doctor("D2", 7)
    d3 = Doctor("D3", 5)
    d4 = Doctor("D4", 20)
    d5 = Doctor("D5", 100)
    p1 = Patient("P1", 18)
    p2 = Patient("P2", 50)
    result = doctors.can_schedule_all([d1,d2,d3,d4,d5], [p1,p2], {d1: set(), d2: set(), d3: set(), d4: set(), d5: set()})
    assert result == True 