# using MySQL and streamlit

import mysql.connector
import streamlit as st
from Crypto.Cipher import DES, AES
import hashlib
import base32hex
import pandas as pd 

def DES_Encryption(passwords):
    key = b'!@#$1!15'
    cipher = DES.new(key, DES.MODE_EAX)
    passwords = passwords.encode()
    nonce = cipher.nonce
    cipherText = cipher.encrypt(passwords)
    encode_string= base32hex.b32encode(cipherText)
    return encode_string
 
def AES_Encryption(passwords):
    key = b'!@#$123bh924y1!@'
    cipher = AES.new(key, AES.MODE_EAX)
    passwords = passwords.encode()
    nonce = cipher.nonce
    cipherText = cipher.encrypt(passwords)
    encode_string= base32hex.b32encode(cipherText)
    return encode_string
 
def Hash(passwords):
    hash_obj = hashlib.md5(passwords.encode())
    return hash_obj.hexdigest()
 
# connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3306",
  password="root",
  database = "sql_i",
)
mycursor = mydb.cursor()
 
st.title("SQL INJECTION")


opt = st.sidebar.selectbox("Menu",["Register", "Login", "List All"])

if opt == "Register":
    st.header("User Registration")
    
    username = st.text_input("Enter the Username : ")
    password = st.text_input("Enter the password : ")
    
    enc1 = DES_Encryption(password)
    enc2 = AES_Encryption(password)
    hashed_enc = Hash(password)
    
    register = st.button("Register")
    
    if register:
        mycursor.execute("INSERT INTO userAccounts (user_name, enc1_pass, enc2_pass, hashed_pass) Values('{}', '{}', '{}', '{}')".format(username, enc1, enc2, hashed_enc))
        mydb.commit()
        st.success("User REgistered")
 
 
if opt == "Login":
    st.header("Login")
    username1 = st.text_input("Enter the username : ", key="1")
    password1 = st.text_input("Enter the password : ", key='2')
    hashed_pass = Hash(password1)
    
    button = st.button("Login")
    if button:
        mycursor.execute("select * from userAccounts where user_name = '%s' and hashed_pass = '%s'" %(username1, hashed_pass))
        for i in mycursor:
            st.write(i[0], i[3])
            st.success("success loggged in")

if opt == "List All":
    if st.button("List All"):
        mycursor.execute("select * from userAccounts")
        for i in mycursor:
            st.write(i[0],i[3])

    if st.button("Table Format all passwords"):
        mycursor.execute("select * from userAccounts")
        result = mycursor.fetchall()
        results=pd.DataFrame(result, columns=["name", "enc1", "enc2", "hsh_enc"])
        st.dataframe(results)


