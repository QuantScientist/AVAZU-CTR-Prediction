# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 19:34:39 2015

@author: Ivan
"""
from datetime import datetime
from csv import DictReader

validation = 50
###############################
# --- Main transformation --- #
###############################
input_file = 'data/onehot/train_df_smooth_hash_app.csv'
output_file = 'xgboost/libsvm_train_app.txt'
output_file2 = 'xgboost/libsvm_validation_app.txt'
var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/app_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        if t % validation != 0:
            new_line = []
        
            if row['click'] == '0':
                label = '0'
            elif row['click'] == '1':
                label = '1'
            else:
                break
            
            new_line.append(label)
            
            del row['id']
            del row['click']
    
            for i, item in row.items():
    
                if item in ['',0,'0']:
                    continue
                
                index = var_dict[str(item)+'.0']            
                  
                # print(i + ': ' + item + ': ' + str(index))
                
                new_item = "%s:%s" % ( index, 1 )
                new_line.append( new_item )
                
            new_line = " ".join( new_line )        
            new_line += "\n"            
            outfile.write(new_line)
            
            # print(new_line)
                
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))

with open(output_file2,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        if t % validation == 0:
            new_line = []
        
            if row['click'] == '0':
                label = '0'
            elif row['click'] == '1':
                label = '1'
            else:
                break
            
            new_line.append(label)
            
            del row['id']
            del row['click']
    
            for i, item in row.items():
    
                if item in ['',0,'0']:
                    continue
                
                index = var_dict[str(item)+'.0']            
                  
                # print(i + ': ' + item + ': ' + str(index))
                
                new_item = "%s:%s" % ( index, 1 )
                new_line.append( new_item )
                
            new_line = " ".join( new_line )        
            new_line += "\n"            
            outfile.write(new_line)
            
            # print(new_line)
                
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))

input_file = 'data/onehot/train_df_smooth_hash_site.csv'
output_file = 'xgboost/libsvm_train_site.txt'
output_file2 = 'xgboost/libsvm_validation_site.txt'
var_dict = {}
for t, row in enumerate(DictReader(open("data/onehot/site_var_dict.csv"))): # site/app
    var_dict[row['key']] = row['val']

start = datetime.now()
with open(output_file,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        if t % validation != 0:
            new_line = []
        
            if row['click'] == '0':
                label = '0'
            elif row['click'] == '1':
                label = '1'
            else:
                break
            
            new_line.append(label)
            
            del row['id']
            del row['click']
    
            for i, item in row.items():
    
                if item in ['',0,'0']:
                    continue
                
                index = var_dict[str(item)+'.0']            
                  
                # print(i + ': ' + item + ': ' + str(index))
                
                new_item = "%s:%s" % ( index, 1 )
                new_line.append( new_item )
                
            new_line = " ".join( new_line )        
            new_line += "\n"            
            outfile.write(new_line)
            
            # print(new_line)
                
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))

start = datetime.now()
with open(output_file2,"wb") as outfile:
    for t, row in enumerate(DictReader(open(input_file))):
        
        if t % validation == 0:
            new_line = []
        
            if row['click'] == '0':
                label = '0'
            elif row['click'] == '1':
                label = '1'
            else:
                break
            
            new_line.append(label)
            
            del row['id']
            del row['click']
    
            for i, item in row.items():
    
                if item in ['',0,'0']:
                    continue
                
                index = var_dict[str(item)+'.0']            
                  
                # print(i + ': ' + item + ': ' + str(index))
                
                new_item = "%s:%s" % ( index, 1 )
                new_line.append( new_item )
                
            new_line = " ".join( new_line )        
            new_line += "\n"            
            outfile.write(new_line)
            
            # print(new_line)
                
            if t % 100000 == 0:
                print("%s\t%s"%(t, str(datetime.now() - start)))
             

