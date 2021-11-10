# run in terminal (Ctrl+j)
# streamlit run databases/ui_for_db.py

from sqlalchemy.orm import query_expression
import streamlit as st
from db_example1 import open_db
from db_example1 import Student, Grades

def show_student_form():
    with st.form('f1'):
        name = st.text_input("Enter Student Name ->>>")
        c1,c2 = st.columns(2)
        klass = c1.text_input('Enter Student class ->>>')
        section = c2.text_input('Enter Student section ->>>')
        is_online = st.checkbox('is student attending online?')
        btn = st.form_submit_button('Add student')
    if btn and name and klass and section:
        db = open_db()
        db.add(Student(name=name,section=section,klass = klass, is_online=is_online))    # add student detail
        db.commit() #save
        db.close() #close the db
        st.success('Saved Student Details')

def grading_form():
    pass

def show_students_data():
    db= open_db()
    Student_list = db.query(Student).all()
    db.close()
    for student in Student_list:
        with st.expander(f'Student Detail {student.name}',False):
            st.subheader(student.name)
            st.markdown(f'''
            - class : {student.klass}
            - section : {student.section}
            - online : {'✔️' if student.is_online else '❌'}
            - admit date : {student.admit_date}
            ''')
            btn = st.button(f"delete {student.name}")
            if btn:
                db = open_db()
                std = db.query(Student).get(student.id)
                db.delete(std)
                db.commit()
                st.success("Student Executed, Press R to move on 😎")

def find_student():
    with st.form('search form'):
        params = ['id','name','section','class']
        c1, c2 = st.columns(2)
        by = c1.selectbox("Search Student By",options= params)
        query = c2.text_input("type keyword here")
        btn = st.form_submit_button("search")

    result = None
    db = open_db()
    if btn and query:
        if by == params[0]:
            result= db.query(Student).filter(Student.id==query)
        if by==params[1]:
            result= db.query(Student).filter(Student.name==query)
        if by==params[2]:
            result= db.query(Student).filter(Student.klass==query)
        if by==params[3]:
            result= db.query(Student).filter(Student.section==query)
    if result:
        st.write(result)
    db.close()


st.title("Database Example")

options = ['View Students','Find Student','View Grades','Add Students','Add Grades']

choice = st.sidebar.radio('Select any option', options)

if choice == options[0]:
    show_students_data()
elif choice == options[1]:
    find_student()
elif choice == options[2]:
    pass
elif choice == options[3]:
    show_student_form()
elif choice == options[4]:
    grading_form()