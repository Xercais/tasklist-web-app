import streamlit as st
import functions

tasks = functions.get_tasklist()


def add_task():
    task_local = st.session_state['new_task'] + '\n'
    tasks.append(task_local)
    functions.write_tasklist(tasks)


st.title("My Tasklist App")
st.subheader("Your tasklist: ")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasklist(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input(label="Enter a task: ", placeholder="Add new task...",
              on_change=add_task, key='new_task')

