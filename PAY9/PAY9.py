__author__ = 'jrg92'

"""
gross = 0.00
tax = 0.00
union = 0.00
mortgage = 0.00
nett = 0.00
emp_no = ""
emp_name = ""


def initilize():
    global gross, tax, nett, emp_no, emp_name, mortgage, union
    gross = 0.00
    tax = 0.00
    union = 0.00
    mortgage = 0.00
    nett = 0.00
    emp_no = ""
    emp_name = ""
"""

employees = []
data = ""
total_gross = 0.00
total_tax = 0.00
total_union = 0.00
total_mortgage = 0.00
total_nett = 0.00
emp_count = 0
union_not_poss = False
mortgage_not_poss = False
total_exception = 0

data_array = []

def calc_values(emp_no, emp_name, hours, rate, union, mortgage):

    global employees, emp_count, union_not_poss, mortgage_not_poss, total_exception, total_union, total_mortgage

    union_not_poss = False
    mortgage_not_poss = False

    emp_count += 1
    gross = 0.00
    tax = 0.00
    nett = 0.00

    temp_data = []
    gross = hours * rate
    tax = gross * 0.25
    wf_super = gross * 0.06
    temp_ded = tax + wf_super
    nett = gross - temp_ded

    if union < nett:
        nett = nett - union
        total_union += union
    else:
        union_not_poss = True

    if mortgage < nett:
        nett = nett - mortgage
        total_mortgage += mortgage
    else:
        mortgage_not_poss = True


    if union_not_poss == True:
        union = "  *****"
        total_exception += 1

    if mortgage_not_poss == True:
        mortgage = "  *****"
        total_exception += 1

    if union == 0:
        union = ""
    if mortgage == 0:
        mortgage = ""
    temp_data.extend([emp_no, emp_name, gross, tax, union, mortgage, nett])
    employees.append(temp_data)


def calc_total():
    global total_gross, total_tax, total_union, total_mortgage, total_nett
    for emp in employees:
        for item in emp:
            if emp.index(item) == 2:
                total_gross += item
            elif emp.index(item) == 3:
                total_tax += item
            elif emp.index(item) == 6:
                total_nett += item

def view():
    for emp in employees:
        print(emp)
        #print(employees.index(emp))

def get_emp_from_file(data):
    emp_no = data[:6]
    emp_name = data[6:26]
    hours = data[26:28] + "." + data[28:30]
    rate = data[30:32] + "." + data[32:34]
    union = data[34:36] + "." + data[36:38]
    mortgage = data[38:41] + "." + data[41:43]

    print(emp_no, emp_name, hours, rate, union, mortgage)
    """
    for item in data:
        if data.index(item) == 5:
            pass
        elif data.index(item) == 25:
            pass
    """

def convert_to_number(num):
    pass

def trim_emp_no(num):
    return num.strip()

def trim_emp_name(name):
    return name.rstrip()

def load(path):
    global data, data_array
    with open(path, "r") as file:
        for line in file:
            data_array.append(line.rstrip('\n'))

if __name__ == "__main__":

    calc_values("111", "james", 20.00, 25.00, 10.00, 1000)
    calc_values("112", "james", 20.00, 25.00, 0, 56.70)
    calc_values("113", "james", 20.00, 25.00, 10.00, 56.70)
    calc_total()
    print(total_gross, total_tax, total_union, total_mortgage, total_nett)
    view()
    load("H:\PYTHON\Assignment2\sample.txt")
    print(data_array[0], len(data_array[1]))
    print("break" + trim_emp_no("    James"))

    get_emp_from_file("  5789Bob Billards        04600230190048945")
    a = "9099.98"
    b = float(a)
    #print("%.2f" % b)
    print("{0:.2f}".format(b))
    print("sadf/sdf\"")