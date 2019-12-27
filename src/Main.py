from classes import Student
import sys

def createReport(path, report_array):
    file = open(path, 'w')
    file = open(path, 'a')
    for line in report_array:
        file.write(line)
    file.close()
        
def generateReportData(students_array, presence_array):
    report_array = []
    for student_name in students_array:
        total_days = 0
        total_minutes = 0
        for presence in presence_array:
            if presence[1] == student_name[1]:
                student = Student(presence[1], presence[3], presence[4], presence[5])
                total_days += 1
                minutes = student.getMinutesPerDay() 
                if minutes > 5:
                    total_minutes += minutes
                continue
        if total_minutes == 0:
            report_array.append(student_name[1] + ': ' + str(total_minutes) + ' minutes\n')
        days = ' days' if total_days > 1 else ' day'
        report_array.append(student_name[1] + ': ' + str(total_minutes) + ' minutes in ' + str(total_days) + days + '\n')
    return report_array


if __name__ == '__main__':
    filename = str(sys.argv[1])
    report_array = []
    report_file = 'output.txt'
    # read the file from argument
    with open(filename, 'r') as file:
        #read the file line by line
        lines = file.readlines()
        #arrays for each command
        students_array = []
        presence_array = []
        for line in lines:
            values_array = line.strip().split(' ')
            #divide file into two separates arrays
            if len(values_array) < 3:
                #with student command
                students_array.append(values_array)
                continue
            if len(values_array) > 5:
                #with presence command
                presence_array.append(values_array)
                continue
        #sort the arrays
        students_array.sort()
        presence_array.sort()
        report_data = generateReportData(students_array, presence_array)
        createReport(report_file, report_data)
        
        print('=D')