import datetime
import time
from tkinter import *

from random import randint


def clear(*args):
    for arg in args:
        if arg == txt_city or arg == txt_overtime or arg == txt_basic_salary:
            arg.delete(1, END)

        else:
            arg.delete(0, END)


def pay_ref():
    clear(txt_pay_date, txt_reference, txt_ni_number)
    txt_pay_date.insert(0, time.strftime("%x"))
    txt_reference.insert(0, f"PR{randint(20_000, 709_467)}")
    txt_ni_number.insert(0, f"NI{randint(4_200, 9_467)}")


def pay_period():
    clear(txt_ni_code, txt_tax_period)
    current_date = datetime.datetime.now()
    txt_tax_period.insert(0, str(current_date.month))
    txt_ni_code.insert(0, f"NICode{randint(4_200,  9_467)}")


def reset():
    clear(txt_ni_code, txt_ni_number, txt_reference, txt_ni_payment, txt_deductions, txt_tax, txt_tax_period,
          txt_post_code, txt_taxable_pay, txt_stud_loan, txt_net_pay, txt_gender, txt_basic_salary,
          txt_pensionable_pay, txt_pay_date, txt_pension, txt_address, txt_overtime, txt_other_payments_due,
          txt_employer_name, txt_employee_name, txt_city, txt_gross_pay)


def format_figures(number):
    return '$%.2f' % number


def monthly_salary():
    get_basic_salary = txt_basic_salary.get()
    basic_salary = float(get_basic_salary[1:])

    get_overtime = txt_overtime.get()
    overtime = float(get_overtime[1:])

    weighting = txt_city.get()
    city_weighting = float(weighting[1:])

    gross_pay = basic_salary + overtime + city_weighting
    tax = 0.3 * gross_pay
    pension = 0.02 * gross_pay
    student_loan = 0.01 * gross_pay
    ni_payment = 0.011 * gross_pay
    deduction = tax + pension + student_loan + ni_payment
    net_salary = gross_pay - deduction

    txt_gross_pay.insert(0, format_figures(gross_pay))
    txt_tax.insert(0, format_figures(tax))
    txt_pension.insert(0, format_figures(pension))
    txt_ni_payment.insert(0, format_figures(ni_payment))
    txt_stud_loan.insert(0, format_figures(student_loan))
    txt_deductions.insert(0, format_figures(deduction))
    txt_net_pay.insert(0, format_figures(net_salary))
    txt_taxable_pay.insert(0, txt_tax.get())
    txt_pensionable_pay.insert(0, txt_pension.get())
    txt_other_payments_due.insert(0, '$0.00')


def exit_system():
    payroll.destroy()


payroll = Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management System")

# =========================================THE TOP==================================================================

Tops = Frame(payroll, width=1350, height=50, bd=16, relief="raised", bg='gray')
Tops.pack(side=TOP)
label_info = Label(Tops, font=('Arial', 50, 'bold'), text="Payroll Management Systems", fg="Steel blue", bd=1,
                   padx=184, pady=35)
label_info.grid(row=0, column=0)

# ======================================LEFT FRAMES=================================================================

left_frame = Frame(payroll, width=700, height=650, bd=16, relief="raised", bg='cadet blue')
left_frame.pack(side=LEFT)

left_frame_top = Frame(left_frame, width=700, height=100, bd=8, relief="raised")
left_frame_top.pack(side=TOP)
left_frame_left = Frame(left_frame, width=325, height=400, bd=8, relief="raised")
left_frame_left.pack(side=LEFT)
left_frame_right = Frame(left_frame, width=325, height=400, bd=8, relief="raised")
left_frame_right.pack(side=RIGHT)

# ======================================RIGHT FRAMES================================================================

right_frame = Frame(payroll, width=600, height=650, bd=16, relief="raised", bg='light gray')
right_frame.pack(side=RIGHT)

right_frame_top = Frame(right_frame, width=600, height=200, bd=8, relief="raised")
right_frame_top.pack(side=TOP)
right_frame_left = Frame(right_frame, width=300, height=400, bd=8, relief="raised")
right_frame_left.pack(side=LEFT)
right_frame_right = Frame(right_frame, width=300, height=400, bd=8, relief="raised")
right_frame_right.pack(side=RIGHT)

# =====================================LEFT SIDE===================================================================

# ======================================Top of LEFT SIDE============================================================

lbl_employee_name = Label(left_frame_top, font=('Arial', 12, 'bold'), text="Employee Name", fg="Steel blue", bd=10,
                          anchor='w')
lbl_employee_name.grid(row=0, column=0)
txt_employee_name = Entry(left_frame_top, font=('Arial', 12, 'bold'), bd=10, width=54, bg="powder blue",
                          justify='left')
