import streamlit as st


def verbose_func(info, verbose=False, st_verbose=False):
    if verbose:
        print(info)
    if st_verbose:
        st.write(info)


def set_var(var='chat_history', define=0):
    if var not in st.session_state:
        st.session_state[var] = define


def get_var(var='inputs'):
    return st.session_state[var]


def update_var(var, data=0):
    st.session_state[var] = data



class Streamlit_helper():
    def notes(self):
        return 'unknown'

    def button_struct(self,name='name', next='next', button_name='内容确认',
                      init=False,func1=None, func2=None, func3=None,key=None,
                      ):
        """
        func1 常备运行
        func2 初始化执行 且静态显示 位置在按钮之前
        func3 初始化不执行 按钮执行 位置在按钮之后 非静态显示 执行显示
        """
        # 先赋值 在运行
        set_var(name, init)  # aa last
        set_var(name + 'self', True)
        func1 = func1 or (lambda: '')
        func1()
        if get_var(name):
            if get_var(name + 'self'):
                func2 = func2 or (lambda: '')
                func2()
            update_var(name + 'self', data=False)
            if st.button(button_name, type="primary",key=key):
                func3 = func3 or (lambda: '')
                func3()
                update_var(name, data=False)
                update_var(next, data=True)
                st.rerun()

#
# # mode()
# modes3('init', 'name', init=True, button_name='内容确认1')
# modes3('name', 'next', button_name='内容确认')
# modes3('next', 'next_1', button_name='内容确认2')
# modes3('next_1', 'next_2', button_name='内容确认3')
