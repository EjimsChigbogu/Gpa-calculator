import csv


with open('gpa_main.csv', 'r') as f:
        rows = csv.DictReader(f)
        
        cu = 0
        gpa = 0
        for row in rows:
                cu += int(row['credit_unit'])
                gpa += int(row['credit_unit']) * int(row['grade_point'])
        
        total_gpa = gpa / cu
        
        print(total_gpa)

