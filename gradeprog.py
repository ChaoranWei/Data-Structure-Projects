'''This module enable us to sort in student data.

This module inputs student record file and then sort student information
according to alphabetic and grade order, and finally output a sorted file.

Author: Chaoran Wei(cwei02)
'''
class _StudentRecord :
    def __init__( self ):
        self.name = None
        self.grade = 0
        self.letter = None
        
def main():
    '''Integrates all functions and executes them to output sorted file.
    '''
    input_file = 'rawgrade.txt'
    output_file = 'procgrade.txt'
    unsorted_record1 = RecordRead(input_file)
    name_sorted = Namesort(unsorted_record1)
    unsorted_record2 = RecordRead(input_file)
    grade_sorted = Gradesort(unsorted_record2)
    Writefile(name_sorted, grade_sorted, output_file)
            
def RecordRead(file):
    '''Reads student data file into python and output a list of objects 
    storing the corresponding information.
    '''
    inputfile = open(file, 'r')
    record_list = []
    for line in inputfile:
        line = line.split()
        a = _StudentRecord()
        a.name = line[0]
        a.grade = int(line[1])
        record_list.append(a)
    inputfile.close()
    return record_list

def Namesort(unsorted_record):
    '''Sorts the list according to alphabetic order.
    '''
    sorted_record = unsorted_record
    n = len(sorted_record)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_record[j].name > sorted_record[j+1].name:
                tmp = unsorted_record[j]
                sorted_record[j] = sorted_record[j+1]
                sorted_record[j+1] = tmp
    return sorted_record     
        
def Gradesort(unsorted_record): 
    '''Sorts the list according to descending grade.
    '''
    sorted_record = unsorted_record
    n = len(sorted_record)
    for i in range(n-1):
        for j in range(n-i-1):
            if sorted_record[j].grade < sorted_record[j+1].grade:
                tmp = sorted_record[j]
                sorted_record[j] = sorted_record[j+1]
                sorted_record[j+1] = tmp        
            
    for i in range(n):
        if sorted_record[i].grade >= 90:
            sorted_record[i].letter = 'A'
        elif sorted_record[i].grade >= 80:
            sorted_record[i].letter = 'B'
        elif sorted_record[i].grade >= 70:
            sorted_record[i].letter = 'C'
        elif sorted_record[i].grade >= 60:
            sorted_record[i].letter = 'D'
        else:
            sorted_record[i].letter = 'F'
        
    return sorted_record           
    
        
def Writefile(name_sorted, grade_sorted, file):
    '''Writes the information contained in two sorted lists into a new file.
    '''
    output = open(file, 'w')
    n =len(name_sorted)
    output.write('Student records in alphabetic order:\n' + '\n')
    for i in range(n):
        b = name_sorted[i]
        output.write(b.name + '  ' + str(b.grade) + '\n')
        
    output.write('\n' + 'Student records by letter grades:\n' + '\n')
    for j in range(n):
        c = grade_sorted[j]
        output.write(c.name + '  ' + str(c.grade) + ' ' + c.letter + '\n')                  
    output.close()
    
main()

#do we need to use unsorted twice
#remember iterators
#how do we get hardware array in python