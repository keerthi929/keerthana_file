SELECT doctor,doctorID, patientID, lastVisit FROM
   Patients INNER JOIN (
      SELECT patientID, MAX(visitTime) AS lastVisit FROM Visits
      GROUP by patientID) latestVisits
   ON lastVisits.patentID = Patients.
   
   
   
   
 #  output
doctor     idDoctor  idPatient  
Dr.mani    5678          1
Dr.suresh   6775        2
Dr.manoj    3456         3



2)

SELECT count(DISTINCT patient) AS "No. of patients taken at least one appointment"
FROM appointment;



       output

doctor              patient id 
Dr.suresh          2
Dr.kani               3
Dr.thanishka     4
Dr.yamuna         5
Dr.roja                 6