"""
Module: doctors

An application to solve the Doctors Without Orders problem.

Authors:
1. Maggie Cope
2. Darby Hunter 
"""

from sys import argv, exit
from dataclasses import dataclass

def hour_or_hours(num_hours: int) -> str:
    """Helper function to get correct pluralization."""
    assert num_hours >= 0
    return "hour" if num_hours == 1 else "hours"


@dataclass(frozen=True)
class Doctor:
    """A representation of a Doctor, including their name and the maximum
    available hours for scheduling (max_hours).

    Doctors are immutable (i.e. can't change any of their two attributes).

    DO NOT MODIFY THIS CLASS IN ANY WAY!!!

    >>> dr_sat = Doctor("Sat Garcia", 7)
    >>> dr_sat.name
    'Sat Garcia'
    >>> dr_sat.max_hours
    7
    >>> dr_sat.max_hours = 11
    Traceback (most recent call last):
        ...
    dataclasses.FrozenInstanceError: cannot assign to field 'max_hours'
    """
    name: str
    max_hours: int

    def __str__(self) -> str:
        h = hour_or_hours(self.max_hours)
        return f"Doctor {self.name} ({self.max_hours} {h})"


@dataclass(frozen=True)
class Patient:
    """A representation of a Patient, including their name and the number of
    hours they need to be seen for (needed_hours).

    Patients are immutable (i.e. can't change any of their two attributes).

    DO NOT MODIFY THIS CLASS IN ANY WAY!!!

    >>> ouchy = Patient("Ben Hurt", 3)
    >>> ouchy.name
    'Ben Hurt'
    >>> ouchy.needed_hours
    3
    >>> ouchy.needed_hours = 1
    Traceback (most recent call last):
        ...
    dataclasses.FrozenInstanceError: cannot assign to field 'needed_hours'
    """
    name: str
    needed_hours: int

    def __str__(self) -> str:
        h = hour_or_hours(self.needed_hours)
        return f"Patient {self.name} ({self.needed_hours} {h})"


def parse_scheduling_data(filename: str) -> tuple[list[Doctor], list[Patient]]:
    """
    Reads the doctor and patient data from <filename>, returning a list of
    Doctors and and a list of Patients.

    DO NOT MODIFY THIS FUNCTION IN ANY WAY!!!

    Parameters:
        filename (str): Name of the file containing doctor and patient info.

    Returns:
        (tuple[list[Doctor], list[Patient]]): Two lists: the first of doctors
            and the second of patients, gathered from the specified file.
    """
    docs = []
    patients = []

    with open(filename, 'r') as f:
        all_lines = f.readlines()

        i = 0
        while i < len(all_lines) and (all_lines[i][0] == '#' or
                                      all_lines[i].strip() == ""):
            i += 1

        for line_num in range(i, len(all_lines)):
            line = all_lines[line_num]
            person_info, hours = line.split(':')
            person_split = person_info.split()
            title = person_split[0]
            name = " ".join(person_split[1:])

            if title == "Doctor":
                docs.append(Doctor(name, int(hours)))
            else:
                patients.append(Patient(name, int(hours)))

    return docs, patients

def hours_left(doctor: Doctor,  schedule: dict[Doctor, set[Patient]] ) -> int: 
    """
    Helper fuction for can_schedule_all returns an int(time) of the number of hours a doctor can still work based on their schedule
   
    Parameters: 
    doctor(Doctor Object)
    schedule(dict[Doctor, set[Patient]]) - dictionary of all the doctors (the keys) associated with a set of patients (the values) 

    Return: 
    time(int) - the number of hours a doctor can still work based on the patients they are already seeing
    """
    #sets time to the doctors max hours 
    time = doctor.max_hours
    
    # for every patient in the doctors schedule, subtracts the hours the patient needs from time 
    for patient in schedule[doctor]:
        time -= patient.needed_hours
    #returns the amount of time the doctor can still work 
    return time


def can_schedule_all(doctors: list[Doctor], patients: list[Patient], schedule: dict[Doctor, set[Patient]]) -> bool:
    """This function takes as input a list of doctors and a list of patients, 
    then returns whether it’s possible to schedule all the patients so that 
    each one is seen by a doctor for the appropriate amount of time. It also updates the schedule based on the patients a doctor will see
    
    Parameters:
    doctors(list[Doctor]) - list of Doctor objects 
    patients(list[Patient]) - list of Patient objects 
    schedule(dict[Doctor, set[Patient]]) - dictionary that schedule has all of the doctors (the keys) associated with a set of empty patients (the values) 

    Return(bool):
    True - if all the patients can be seen 
    False - if not  
    """
    #base case1 
    if len(doctors) == 0 and len(patients) != 0:
        return False 
    #base case 2
    if len(patients)==0: 
        #returns true if all the patients can be seen 
        return True 
    
    #loops through one doctor at a time, deciding which subset of patients that doctor should see. 
    for doctor in doctors: 
        doctor_hours_left = hours_left(doctor, schedule)
        if (doctor_hours_left - patients[0].needed_hours) >= 0:
            schedule[doctor].add(patients[0])
            return can_schedule_all(doctors, patients[1:], schedule) 
    #if there is not possible schedule, returns False 
  
    return False 

          
                
        
            
   

  
       

              





if __name__ == "__main__":
    if len(argv) != 2:
        print("Error: wrong number of command line parameters")
        exit(1)

    docs, patients = parse_scheduling_data(argv[1])

    # create initial schedule, with each doctor assigned to no one!
    proposed_schedule: dict[Doctor, set[Patient]] = {d: set() for d in docs}

    if can_schedule_all(docs, patients, proposed_schedule):
        print("Proposed schedule:")
        for doc, docs_patients in proposed_schedule.items():
            patient_names = ", ".join([str(p) for p in docs_patients])
            print(f"\t{doc} -> {patient_names}")
    else:
        print("No valid schedule possible!")