txt_employee_name.grid(row=0, column=1)

lbl_address = Label(left_frame_top, font=('Arial', 12, 'bold'), text="Address", fg="Steel blue", bd=10, anchor='w')
lbl_address.grid(row=1, column=0)
txt_address = Entry(left_frame_top, font=('Arial', 12, 'bold'), bd=10, width=54, bg="powder blue", justify='left')
txt_address.grid(row=1, column=1)

lbl_reference = Label(left_frame_top, font=('Arial', 12, 'bold'), text="Reference", fg="Steel blue", bd=10,
                      anchor='w')
lbl_reference.grid(row=2, column=0)
txt_reference = Entry(left_frame_top, font=('Arial', 12, 'bold'), bd=10, width=54, bg="powder blue", justify='left')
txt_reference.grid(row=2, column=1)

lbl_employer_name = Label(left_frame_top, font=('Arial', 12, 'bold'), text="Employer Name", fg="Steel blue", bd=10,
                          anchor='w')
lbl_employer_name.grid(row=3, column=0)
txt_employer_name = Entry(left_frame_top, font=('Arial', 12, 'bold'), bd=10, width=54, bg="powder blue",
                          justify='left')
txt_employer_name.grid(row=3, column=1)

# =========================================Left of LEFT SIDE=======================================================

