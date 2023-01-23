from ZS import ZeroShotImageIdentification

#Spanish + Vision Transformer as vision backbone

zs = ZeroShotImageIdentification(lang="es")

preds = zs(image="http://images.cocodataset.org/val2017/000000039769.jpg",
            candidate_labels=["gatita", "perras", "gatas","leonas"],
            hypothesis_template="una imagen de {}",  
            )
print(preds)


'''
Prints the following
{'image': 'http://images.cocodataset.org/val2017/000000039769.jpg', 
'scores': [0.5385471, 0.0016878153, 0.45578623, 0.003978893], 
'labels': ['gatita', 'perras', 'gatas', 'leonas']
}
'''

#English + CNN based model as vision backbone

from ZS import ZeroShotImageIdentification

zsii = ZeroShotImageIdentification(model="RN50")


#Predictions
preds = zs(image="http://images.cocodataset.org/val2017/000000039769.jpg",
            candidate_labels=["birds", "lions", "cats","dogs"], 
            )
print(preds)

'''
Prints the following
{'image': 'http://images.cocodataset.org/val2017/000000039769.jpg', 
'scores': [0.00046659182, 0.0024660423, 0.9949238, 0.002143612], 
'labels': ['birds', 'lions', 'cats', 'dogs']
}
'''
