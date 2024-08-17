import os

dictory="D:\1000_leeet_code _probelem_solution"

if not os.path.exists(dictory):
    os.makedirs(dictory)
for i in range(1,1001):
    file_name=f'python_program_{i}.py'
    file_path=os.path.join(dictory,file_name)
    with open(file_path,'w') as f:
        f.write(f"#this is leet code program python_program \t {i}.py \n")
        
print(f"1000 python files created in the '{dictory}'  directory")
    