lbl_tax = Label(left_frame_left, font=('Arial', 12, 'bold'), text="Tax", fg="Steel blue", bd=10, anchor='w')
lbl_tax.grid(row=0, column=0)
txt_tax = Entry(left_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify='left')
txt_tax.grid(row=0, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_pension = Label(left_frame_left, font=('Arial', 12, 'bold'), text="Pension", fg="Steel blue", bd=10, anchor='w')
lbl_pension.grid(row=1, column=0)
txt_pension = Entry(left_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify='left')
txt_pension.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_stud_loan = Label(left_frame_left, font=('Arial', 12, 'bold'), text="Student Loan", fg="Steel blue", bd=10,
                      anchor='w')
lbl_stud_loan.grid(row=2, column=0)
txt_stud_loan = Entry(left_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                      justify='left')
txt_stud_loan.grid(row=2, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_ni_payment = Label(left_frame_left, font=('Arial', 12, 'bold'), text="NI Payment", fg="Steel blue", bd=10,
                       anchor='w')
lbl_ni_payment.grid(row=3, column=0)
txt_ni_payment = Entry(left_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                       justify='left')
txt_ni_payment.grid(row=3, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_deductions = Label(left_frame_left, font=('Arial', 12, 'bold'), text="Deductions", fg="Steel blue", bd=10,
                       anchor='w')
lbl_deductions.grid(row=4, column=0)
txt_deductions = Entry(left_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                       justify='left')
txt_deductions.grid(row=4, column=1)

# =====================================left of LEFT SIDE ===========================================================

lbl_city = Label(left_frame_right, font=('Arial', 12, 'bold'), text="City Weighting", fg="Steel blue", bd=10,
                 anchor='w')
lbl_city.grid(row=0, column=0)
txt_city = Entry(left_frame_right, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify='left')
txt_city.insert(0, '$')
txt_city.grid(row=0, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_basic_salary = Label(left_frame_right, font=('Arial', 12, 'bold'), text="Basic Salary", fg="Steel blue", bd=10,
                         anchor='w')
lbl_basic_salary.grid(row=1, column=0)
txt_basic_salary = Entry(left_frame_right, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                         justify='left')
txt_basic_salary.insert(0, '$')
txt_basic_salary.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_overtime = Label(left_frame_right, font=('Arial', 12, 'bold'), text="Over Time", fg="Steel blue", bd=10,
                     anchor='w')
lbl_overtime.grid(row=2, column=0)
txt_overtime = Entry(left_frame_right, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                     justify='left')
txt_overtime.insert(0, '$')
txt_overtime.grid(row=2, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_gross_pay = Label(left_frame_right, font=('Arial', 12, 'bold'), text="Gross Pay", fg="Steel blue", bd=10,
                      anchor='w')
lbl_gross_pay.grid(row=3, column=0)
txt_gross_pay = Entry(left_frame_right, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                      justify='left')
txt_gross_pay.grid(row=3, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_net_pay = Label(left_frame_right, font=('Arial', 12, 'bold'), text="Net Pay", fg="Steel blue", bd=10,
                    anchor='w')
lbl_net_pay.grid(row=4, column=0)
txt_net_pay = Entry(left_frame_right, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify='left')
txt_net_pay.grid(row=4, column=1)

# =====================================RIGHT Side ==================================================================

# =====================================Top of RIGHT SIDE ===========================================================

lbl_post_code = Label(right_frame_top, font=('Arial', 12, 'bold'), text="Post Code", fg="Steel blue", bd=10,
                      anchor='w')
lbl_post_code.grid(row=0, column=0)
txt_post_code = Entry(right_frame_top, font=('Arial', 12, 'bold'), bd=10, width=52, bg="powder blue",
                      justify='left')
txt_post_code.grid(row=0, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_gender = Label(right_frame_top, font=('Arial', 12, 'bold'), text="Gender", fg="Steel blue", bd=10, anchor='w')
lbl_gender.grid(row=1, column=0)
txt_gender = Entry(right_frame_top, font=('Arial', 12, 'bold'), bd=10, width=52, bg="powder blue", justify='left')
txt_gender.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------------------

# =========================================Left of RIGHT SIDE ======================================================

lbl_pay_date = Label(right_frame_left, font=('Arial', 12, 'bold'), text="Pay Date", fg="Steel blue", bd=10,
                     anchor='w')
lbl_pay_date.grid(row=0, column=0)
txt_pay_date = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                     justify='left')
txt_pay_date.grid(row=0, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_tax_period = Label(right_frame_left, font=('Arial', 12, 'bold'), text="Tax Period", fg="Steel blue", bd=10,
                       anchor='w')
lbl_tax_period.grid(row=1, column=0)
txt_tax_period = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                       justify='left')
txt_tax_period.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_ni_number = Label(right_frame_left, font=('Arial', 12, 'bold'), text="NI Number", fg="Steel blue", bd=10,
                      anchor='w')
lbl_ni_number.grid(row=2, column=0)
txt_ni_number = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                      justify='left')
txt_ni_number.grid(row=2, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_ni_code = Label(right_frame_left, font=('Arial', 12, 'bold'), text="NI Code", fg="Steel blue", bd=10,
                    anchor='w')
lbl_ni_code.grid(row=3, column=0)
txt_ni_code = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify='left')
txt_ni_code.grid(row=3, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_taxable_pay = Label(right_frame_left, font=('Arial', 12, 'bold'), text="Taxable Pay", fg="Steel blue", bd=10,
                        anchor='w')
lbl_taxable_pay.grid(row=4, column=0)
txt_taxable_pay = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                        justify='left')
txt_taxable_pay.grid(row=4, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_pensionable_pay = Label(right_frame_left, font=('Arial', 12, 'bold'), text="Pensionable Pay", fg="Steel blue",
                            bd=10, anchor='w')
lbl_pensionable_pay.grid(row=5, column=0)
txt_pensionable_pay = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                            justify='left')
txt_pensionable_pay.grid(row=5, column=1)

# ----------------------------------------------------------------------------------------------------------------------

lbl_other_payments_due = Label(right_frame_left, font=('Arial', 12, 'bold'), text="Other Payments Due",
                               fg="Steel blue", bd=10, anchor='w')
lbl_other_payments_due.grid(row=6, column=0)
txt_other_payments_due = Entry(right_frame_left, font=('Arial', 12, 'bold'), bd=10, width=18, bg="powder blue",
                               justify='left')
txt_other_payments_due.grid(row=6, column=1)

# ----------------------------------------------------------------------------------------------------------------------

# =====================================Right of RIGHT SIDE =========================================================

# =========================================BUTTONS======================================================================

btn_wage_payment = Button(right_frame_right, text="Wage Payment", font=('Arial', 16, 'bold'), pady=8, fg="black",
                          width=14, bd=8, relief="raised", command=monthly_salary)
btn_wage_payment.grid(row=0, column=1)

# ----------------------------------------------------------------------------------------------------------------------

btn_reset_system = Button(right_frame_right, text="Reset System", font=('Arial', 16, 'bold'), fg="black", pady=8,
                          width=14, bd=8, relief="raised", command=reset)
btn_reset_system.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------------------

btn_pay_reference = Button(right_frame_right, text="Pay Reference", font=('Arial', 16, 'bold'), fg="black",
                           width=14,
                           pady=8, bd=8, relief="raised", command=pay_ref)
btn_pay_reference.grid(row=2, column=1)

# ----------------------------------------------------------------------------------------------------------------------

btn_pay_code = Button(right_frame_right, text="Pay Code", font=('Arial', 16, 'bold'), fg="black", width=14, bd=8,
                      pady=8, relief="raised", command=pay_period)
btn_pay_code.grid(row=3, column=1)

# ----------------------------------------------------------------------------------------------------------------------

btn_exit = Button(right_frame_right, text="Exit", font=('Arial', 16, 'bold'), fg="black", width=14, bd=8, pady=8,
                  relief="raised", command=exit_system)
btn_exit.grid(row=4, column=1)

# ----------------------------------------------------------------------------------------------------------------------

payroll.mainloop()
