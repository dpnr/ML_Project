
def addFeatures(dataset):
    for person in dataset:
        first_name =person['name'][0:person['name'].find(" ")]
        last_name = person['name'][person['name'].rfind(" ")+1:]
        
        #feature1
        if(  len( first_name ) > len( last_name )):
            person["name_len"] = "+"
        else:
            person["name_len"] =  "-"
        #feature2
        if( person['name'].count(" ")==2 ):
            person["middle_name"] = "+"
        else:
            person["middle_name"] = "-"
        #feature3
        if(first_name[0:1].lower() == first_name[-1:].lower() ):
            person["first_same"] = "+"
        else:
            person["first_same"] = "-"
        #feature4
        
        if( first_name[0:1].lower() < last_name[0:1].lower() ): 
            person["alphabet"] = "+"
        else:
            person["alphabet"] = "-"
        #feature5
        if(first_name[1:2].lower() in ['a','e','i','o','u']):
            person['vowel'] = "+"
        else:
            person['vowel'] = "-"
        #feature6
        if(len(last_name)%2==0):
            person["last_even"] = "+"
        else:
            person["last_even"] = "-"

    return dataset


