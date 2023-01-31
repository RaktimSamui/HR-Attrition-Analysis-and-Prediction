from joblib import load
import streamlit as st
import numpy as np

model=load("model.joblib")
def predict_func(age,bt,dt,dep,dfh,edu,edu_f,env_sat,gend,hour_rate,job_inv,job_lev,job_ro,job_sat,marital,month_rate,num_com_work,overtim,percent_sal_hike,relation_sat,stock_op,train_time,work_lif_bal,years_at_comp,years_since_last_promo):
    lis=[age,bt,dt,dep,dfh,edu,edu_f,env_sat,gend,hour_rate,job_inv,job_lev,job_ro,job_sat,marital,month_rate,num_com_work,overtim,percent_sal_hike,relation_sat,stock_op,train_time,work_lif_bal,years_at_comp,years_since_last_promo]
    ar=np.array(lis).reshape(1,-1)
    prediction=model.predict(ar)
    if prediction==0:
        st.success("Employee is not likely to leave")
    else:
        st.error("Employee is likely to leave")

def main():
    model=load("model.joblib")
    st.title("HR Attrition Prediction")
    st.subheader("This application helps in predicting weather any given employee is likely to leave the organization or not")
    age=st.slider("specify the age:",min_value=18,max_value=60)
    business_travel=st.number_input("specify the number of business travels:",min_value=0)
    daily_rate=st.number_input("specify daily rate:",min_value=1)
    department=st.radio("specify the department:",options=["Research & Development","Sales","Human Resources"])
    if department=="Research & Development":
        department=1
    elif department=="Sales":
        department=2
    elif department=="Human Resources":
        department=0
    distance_from_home=st.number_input("specify the distance from home in kms:",min_value=0)
    education=st.selectbox("specify the level of education on a scale of 1 to 5:",options=[1,2,3,4,5])
    education_field=st.selectbox("specify the field of education:",options=["Life Sciences","Medical","Marketing","Technical Degree","Other","Human Resources"])
    if education_field=="Life Sciences":
        education_field=1
    elif education_field=="Medical":
        education_field=3
    elif education_field=="Marketing":
        education_field=2
    elif education_field=="Technical Degree":
        education_field=5
    elif education_field=="Other":
        education_field=4
    elif education_field=="Human Resources":
        education_field=0
    environment_sat=st.slider("on a scale of 1 to 4 what is the satisfaction level with respect to environment:",min_value=1,max_value=4)
    gender=st.selectbox("gender:",options=["Male","Female"])
    if gender=="Male":
        gender=1
    elif gender=="Female":
        gender=0
    hourly_rate=st.number_input("specify hourly rate:",min_value=1)
    job_involvement=st.slider("on a scale of 1 to 4 what is the level of job involvement:",min_value=1,max_value=4)
    job_level=st.slider("on a scale of 1 to 5 what is the job level:",min_value=1,max_value=5)
    job_role=st.selectbox("specify job role:",options=["Sales Executive","Research Scientist","Laboratory Technician","Manufacturing Director","Healthcare Representative","Manager","Sales Representative","Research Director","Human Resources"])
    if job_role=="Sales Executive":
        job_role=7
    elif job_role=="Research Scientist":
        job_role=6
    elif job_role=="Laboratory Technician":
        job_role=2
    elif job_role=="Manufacturing Director":
        job_role=4
    elif job_role=="Healthcare Representative":
        job_role=0
    elif job_role=="Manager":
        job_role=3
    elif job_role=="Sales Representative":
        job_role=8
    elif job_role=="Research Director":
        job_role=5
    elif job_role=="Human Resources":
        job_role=1
    job_sat=st.slider("on a scale of 1 to 4 what is the level of job satisfaction:",min_value=1,max_value=4)
    marital_status=st.selectbox("marital status:",options=["Married","Single","Divorced"])
    if marital_status=="Married":
        marital_status=1
    elif marital_status=="Single":
        marital_status=2
    elif marital_status=="Divorced":
        marital_status=0
    monthly_rate=st.number_input("specify monthly rate:",min_value=1)
    num_comp_worked=st.number_input("specify the number of companies worked for:",min_value=0)
    overtime=st.radio("specify overtime:",options=["Yes","No"])
    if overtime=="Yes":
        overtime=1
    elif overtime=="No":
        overtime=0
    percent_sal_hike=st.slider("specify percent salary hike:",min_value=1,max_value=100)
    relation_sat=st.slider("on a scale of 1 to 4 specify the relationship satisfaction:",min_value=1,max_value=4)
    stock_op_level=st.slider("specify your stock option level from of 0 to 3:",min_value=0,max_value=3)
    train_time_last_year=st.number_input("specify the number of training recieved in last year:",min_value=0)
    work_lif_bal=st.slider("specify work life balance on a scale of 1 to 4:",min_value=1,max_value=4)
    years_at_comp=st.number_input("specify the number of years at company:",min_value=0)
    years_since_last_promo=st.number_input("specify the number of years since last promotion:",min_value=0)
    if st.button("Predict"):
        predict_func(age,business_travel,daily_rate,department,distance_from_home,education,education_field,environment_sat,gender,hourly_rate,job_involvement,job_level,job_role,job_sat,marital_status,monthly_rate,num_comp_worked,overtime,percent_sal_hike,relation_sat,stock_op_level,train_time_last_year,work_lif_bal,years_at_comp,years_since_last_promo)
        
if __name__=="__main__":
    main()

