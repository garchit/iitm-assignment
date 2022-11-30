import numpy as np
import pandas as pd
import streamlit as st


def main():
  


  st.title("Even or Odd")
  a=st.number_input("Enter Number")
  

  if(a%2==0):
    st.write("Num is EVEN")
  else:
    st.write("Num is ODD")
  

  
if __name__=='__main__':
  main()
#   main()

#     main()
