# HR-Attrition-Analysis-and-Prediction
## The problem statement consisted of carefully analysing the data to come up with important insights for the HR department that suggest the reasons for employees leaving the organization and finally to create a model to predict employee attrition so that HR can take corrective and preventive measures to stop or control the attrition.
## Getting started with the problem first i imported the necessary dependencies and the data that is required for the project, then i quickly realised that a lot of data wrangling and munging is required with the data as it contained lots of problems such as null values, nuisance columns etc.
![Screenshot (43)](https://user-images.githubusercontent.com/116963622/215730903-fdb15a5e-32b4-4b9c-a3ea-cec1b8515dbd.png)
![Screenshot (44)](https://user-images.githubusercontent.com/116963622/215731395-66383f96-737f-4749-8588-444b4aab24c5.png)
![Screenshot (45)](https://user-images.githubusercontent.com/116963622/215732710-6c2581bf-e84e-4612-8da7-496e0d9c00d6.png)
## Once done with most of the wrangling part, i started carefully analysing the data and providing various interesting insights by using lots of visualization and statistical analysis.
![Screenshot (46)](https://user-images.githubusercontent.com/116963622/215733386-670a8e9e-9a63-4bbe-8d82-8a810bc65556.png)
![Screenshot (47)](https://user-images.githubusercontent.com/116963622/215733824-f99138c3-cb9f-412a-acf8-8bb168e303b9.png)
![Screenshot (48)](https://user-images.githubusercontent.com/116963622/215734264-d8460390-add0-4fda-ba0f-c2fcc00a79bd.png)
![Screenshot (49)](https://user-images.githubusercontent.com/116963622/215734832-5ef26ae0-d046-4a7b-9a7e-6f6b7936d0f6.png)
![Screenshot (50)](https://user-images.githubusercontent.com/116963622/215735220-5d412830-4d60-4d01-be32-0c3b2259f880.png)
![Screenshot (51)](https://user-images.githubusercontent.com/116963622/215735772-c7967b0b-8449-4362-8a3e-37ebd68e7281.png)
## and using such careful analysis i drew insights
![Screenshot (54)](https://user-images.githubusercontent.com/116963622/215737111-511c3cd2-531b-47ff-b863-7ff4dac30eb1.png)
![Screenshot (53)](https://user-images.githubusercontent.com/116963622/215736737-93e3b8f6-a654-4bb8-b7a9-675925b11d1d.png)
![Screenshot (52)](https://user-images.githubusercontent.com/116963622/215736417-c78fb56f-eb52-4b4b-b4be-6ea224bcaca7.png)
## then i moved ahead and started preprocessing the data for feeding it to a machine learning model, after a quite a lot of preprocessing the data was finally ready to be fed to the model.
## after this i selected decision tree as my benchmark model and fitted our data into the model and since our model on evaluation gave pretty good results hence i stuck with it.
![Screenshot (55)](https://user-images.githubusercontent.com/116963622/215740664-45642b3a-4223-4766-9ff3-c47d69c7f402.png)
![Screenshot (56)](https://user-images.githubusercontent.com/116963622/215740875-4bbbcd51-a5ed-41e5-8e5c-ff65c6fa38d9.png)
![Screenshot (57)](https://user-images.githubusercontent.com/116963622/215741113-0d92fe73-c09d-4825-aadc-a1036f17f241.png)
## and at the end i exported the model and went ahead and created a web application using it by the help of streamlit framework for the HR that can predict weather an employee is likely to leave or not leave the organization given a bunch of variables.
![Screenshot (58)](https://user-images.githubusercontent.com/116963622/215742600-aa63341f-b721-43d8-ba58-a4c0d1599e50.png)
![Screenshot (59)](https://user-images.githubusercontent.com/116963622/215743004-82d90de8-ed74-4022-9abd-79222678bfa0.png)
![Screenshot (60)](https://user-images.githubusercontent.com/116963622/215743381-8c7b717c-9558-45cb-9d35-d5743543e134.png)
![Screenshot (61)](https://user-images.githubusercontent.com/116963622/215743813-cd0cd2ed-8231-4237-bd9d-464cddb4252e.png)
## in this web application the HR just has to enter the details of the employees whom he/she wants to check weather they are likely to leave the organization or not and after entering the details they just have to click on the predict button to get the result.
![Screenshot (63)](https://user-images.githubusercontent.com/116963622/215745389-d517eb17-eca2-4f4f-b980-ba38f3267eb3.png)
![Screenshot (62)](https://user-images.githubusercontent.com/116963622/215745499-9570fc7f-c6af-4c5f-8ac0-52114616ac3d.png)
