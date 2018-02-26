import Algorithmia

input = {
  "images": [
    "data://deeplearning/example_data/elon_musk.jpg"
  ],
  "savePaths": [
    "data://.algo/deeplearning/DeepFilter/temp/elon_space_pizza.jpg"
  ],
  "filterName": "space_pizza"
}
client = Algorithmia.client('simagLv+XbstNbx8tJ3aEcvnJ9m1')
algo = client.algo('deeplearning/DeepFilter/0.6.0')
print(algo.pipe(input)) 

'''
Web API
Connect to Algorithmia
set up with my facebook account

This is API for Image Processing
'''