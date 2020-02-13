supermarket={
    'store1':{
                'name':'surender software solutions',
                'items':[
                            {'name':'python','quantity':100},
                            {'name':'java','quantity':200},
                            {'name':'bigdata','quantity':400}
                        ]
        },
    'store2':{
                'name':'roopa solutions',
                'items':[
                            {'name':'khana','quantity':100},
                            {'name':'acha_khana','quantity':200},
                            {'name':'rasmalai','quantity':300}
                        ]
            }    
}
# print(supermarket['store1']['name'])
# print(supermarket.get('store1').get('name'))

# for d in supermarket['store1']['items']:
#     print(d['name'])

# print(supermarket['store2']['items'][1]['quantity'])
for d in supermarket['store2']['items']:
    if d['name']=='acha_khana':
        print(d['quantity'])
